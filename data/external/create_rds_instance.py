import boto3  # Import the boto3 library for AWS interactions
import os  # Import the os module for operating system interactions
from dotenv import load_dotenv  # Import load_dotenv function from dotenv package

# Load environment variables from the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '../../environment/.env')
load_dotenv(dotenv_path)

# Retrieve environment variables
PROFILE_NAME            = os.getenv('PROFILE_NAME')             # AWS profile name for boto3 session
DB_INSTANCE_IDENTIFIER  = os.getenv('DB_INSTANCE_IDENTIFIER')   # RDS DB instance identifier
DB_INSTANCE_CLASS       = os.getenv('DB_INSTANCE_CLASS')        # RDS instance class (e.g., db.t2.micro)
DB_ENGINE               = os.getenv('DB_ENGINE')                # Database engine type (e.g., mysql)
DB_NAME                 = os.getenv('DB_NAME')                  # Database name
DB_USER                 = os.getenv('DB_USER')                  # Database username
DB_PASSWORD             = os.getenv('DB_PASSWORD')              # Database password
DB_PORT                 = os.getenv('DB_PORT')                  # Database port
DB_SUBNET_GROUP         = os.getenv('DB_SUBNET_GROUP')          # DB subnet group for RDS instance

# Configure boto3 client for RDS using the specified AWS profile
boto_session = boto3.Session(profile_name=PROFILE_NAME)
boto3.setup_default_session(profile_name=PROFILE_NAME)
rds_client = boto3.client('rds')  # Initialize boto3 client for RDS

def create_rds_instance():
    try:
        # Check if the RDS instance already exists
        response = rds_client.describe_db_instances(DBInstanceIdentifier=DB_INSTANCE_IDENTIFIER)
        db_instances = response['DBInstances']
        if len(db_instances) > 0:
            print(f"The database instance {DB_INSTANCE_IDENTIFIER} already exists.")
            return db_instances[0]  # Return the first instance found

    except rds_client.exceptions.DBInstanceNotFoundFault:
        print(f"The database instance {DB_INSTANCE_IDENTIFIER} does not exist. Creating a new instance.")

    try:
        # Create a new RDS instance
        response = rds_client.create_db_instance(
            DBInstanceIdentifier=DB_INSTANCE_IDENTIFIER,
            DBInstanceClass=DB_INSTANCE_CLASS,
            Engine=DB_ENGINE,
            DBName=DB_NAME,
            MasterUsername=DB_USER,
            MasterUserPassword=DB_PASSWORD,
            Port=int(DB_PORT),
            AllocatedStorage=20,
            BackupRetentionPeriod=7,
            MultiAZ=False,
            EngineVersion='8.0',
            PubliclyAccessible=True,
            StorageType='gp2',
            DBSubnetGroupName=DB_SUBNET_GROUP
        )

        db_instance = response['DBInstance']
        print(f"Creating database instance {DB_INSTANCE_IDENTIFIER}...")

        # Wait until the instance is available
        waiter = rds_client.get_waiter('db_instance_available')
        waiter.wait(DBInstanceIdentifier=DB_INSTANCE_IDENTIFIER)
        
        # Retrieve the instance details again after creation
        response = rds_client.describe_db_instances(DBInstanceIdentifier=DB_INSTANCE_IDENTIFIER)
        db_instance = response['DBInstances'][0]  # Access the first returned instance

        print(f"The database instance {DB_INSTANCE_IDENTIFIER} is available.")
        return db_instance

    except Exception as e:
        print(f"Error creating the database instance: {e}")
        return None

if __name__ == "__main__":
    # Create an RDS instance using the defined function
    db_instance = create_rds_instance()

    # If an instance was successfully created, print connection details
    if db_instance:
        endpoint = db_instance['Endpoint']
        address = endpoint['Address']
        port = endpoint['Port']
        print(f"Connect to the database using endpoint: {address} and port: {port}")
