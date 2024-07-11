import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
from create_rds_instance import create_rds_instance

# Carrega as variáveis de ambiente do arquivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '../../environment/.env')
load_dotenv(dotenv_path)

def create_connection():
    try:
        db_instance = create_rds_instance()
        if db_instance:
            endpoint = db_instance['Endpoint']
            host = endpoint['Address']
            port = endpoint['Port']
            database = os.getenv("DB_NAME")
            user = os.getenv("DB_USER")
            password = os.getenv("DB_PASSWORD")

            # Conecta ao banco de dados MySQL
            connection = mysql.connector.connect(
                host=host,
                port=port,
                database=database,
                user=user,
                password=password
            )

            if connection.is_connected():
                print("Conexão bem-sucedida ao banco de dados")
                return connection

    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        print('Conexão bem-sucedida')
        conn.close()