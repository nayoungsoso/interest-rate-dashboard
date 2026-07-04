from fastapi import FastAPI
from app.model_loader import load_model
# 예측 서비스 함수
from app.services import predict_latest
# API 응답 형식 import
from app.schemas import (
    RootResponse,
    HealthResponse,
    ModelInfoResponse,
    LatestPredictionResponse,
)

app = FastAPI(
    title="Korea Interest Rate Prediction API",
    description="한국 금리 예측 API",
    version="0.1.0",
)

model = load_model()

@app.get("/", response_model=RootResponse)
def root():
    return {
        "project": "Korea Interest Rate Prediction API",
        "version": "0.1.0",
        "docs": "/docs"
    }

@app.get("/health", response_model=HealthResponse)
def health_check():
    return {
        "status": "healthy",
        "message": "API server is running",
        "model_status": "loaded"
    }

@app.get("/model-info", response_model=ModelInfoResponse)
def model_info():
    return {
        "model_status": "loaded",
        "model_type": type(model).__name__
    }

# 최신 데이터를 이용하여 다음달 금리를 예측하는 API
@app.get(
    "/predict/latest",
    response_model=LatestPredictionResponse
)
def predict_latest_base_rate():
    return predict_latest(model)