from aifc import Error
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


# Carrega as variáveis de ambiente do arquivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '../../environment/.env')
load_dotenv(dotenv_path)

def create_connection():
    try:    
        host        = os.getenv("DB_HOST")
        port        = os.getenv("DB_PORT")
        database    = os.getenv("DB_NAME")
        user        = os.getenv("DB_USER")
        password    = os.getenv("DB_PASSWORD")

        # Conectando via sqlalchemy
        connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        connection = create_engine(connection_string)

        if connection:
            print("Conexão bem-sucedida ao banco de dados")
            return connection

    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    

# Estabelecendo Conexao 
conn = create_connection()
