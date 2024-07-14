from sqlalchemy import create_engine  # Import SQLAlchemy's create_engine function
from dotenv import load_dotenv  # Import load_dotenv function from dotenv package
import os  # Import os module
from create_rds_instance import create_rds_instance  # Import the create_rds_instance function from create_rds_instance.py

# Load environment variables from the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '../../environment/.env')
load_dotenv(dotenv_path)

# Define a function to create a database connection
def create_connection():
    try:
        # Create an RDS instance
        db_instance = create_rds_instance()

        # Check if the RDS instance was created successfully
        if db_instance:
            # Extract endpoint information from the RDS instance
            endpoint = db_instance['Endpoint']
            address = endpoint['Address']
            port = endpoint['Port']

            # Get database credentials from environment variables
            database = os.getenv("DB_NAME")
            user = os.getenv("DB_USER")
            password = os.getenv("DB_PASSWORD")

            # Construct the connection string for SQLAlchemy
            connection_string = f"mysql+pymysql://{user}:{password}@{address}:{port}/{database}"
            connection = create_engine(connection_string)

            # Check if the connection was successful
            if connection:
                print("Conexão bem-sucedida ao banco de dados")  # Print a success message
                return connection  # Return the database connection object

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")  # Print an error message if connection fails
        return None  # Return None if connection fails

# Establish a database connection using the create_connection function
conn = create_connection()
