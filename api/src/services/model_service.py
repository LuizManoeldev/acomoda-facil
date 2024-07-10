from src.utils.s3_utils import load_model_from_s3
from src.config.config import BUCKET_NAME, MODEL_KEY
from src.models.inference_request import InferenceRequest
from src.logging.logger import logger

class ModelService:
    model = load_model_from_s3(BUCKET_NAME, MODEL_KEY)
    
    @classmethod
    def predict(cls, request: InferenceRequest):
        input_data = [
            request.no_of_adults,
            request.no_of_children,
            request.type_of_meal_plan,
            
        ]
        prediction = cls.model.predict([input_data])[0]
        logger.info(f"Prediction: {prediction} for input: {input_data}")
        return prediction