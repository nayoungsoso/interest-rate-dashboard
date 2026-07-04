from fastapi import FastAPI
from app.model_loader import load_model

app = FastAPI(
    title="Korea Interest Rate Prediction API",
    description="한국 금리 예측 API",
    version="0.1.0",
)

model = load_model()

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "Interest Rate Prediction API is running"
    }

@app.get("/model-info")
def model_info():
    return {
        "model_status": "loaded",
        "model_type": type(model).__name__
    }