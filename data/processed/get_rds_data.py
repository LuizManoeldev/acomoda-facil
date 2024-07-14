import os  # Import the os module for operating system interactions
from dotenv import load_dotenv  # Import load_dotenv function from dotenv package
from sqlalchemy import create_engine  # Import create_engine function from SQLAlchemy
import pandas as pd  # Import pandas library for data manipulation

# Load environment variables from the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '../../environment/.env')
load_dotenv(dotenv_path)

# Retrieve environment variables for database connection
host        = os.getenv("DB_HOST")      # Database host address
port        = os.getenv("DB_PORT")      # Database port
database    = os.getenv("DB_NAME")      # Database name
user        = os.getenv("DB_USER")      # Database username
password    = os.getenv("DB_PASSWORD")  # Database password

# Create a connection string for SQLAlchemy
connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_string)  # Create SQLAlchemy engine

# SQL query to retrieve data from the 'reservations' table
sql_query = "SELECT * FROM reservations"

# Create a dataframe from the SQL query result
try:
    base_reservations = pd.read_sql(sql_query, engine)
    #print(base_reservations)  # Optionally print the dataframe
except Exception as e:
    print(f"Error executing query: {e}")  # Print an error message if query execution fails
