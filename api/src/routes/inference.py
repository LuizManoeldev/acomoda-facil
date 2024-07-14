from fastapi import APIRouter, HTTPException 
import xgboost as xgb  # 
from src.models.inference_request import InferenceRequest  
from src.services.model_service import ModelService  

router = APIRouter()  # Create an instance of APIRouter for defining API endpoints

@router.post("/api/v1/inference") 
def make_inference(request: InferenceRequest): 
    try:
        model_service = ModelService()                   # Create an instance of ModelService for model operations
        request_dict = request.dict()                    # Convert InferenceRequest object to dictionary
        processed_data = preprocess_input(request_dict)  # Preprocess input data using preprocess_input function
        dmatrix = xgb.DMatrix(processed_data)            # Create XGBoost DMatrix from processed data
        prediction = model_service.predict(dmatrix)      # Make prediction using ModelService
        
        # Increment the prediction by 1 and convert it to integer
        prediction_int = int(prediction[0]) + 1
        
        return {"result": prediction_int}  # Return prediction result as JSON response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Raise HTTPException with status code 500 and error message
