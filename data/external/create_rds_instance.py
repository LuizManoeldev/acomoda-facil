import boto3
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '../../environment/.env')
load_dotenv(dotenv_path)

# Pegue as variáveis de ambiente
PROFILE_NAME = os.getenv('PROFILE_NAME')
DB_INSTANCE_IDENTIFIER = os.getenv('DB_INSTANCE_IDENTIFIER')
DB_INSTANCE_CLASS = os.getenv('DB_INSTANCE_CLASS')
DB_ENGINE = os.getenv('DB_ENGINE')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')

# Configura o cliente do boto3 para o RDS
boto_session = boto3.Session(profile_name=PROFILE_NAME)
boto3.setup_default_session(profile_name=PROFILE_NAME)
rds_client = boto3.client('rds')

def create_rds_instance():
    try:
        # Verifica se a instância do RDS já existe
        response = rds_client.describe_db_instances(DBInstanceIdentifier=DB_INSTANCE_IDENTIFIER)
        db_instances = response['DBInstances']
        if len(db_instances) > 0:
            print(f"A instância do banco de dados {DB_INSTANCE_IDENTIFIER} já existe.")
            return db_instances[0]
    except rds_client.exceptions.DBInstanceNotFoundFault:
        print(f"A instância do banco de dados {DB_INSTANCE_IDENTIFIER} não existe. Criando uma nova instância.")

    try:
        # Cria uma nova instância do RDS
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
        )

        db_instance = response['DBInstance']
        print(f"Criando a instância do banco de dados {DB_INSTANCE_IDENTIFIER}...")

        # Espera até que a instância esteja disponível
        waiter = rds_client.get_waiter('db_instance_available')
        waiter.wait(DBInstanceIdentifier=DB_INSTANCE_IDENTIFIER)
        
        # Obtém novamente os detalhes da instância após criação
        response = rds_client.describe_db_instances(DBInstanceIdentifier=DB_INSTANCE_IDENTIFIER)
        db_instance = response['DBInstances'][0]  # Acessa a primeira instância retornada

        print(f"A instância do banco de dados {DB_INSTANCE_IDENTIFIER} está disponível.")
        return db_instance

    except Exception as e:
        print(f"Erro ao criar a instância do banco de dados: {e}")
        return None

#if __name__ == "__main__":
 #   db_instance = create_rds_instance()
  #  if db_instance:
   #     endpoint = db_instance['Endpoint']
    #    address = endpoint['Address']
     #   port = endpoint['Port']
      #  print(f"Conecte-se ao banco de dados usando o endpoint: {address} e porta: {port}")