from fastapi import APIRouter, HTTPException
import xgboost as xgb
from src.models.inference_request import InferenceRequest
from src.services.model_service import ModelService
from src.utils.preprocess import preprocess_input

router = APIRouter()

@router.post("/api/v1/inference")
def make_inference(request: InferenceRequest):
    try:
        model_service = ModelService()
        request_dict = request.dict()
        processed_data = preprocess_input(request_dict)
        dmatrix = xgb.DMatrix(processed_data)
        prediction = model_service.predict(dmatrix)
        
        # Incrementar a previsão por 1 e convertê-la para inteiro
        prediction_int = int(prediction[0]) + 1
        
        return {"result": prediction_int}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
