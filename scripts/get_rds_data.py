import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# Carregando variabeis de ambiente
dotenv_path = os.path.join(os.path.dirname(__file__), '../environment/.env')
load_dotenv(dotenv_path)

# Variaveis de ambiente
host        = os.getenv("DB_HOST")
port        = os.getenv("DB_PORT")
database    = os.getenv("DB_NAME")
user        = os.getenv("DB_USER")
password    = os.getenv("DB_PASSWORD")

# Conectando via sqlalchemy
connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_string)

# Query de consulta
sql_query = "SELECT * FROM reservations"

# Criando data frame
try:
    base_reservations = pd.read_sql(sql_query, engine)
    print(base_reservations)
except Exception as e:
    print(f"Erro ao executar a consulta: {e}")
