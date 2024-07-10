from fastapi import FastAPI
from src.routes.inference import router as inference_router

app = FastAPI()

app.include_router(inference_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)