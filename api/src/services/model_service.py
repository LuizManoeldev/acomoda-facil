from src.utils.s3_utils import load_model_from_s3
from src.config.config import BUCKET_NAME, MODEL_KEY
from src.models.inference_request import InferenceRequest
from src.logging.logger import logger

class ModelService:
    model = load_model_from_s3(BUCKET_NAME, MODEL_KEY)
    
    @classmethod
    def predict(cls, request: InferenceRequest):
        input_data = [
            request.label_avg_price_per_room,
            request.no_of_adults,
            request.no_of_children,
            request.required_car_parking_space,
            request.arrival_year,
            request.arrival_month,
            request.no_of_special_requests,
            request.type_of_meal_plan,
            request.room_type_reserved,
            request.market_segment_type,
            request.booking_status
        ]
        prediction = cls.model.predict([input_data])[0]
        logger.info(f"Prediction: {prediction} for input: {input_data}")
        return prediction