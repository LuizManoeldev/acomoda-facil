from connect_db import conn as connection  # Import the database connection object from connect_db.py
import pandas as pd  # Import the pandas library for data manipulation

if __name__ == "__main__":
    try:
        # Load the dataframe from a CSV file
        csv_path = 'data/raw/hotel_reservations.csv'
        reservations_dataframe = pd.read_csv(csv_path)

        # Send the dataframe to the RDS database
        reservations_dataframe.to_sql('reservations', con=connection, if_exists='replace', index=False)
        
        # Close the database connection
        connection.dispose()
        print("DataFrame sent successfully and connection closed")
    
    except Exception as e:
        print(f"Error sending the DataFrame: {e}")
