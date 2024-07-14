import joblib
import boto3
from io import BytesIO
from src.utils.preprocess import preprocess_input
from src.utils.s3_utils import load_model_from_s3

class ModelService:
    def __init__(self):
        self.model = load_model_from_s3()
    
    def predict(self, request):
        prediction = self.model.predict(request)
        return prediction
