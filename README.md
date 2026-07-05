# 🇰🇷 Korea Base Rate Prediction System

> 한국은행 ECOS Open API와 머신러닝(RandomForest)을 활용하여 다음 달 한국 기준금리를 예측하는 Python 백엔드 프로젝트

## 📌 Project Overview

본 프로젝트는 한국은행 **ECOS Open API**에서 경제 데이터를 자동 수집하고,
머신러닝(RandomForest)을 이용하여 **다음 달 한국 기준금리**를 예측하는 서비스입니다.

예측 모델을 FastAPI 기반 REST API로 제공하며,
Streamlit을 이용하여 사용자가 쉽게 예측 결과를 확인할 수 있도록 구현하였습니다.

또한 Docker와 Docker Compose를 적용하여 동일한 실행 환경을 제공합니다.

---

# 🏗 System Architecture

```
            ECOS Open API
                    │
                    ▼
          Data Collection
                    │
                    ▼
          Data Preprocessing
                    │
                    ▼
       Feature Engineering
                    │
                    ▼
        RandomForest Model
                    │
                    ▼
              FastAPI
                    │
            REST API
                    │
                    ▼
             Streamlit UI
```

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- Pydantic

## Machine Learning

- Scikit-learn
- RandomForest
- Joblib

## Frontend

- Streamlit

## Data

- Pandas
- ECOS Open API

## DevOps

- Docker
- Docker Compose

## Version Control

- Git
- GitHub
- SourceTree

---

# 📂 Project Structure

```
interest-rate-dashboard

├── app
│   ├── main.py
│   ├── services.py
│   ├── schemas.py
│   └── model_loader.py
│
├── frontend
│   └── streamlit_app.py
│
├── model
│   └── rf_base_rate.pkl
│
├── data
│   └── processed
│       └── feature_df.csv
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🚀 Features

### Data

- ECOS Open API 자동 데이터 수집
- 데이터 병합(Merge)
- 결측치 처리
- 분기 → 월 변환

### Feature Engineering

- Lag Feature 생성
- Target 생성(Shift)

### Machine Learning

- RandomForest 모델 학습
- Feature Importance 분석
- 모델 저장(Joblib)

### FastAPI

- REST API 제공
- Swagger(OpenAPI)
- Service Layer 분리
- Exception Handling

### Streamlit

- 예측 결과 조회
- 모델 정보 조회
- Loading Spinner
- 사용자 친화적 UI

### Docker

- Dockerfile
- Docker Compose
- 컨테이너 실행 지원

---

# 📡 API

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /model-info | 모델 정보 조회 |
| GET | /predict/latest | 최신 데이터 기준 금리 예측 |

Swagger

```
http://localhost:8000/docs
```

---

# 🐳 Docker

### Build

```bash
docker build -t interest-rate-api .
```

### Run

```bash
docker compose up
```

---

# 📷 Screenshots

### Streamlit

(프로젝트 실행 화면 추가)

### Swagger

(Swagger 화면 추가)

---

# 📈 Model

Algorithm

- RandomForest Regressor

Input

- 한국은행 ECOS 경제지표
- Lag Feature

Output

- 다음 달 한국 기준금리 예측

---

# 📚 What I Learned

이번 프로젝트를 진행하면서 다음 내용을 학습하였습니다.

- REST API 설계
- FastAPI 기반 백엔드 개발
- Service Layer 분리
- Exception Handling
- Streamlit UI 개발
- Docker 및 Docker Compose
- Git Branch 전략
- 머신러닝 모델 서비스화(Serving)

---

# ⚠ Trouble Shooting

### feature_names_in_ 오류

RandomForest 모델 저장 시 DataFrame이 아닌 NumPy 배열로 학습하여

```
AttributeError:
RandomForestRegressor has no attribute feature_names_in_
```

오류가 발생하였습니다.

CSV의 Feature 컬럼을 직접 선택하는 방식으로 해결하였습니다.

---

# 🔨 Future Improvements

- XGBoost 모델 성능 비교
- 자동 데이터 업데이트
- 모델 재학습 자동화
- AWS 배포
- CI/CD 구축

---

# 👨‍💻 Author

이나영

GitHub

https://github.com/nayoungsoso

Blog

https://blog.naver.com/seotunbread
