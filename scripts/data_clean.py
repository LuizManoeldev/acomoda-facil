from get_rds_data import base_reservations, engine

# TEST
try:
    # PREPARAR DADOS...
    base_reservations.to_sql('reservations_test', con=engine, if_exists='replace', index=False)
    print("DataFrame written to SQL table successfully.")
except Exception as e:
    print(f"Erro ao escrever no banco de dados: {e}")