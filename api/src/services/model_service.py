from src.utils.s3_utils import load_model_from_s3  

class ModelService:
    def __init__(self):
        self.model = load_model_from_s3()  # Initialize ModelService by loading model from S3
    
    def predict(self, dmatrix):
        prediction = self.model.predict(dmatrix)  # Use the loaded model to make predictions on dmatrix
        return prediction  # Return the predictions
