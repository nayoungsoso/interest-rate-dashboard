from fastapi import FastAPI

app = FastAPI(
    title="Korea Base Rate Prediction API",
    description="한국 기준금리 예측 API",
    version="0.1.0",
)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Base Rate Prediction API is running"}