from connect_db import conn as connection
import pandas as pd

if __name__ == "__main__":
    try:
        # Carregando dataframe
        csv_path = 'data/raw/hotel_reservations.csv'
        reservations_dataframe = pd.read_csv(csv_path)

        # Enviando dataframe para o RDS
        #                             Nome da tabela, conexao com o banco - 
        reservations_dataframe.to_sql('reservations', con=connection, if_exists='replace', index=False)
        
        # Encerrando a conexão
        connection.dispose()
        print("Envio do DataFrame realizado com sucesso e conexão fechada")
    except Exception as e:
        print(f"Erro ao enviar o DataFrame: {e}")
