import boto3
import pickle
from src.logging.logger import logger

def load_model_from_s3(bucket_name: str, model_key: str):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=model_key)
    model = pickle.loads(response['Body'].read())
    logger.info(f"Model loaded from S3: {bucket_name}/{model_key}")
    return model