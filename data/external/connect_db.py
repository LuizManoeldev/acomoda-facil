from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from create_rds_instance import create_rds_instance

# Carrega as variáveis de ambiente do arquivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '../../environment/.env')
load_dotenv(dotenv_path)

def create_connection():
    try:
        db_instance = create_rds_instance()
        if db_instance:
            endpoint = db_instance['Endpoint']
            address = endpoint['Address']
            port = endpoint['Port']
            database = os.getenv("DB_NAME")
            user = os.getenv("DB_USER")
            password = os.getenv("DB_PASSWORD")

            # Conectando via sqlalchemy
            connection_string = f"mysql+pymysql://{user}:{password}@{address}:{port}/{database}"
            connection = create_engine(connection_string)

            if connection:
                print("Conexão bem-sucedida ao banco de dados")
                return connection
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Estabelecendo Conexao
conn = create_connection()
