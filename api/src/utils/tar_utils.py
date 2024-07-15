import tarfile  
from io import BytesIO
from api.src.logging.logger import logger

def extract_tar_gz(fileobj):
    fileobj_bytes = fileobj.read()  # Read the contents of the file object into bytes
    fileobj_bytesio = BytesIO(fileobj_bytes)  # Create a BytesIO object from the read bytes
    
    try:
        with tarfile.open(fileobj=fileobj_bytesio, mode="r:gz") as tar:
            member = tar.getmembers()[0]  # Get the first member (file) from the tar archive
            model_bytes = tar.extractfile(member).read()  # Read the contents of the member (file) into bytes
        return model_bytes  # Return the bytes of the extracted model file
    except Exception as e:
        logger.error(f'Falha em extrair o objeto: {fileobj}. ERROR: {str(e)}')