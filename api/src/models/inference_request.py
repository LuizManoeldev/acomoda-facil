from pydantic import BaseModel  # Import BaseModel from pydantic for creating data models

# Define a data model using BaseModel from pydantic
class InferenceRequest(BaseModel):
    no_of_adults: int
    no_of_children: int
    required_car_parking_space: int
    lead_time: int
    arrival_year: int
    arrival_month: int
    arrival_date: int
    repeated_guest: int
    no_of_previous_cancellations: int
    no_of_special_requests: int
    type_of_meal_plan: str
    room_type_reserved: str
    market_segment_type: str
    booking_status: str
