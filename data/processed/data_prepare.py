from get_rds_data import base_reservations, engine
import pandas as pd

try:
    # Removendo colunas desnecessarias
    prepared_base = base_reservations.drop(['no_of_previous_bookings_not_canceled', 
                                            'Booking_ID',
                                            'no_of_weekend_nights',
                                            'no_of_week_nights'], axis = 1)
    
    # Criar a coluna label_avg_price_per_room com base nos critérios fornecidos
    prepared_base['label_avg_price_per_room'] = pd.cut(prepared_base['avg_price_per_room'],
                                                   bins=[-float('inf'), 85, 115, float('inf')],
                                                   labels=[1, 2, 3])
    
    prepared_base['label_avg_price_per_room'] = prepared_base['label_avg_price_per_room'].astype('category')

    #Mapear os valores de 1, 2, 3 para 0, 1, 2
    mapping = {1: 0, 2: 1, 3: 2}
    prepared_base['label_avg_price_per_room'] = prepared_base['label_avg_price_per_room'].cat.rename_categories(mapping)

    # Reeordenando colunas
    target_column = 'label_avg_price_per_room'

    columns = [target_column] + [col for col in prepared_base.columns if col != target_column]
    prepared_base = prepared_base[columns]
    
    # Removendo a coluna original de preços
    prepared_base = prepared_base.drop(['avg_price_per_room'], axis = 1)

    # Convertendo colunas categoricas   
    prepared_base = pd.get_dummies(prepared_base, columns=['type_of_meal_plan', 'room_type_reserved', 'market_segment_type', 'booking_status'])

    # Escrevendo dados preparados em outra tabela
    prepared_base.to_sql('reservations_prepared', con=engine, if_exists='replace', index=False)
    print("DataFrame written to SQL table successfully.")

except Exception as e:
    print(f"Erro ao escrever no banco de dados:{e}")