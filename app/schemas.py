from pydantic import BaseModel

# API 응답(Response) 데이터 형식을 정의하는 클래스
class LatestPredictionResponse(BaseModel):
    # 예측 기준 날짜
    prediction_date: str
    # 예측된 다음 달 기준금리
    predicted_base_rate: float


class RootResponse(BaseModel):
    project: str
    version: str
    docs: str


class HealthResponse(BaseModel):
    status: str
    message: str
    model_status: str


class ModelInfoResponse(BaseModel):
    model_status: str
    model_type: str