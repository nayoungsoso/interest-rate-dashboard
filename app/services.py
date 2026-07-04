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
    # 모델 입력에 사용할 Feature 컬럼 선택
    feature_columns = [col for col in df.columns if col not in ["date", "target"]]

    # Feature 컬럼이 없는 경우 예외 처리
    if not feature_columns:
        raise ValueError("No feature columns found.")

    # 최신 데이터 선택
    latest_row = df.sort_values("date").iloc[-1]
    prediction_date = latest_row["date"]

    # 예측 입력 데이터 생성
    X = latest_row[feature_columns].to_frame().T

    prediction = model.predict(X)[0]
    # API 응답 형태로 반환
    return {
        "prediction_date": str(prediction_date),
        "predicted_base_rate": round(float(prediction), 2)
    }