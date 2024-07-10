from fastapi import FastAPI
from src.routes.inference import router as inference_router
from src.config.config import PORT, HOST

app = FastAPI()

app.include_router(inference_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, HOST, PORT)