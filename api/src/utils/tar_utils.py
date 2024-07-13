import tarfile
from io import BytesIO

def extract_tar_gz(fileobj):
    fileobj_bytes = fileobj.read()
    fileobj_bytesio = BytesIO(fileobj_bytes)
    with tarfile.open(fileobj=fileobj_bytesio, mode="r:gz") as tar:
        member = tar.getmembers()[0]
        model_bytes = tar.extractfile(member).read()
    return model_bytes