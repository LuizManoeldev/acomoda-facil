from io import BytesIO
import boto3
import joblib
from src.utils.tar_utils import extract_tar_gz
from src.config.config import PROFILE_NAME
from src.logging.logger import logger

def load_model_from_s3(bucket_name: str, model_key: str):
    session = boto3.Session(profile_name=PROFILE_NAME)
    s3 = session.client('s3')
    try:
        response = s3.get_object(Bucket=bucket_name, Key=model_key)
        model_bytes = extract_tar_gz(response['Body'])
        model = joblib.load(BytesIO(model_bytes))
        logger.info(f"Model loaded from S3: {bucket_name}/{model_key}")
        return model
    except Exception as e:
        logger.error(f"Failed to load model from S3: {bucket_name}/{model_key}. Error: {str(e)}")
        return None
