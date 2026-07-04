from pathlib import Path
import pandas as pd

# 프로젝트 루트 경로
BASE_DIR = Path(__file__).resolve().parent.parent
# 예측에 사용할 Feature 데이터 경로
DATA_PATH = BASE_DIR / "data" / "processed" / "feature_df.csv"

def predict_latest(model):
    # Feature 데이터 불러오기
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Feature data not found: {DATA_PATH}")
    df = pd.read_csv(DATA_PATH)

    # 모델이 학습한 Feature가 CSV에 모두 존재하는지
    missing_features = [
        feature
        for feature in model.feature_names_in_
        if feature not in df.columns
    ]

    # 하나라도 없으면 예측 불가
    if missing_features:
        raise KeyError(f"Missing model features: {missing_features}")


    # 날짜 기준으로 정렬 후 가장 최신 데이터 선택
    latest_row = df.sort_values("date").iloc[-1]
    # 예측 기준 날짜 저장
    prediction_date = latest_row["date"]

    # 모델 입력에 필요 없는 date 컬럼 제거
    X = latest_row[model.feature_names_in_].to_frame().T

    prediction = model.predict(X)[0]
    # API 응답 형태로 반환
    return {
        "prediction_date": str(prediction_date),
        "predicted_base_rate": round(float(prediction), 2)
    }