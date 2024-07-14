import tarfile  
import os  
import boto3 
import xgboost as xgb  
from src.config.config import PROFILE_NAME, BUCKET_NAME, MODEL_KEY  

def load_model_from_s3():
    # Create a session using boto3 with the specified AWS profile
    session = boto3.Session(profile_name=PROFILE_NAME)
    s3 = session.client('s3')  # Create an S3 client using the session
    
    try:
        local_model_path = 'model.tar.gz'  
        s3.download_file(BUCKET_NAME, MODEL_KEY, local_model_path)  # Download model archive from S3 to local path
        print(f"Modelo baixado para: {local_model_path}") 
        
        extracted_model_path = 'xgboost-model'  
        if not os.path.exists(extracted_model_path):
            os.makedirs(extracted_model_path)  # Create directory if it doesn't exist
        
        with tarfile.open(local_model_path, 'r:gz') as tar:
            tar.extractall(path=extracted_model_path)  # Extract model files from the tar archive
        
        extracted_files = os.listdir(extracted_model_path)  # List extracted files from the directory
        print(f"Arquivos extraídos: {extracted_files}") 
        
        model_file = os.path.join(extracted_model_path, 'xgboost-model')
        
        if os.path.exists(model_file):  # Check if the model file exists
            print(f"Modelo encontrado em: {model_file}")  
        else:
            print(f"Modelo não encontrado em: {model_file}")  
            return None
        
        model = xgb.Booster()  # Create an instance of XGBoost Booster
        model.load_model(model_file)  # Load the model from the specified model file
        print("Modelo carregado com sucesso.") 
        
        return model  # Return the loaded XGBoost model
    
    except Exception as e:
        print(f"Falha ao carregar o modelo do S3: {str(e)}")  
        return None
