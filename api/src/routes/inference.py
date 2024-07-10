from fastapi import APIRouter, HTTPException
from src.models.inference_request import InferenceRequest
from src.services.model_service import ModelService

router = APIRouter()

@router.post("/api/v1/inference")
def make_inference(request: InferenceRequest):
    try:
        prediction = ModelService.predict(request)
        return {"result": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
