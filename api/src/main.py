from fastapi import FastAPI
import uvicorn
from api.src.routes.inference import router as inference_router
from api.src.config.config import PORT, HOST

app = FastAPI()

app.include_router(inference_router)

if __name__ == "__main__":
    uvicorn.run(app, HOST, PORT)