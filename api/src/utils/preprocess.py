import pandas as pd

def preprocess_input(data):
    df = pd.DataFrame([data])
    df = pd.get_dummies(df, columns=[
        'type_of_meal_plan', 'room_type_reserved', 
        'market_segment_type', 'booking_status'
    ])
    
    expected_columns = [
        'no_of_adults', 'no_of_children', 'required_car_parking_space', 
        'lead_time', 'arrival_year', 'arrival_month', 'arrival_date', 
        'repeated_guest', 'no_of_previous_cancellations', 
        'no_of_special_requests', 'type_of_meal_plan_Meal Plan 1', 
        'type_of_meal_plan_Meal Plan 2', 'type_of_meal_plan_Meal Plan 3', 
        'type_of_meal_plan_Not Selected', 'room_type_reserved_Room_Type 1', 
        'room_type_reserved_Room_Type 2', 'room_type_reserved_Room_Type 3', 
        'room_type_reserved_Room_Type 4', 'room_type_reserved_Room_Type 5', 
        'room_type_reserved_Room_Type 6', 'room_type_reserved_Room_Type 7', 
        'market_segment_type_Aviation', 'market_segment_type_Complementary', 
        'market_segment_type_Corporate', 'market_segment_type_Offline', 
        'market_segment_type_Online', 'booking_status_Canceled', 
        'booking_status_Not_Canceled'
    ]
    
    for col in expected_columns:
        if (col not in df.columns) and ('repeated_guest' not in col):
            df[col] = 0
    
    df = df[expected_columns]
    
    return df
