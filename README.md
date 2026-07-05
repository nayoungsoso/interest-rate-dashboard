# 🇰🇷 Korea Base Rate Prediction System

> 한국은행 ECOS(Open API)와 머신러닝(RandomForest)을 활용하여 다음 달 한국 기준금리를 예측하는 Python 백엔드 서비스

---

## 📌 Project Overview

본 프로젝트는 한국은행 **ECOS Open API**에서 경제 데이터를 자동 수집하고,
머신러닝(RandomForest)을 활용하여 **다음 달 한국 기준금리**를 예측하는 서비스입니다.

프로젝트는 **2024.12 ~ 2025.05까지 진행한 4인 팀 프로젝트**를 기반으로 개발되었습니다.

이후 **Python 백엔드 취업 포트폴리오 완성도를 높이기 위해 개인적으로 1차 리팩토링**을 진행하였으며,

FastAPI 기반 REST API 구축, Streamlit Dashboard 개발, Docker/Docker Compose 적용, 프로젝트 구조 개선 및 문서화를 수행하였습니다.

---

# 📋 Project Information

| Item | Description |
|------|-------------|
| Project | Korea Base Rate Prediction System |
| Development Period | 2024.12 ~ 2025.05 |
| Team | 4 Members |
| Refactoring | 2026 (Personal Refactoring) |
| Project Type | Team Project → Personal Backend Portfolio |
| Backend | FastAPI |
| Frontend | Streamlit |
| Machine Learning | RandomForest |
| DevOps | Docker / Docker Compose |

---

# 👨‍💻 My Contributions

## Team Project

- 한국은행 ECOS Open API 경제 데이터 수집
- 데이터 전처리 및 Feature Engineering
- Lag Feature 생성
- 머신러닝(RandomForest) 모델 개발
- 모델 성능 비교(RandomForest, XGBoost, LightGBM)

## Personal Refactoring

프로젝트 종료 후 백엔드 포트폴리오를 목적으로 개인 리팩토링을 진행하였습니다.

### Backend

- FastAPI 기반 REST API 구축
- Service Layer 분리
- Pydantic Response Model 적용
- Exception Handling 추가
- Swagger(OpenAPI) 적용

### Frontend

- Streamlit Dashboard 개발
- FastAPI API 연동
- 예측 결과 시각화
- Loading Spinner 및 사용자 예외 처리

### DevOps

- Dockerfile 작성
- Docker Image 생성
- Docker Container 실행
- Docker Compose 적용

### Project Management

- Git Branch 전략 적용
- GitHub 프로젝트 관리
- 기술 블로그 작성
- README 문서화

---

# 🏗 System Architecture

```text
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
          REST API Server
                     │
                     ▼
          Streamlit Dashboard
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

## Collaboration

- Git
- GitHub
- SourceTree

---

# 📂 Project Structure

```text
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
├── data
│   └── processed
│       └── feature_df.csv
│
├── model
│   └── rf_base_rate.pkl
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🚀 Features

## Data Pipeline

- ECOS Open API 자동 데이터 수집
- 데이터 병합(Merge)
- 결측치 처리
- 분기 → 월 변환
- Duplicate 제거

## Feature Engineering

- Lag1
- Lag3
- Lag6
- Target Shift(-1)

## Machine Learning

- RandomForest 모델 학습
- Feature Importance 분석
- 모델 저장(Joblib)

## FastAPI

- REST API 제공
- Swagger(OpenAPI)
- Response Model(Pydantic)
- Service Layer 분리
- Exception Handling

## Streamlit

- 예측 결과 조회
- 모델 정보 조회
- Loading Spinner
- 사용자 친화적 UI

## Docker

- Dockerfile
- Docker Compose
- 컨테이너 기반 실행 환경

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

### Streamlit Dashboard

> 실행 화면 추가 예정

### Swagger

> 실행 화면 추가 예정

---

# 📈 Machine Learning Model

### Algorithm

- RandomForest Regressor

### Input

- 한국은행 ECOS 경제지표
- Lag Feature

### Output

- 다음 달 기준금리 예측

---

# 🔄 Refactoring

프로젝트 종료 후 Python 백엔드 포트폴리오 완성도를 높이기 위해 개인적으로 리팩토링을 진행하였습니다.

## 개선 내용

- FastAPI 기반 REST API 구축
- Service Layer 분리
- Response Model(Pydantic) 적용
- Exception Handling 추가
- Streamlit Dashboard 개발
- Docker 환경 구성
- Docker Compose 적용
- Git Branch 전략 적용
- 프로젝트 문서화(README)
- 기술 블로그 작성

---

# ⚠ Trouble Shooting

### RandomForest feature_names_in_ 오류

RandomForest 모델 저장 시 DataFrame이 아닌 NumPy 배열로 학습되어

```
AttributeError:
RandomForestRegressor has no attribute feature_names_in_
```

오류가 발생하였습니다.

CSV의 Feature 컬럼을 직접 선택하는 방식으로 수정하여 해결하였습니다.

---

# 📚 What I Learned

이번 프로젝트를 통해 다음 기술을 실제 서비스에 적용해볼 수 있었습니다.

- REST API 설계
- FastAPI 기반 백엔드 개발
- Service Layer 설계
- Exception Handling
- Streamlit Dashboard 개발
- Docker 및 Docker Compose
- Git Branch 전략
- 머신러닝 모델 서비스화(Model Serving)

---

# 🔨 Future Improvements

- ECOS 데이터 자동 업데이트
- 모델 자동 재학습
- AWS 배포
- CI/CD 구축(GitHub Actions)
- PostgreSQL 연동
- Redis 적용

---

# 📝 Technical Blog

프로젝트 개발 과정은 아래 블로그에 정리하였습니다.

- FastAPI 구축
- Prediction API 개발
- Exception Handling
- Streamlit 연동
- Docker 적용

👉 https://blog.naver.com/seotunbread

---

# 👨‍💻 Author

GitHub

https://github.com/nayoungsoso

Blog

https://blog.naver.com/seotunbread
