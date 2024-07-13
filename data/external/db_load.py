from connect_db import conn as connection
import pandas as pd

if __name__ == "__main__":
    try:
        # Carregando dataframe
        reservations_dataframe = pd.read_csv('C:/Atividades compassUOL/Sprint 4-5/sprints-4-5-pb-aws-maio/assets/csv_files/hotel_reservations.csv')

        # Enviando dataframe para o RDS
        reservations_dataframe.to_sql('reservations', con=connection, if_exists='replace', index=False)
        
        # Encerrando a conexão
        connection.dispose()
        print("Envio do DataFrame realizado com sucesso e conexão fechada")
    except Exception as e:
        print(f"Erro ao enviar o DataFrame: {e}")
