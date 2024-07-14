import os  # Import the os module for operating system interactions
from dotenv import load_dotenv  # Import load_dotenv function from dotenv package
from sqlalchemy import create_engine  # Import create_engine function from SQLAlchemy
import pandas as pd  # Import pandas library for data manipulation

from data.external.connect_db import conn as db_connection

# SQL query to retrieve data from the 'reservations' table
sql_query = "SELECT * FROM reservations"

# Create a dataframe from the SQL query result
try:
    base_reservations = pd.read_sql(sql_query, db_connection)
    #print(base_reservations)  # Optionally print the dataframe
except Exception as e:
    print(f"Error executing query: {e}")  # Print an error message if query execution fails
