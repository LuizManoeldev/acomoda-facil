from src.utils.s3_utils import load_model_from_s3

class ModelService:
    def __init__(self):
        self.model = load_model_from_s3()
    
    def predict(self, dmatrix):
        prediction = self.model.predict(dmatrix)
        return prediction
