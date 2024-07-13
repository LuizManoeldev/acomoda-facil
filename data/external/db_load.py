from aifc import Error
from connect_db import conn as connection
import pandas as pd

if __name__ == "__main__":
    try:
        # Carregando dataframe
        reservations_dataframe = pd.read_csv('../assets/csv_files/hotel_reservations.csv')

        # Enviando dataframe para o RDS
        # Nome da tabela, conexao com o banco, replace se ja existir,                             
        reservations_dataframe.to_sql('reservations', con=connection, if_exists='replace', index=False)

        # Encerrando a conexao
        connection.dispose()
        print("Conexão fechada")
    except Error:
        print(Error)