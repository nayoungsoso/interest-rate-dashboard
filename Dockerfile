# python이 설치된 이미지(Linux)
FROM python:3.12-slim

# 컨테이너 내부 작업 폴더 생성
WORKDIR /app

# requirements.txt 먼저 복사
COPY requirements.txt .

# 필요한 패키지 설치(캐시 최적화)
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 전체 복사
COPY . .

# FastAPI 포트
EXPOSE 8000

# FastAPI 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]