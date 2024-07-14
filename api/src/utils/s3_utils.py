import tarfile
import os
import boto3
import xgboost as xgb
from src.config.config import PROFILE_NAME, BUCKET_NAME, MODEL_KEY

def load_model_from_s3():
    session = boto3.Session(profile_name=PROFILE_NAME)
    s3 = session.client('s3')
    try:
        local_model_path = 'model.tar.gz'

        s3 = boto3.client('s3')
        s3.download_file(BUCKET_NAME, MODEL_KEY, local_model_path)
        print(f"Modelo baixado para: {local_model_path}")

        # Caminho para extrair o modelo
        extracted_model_path = 'xgboost-model'

        # Extrair o arquivo tar.gz
        with tarfile.open(local_model_path, 'r:gz') as tar:
            tar.extractall(path=extracted_model_path)
        
        # Verificar os arquivos extraídos
        extracted_files = os.listdir(extracted_model_path)
        print(f"Arquivos extraídos: {extracted_files}")

        # Verificar se o modelo está presente após a extração
        model_file = os.path.join(extracted_model_path, 'modelo.joblib')
        if os.path.exists(model_file):
            print(f"Modelo encontrado em: {model_file}")
        else:
            print(f"Modelo não encontrado em: {model_file}")
            return None
        
        # Carregar o modelo XGBoost
        model = xgb.Booster()
        model.load_model(model_file)
        print("Modelo carregado com sucesso.")

        return model

    except Exception as e:
        print(f"Falha ao carregar o modelo do S3: {str(e)}")
        return None
