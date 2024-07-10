from pydantic import BaseModel

class InferenceRequest(BaseModel):
    label_avg_price_per_room: int
    no_of_adults: int
    no_of_children: int
    required_car_parking_space: int
    arrival_year: int
    arrival_month: int
    no_of_special_requests: int
    type_of_meal_plan: str
    room_type_reserved: str
    market_segment_type: str
    booking_status: str