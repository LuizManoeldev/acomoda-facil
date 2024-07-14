from get_rds_data import base_reservations, engine  # Import base_reservations dataframe and engine from get_rds_data.py
import pandas as pd  # Import pandas library for data manipulation

try:
    # Remove unnecessary columns from base_reservations dataframe
    prepared_base = base_reservations.drop(['no_of_previous_bookings_not_canceled', 
                                            'Booking_ID',
                                            'no_of_weekend_nights',
                                            'no_of_week_nights'], axis=1)
    
    # Create the label_avg_price_per_room column based on given criteria
    prepared_base['label_avg_price_per_room'] = pd.cut(prepared_base['avg_price_per_room'],
                                                   bins=[-float('inf'), 85, 115, float('inf')],
                                                   labels=[1, 2, 3])
    
    # Convert label_avg_price_per_room to categorical and map values 1, 2, 3 to 0, 1, 2
    prepared_base['label_avg_price_per_room'] = prepared_base['label_avg_price_per_room'].astype('category')
    mapping = {1: 0, 2: 1, 3: 2}
    prepared_base['label_avg_price_per_room'] = prepared_base['label_avg_price_per_room'].cat.rename_categories(mapping)

    # Reorder columns with label_avg_price_per_room as the first column
    target_column = 'label_avg_price_per_room'
    columns = [target_column] + [col for col in prepared_base.columns if col != target_column]
    prepared_base = prepared_base[columns]
    
    # Remove the original avg_price_per_room column
    prepared_base = prepared_base.drop(['avg_price_per_room'], axis=1)

    # Convert categorical columns into dummy/indicator variables
    prepared_base = pd.get_dummies(prepared_base, columns=['type_of_meal_plan', 'room_type_reserved', 'market_segment_type', 'booking_status'])

    # Write prepared data to another SQL table named 'reservations_prepared'
    prepared_base.to_sql('reservations_prepared', con=engine, if_exists='replace', index=False)
    print("DataFrame written to SQL table successfully.")

except Exception as e:
    print(f"Error writing to the database: {e}")
