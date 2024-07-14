from fastapi import APIRouter, HTTPException
from src.models.inference_request import InferenceRequest
from src.services.model_service import ModelService

router = APIRouter()

@router.post("/api/v1/inference")
def make_inference(request: InferenceRequest):
    try:
        model_service = ModelService()  # Crie uma instância do ModelService

        # Converta os dados da requisição para um dicionário
        request_dict = request.dict()

        # Chame o método predict do ModelService com os dados da requisição
        prediction = model_service.predict(request_dict)
        return {"result": prediction}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
