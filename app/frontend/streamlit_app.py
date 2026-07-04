import requests
import streamlit as st

# FastAPI 서버 주소
API_BASE_URL = "http://127.0.0.1:8000"


# 최신 예측 결과를 FastAPI에서 가져오는 함수
def get_latest_prediction():
    response = requests.get(f"{API_BASE_URL}/predict/latest")

    # 요청 실패 시 에러 발생
    response.raise_for_status()

    return response.json()


# 모델 정보를 FastAPI에서 가져오는 함수
def get_model_info():
    response = requests.get(f"{API_BASE_URL}/model-info")

    # 요청 실패 시 에러 발생
    response.raise_for_status()

    return response.json()


# Streamlit 페이지 기본 설정
st.set_page_config(
    page_title="한국 기준금리 예측 시스템",
    page_icon="📈",
    layout="centered",
)

# 화면 제목
st.title("한국 기준금리 예측")

# 프로젝트 설명
st.write(
    "한국은행 ECOS Open API 기반 경제지표와 머신러닝 모델을 활용하여 "
    "다음 달 기준금리를 예측하는 서비스."
)

st.divider()

# 예측 결과 조회 버튼
if st.button("최신 기준금리 예측하기"):
    
    try:
        # API 호출 중 로딩 메시지 표시
        with st.spinner("FastAPI 서버에서 예측 결과를 가져오는 중입니다..."):
            prediction = get_latest_prediction()
            model_info = get_model_info()

        # API 호출 성공 메시지
        st.success("예측 결과를 성공적으로 불러왔습니다.")

        st.divider()

        # 예측 결과 출력
        st.subheader("📌 예측 결과")

        # 예측 기준일과 예측 금리를 2개 컬럼으로 표시
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="예측 기준일",
                value=prediction["prediction_date"]
            )

        with col2:
            st.metric(
                label="예측 기준금리",
                value=f"{prediction['predicted_base_rate']}%"
            )

        st.write(f"예측 기준 날짜: {prediction['prediction_date']}")

        st.divider()

        # 모델 정보 호출
        model_info = get_model_info()

        st.subheader("모델 정보")
        st.write(f"모델 상태: {model_info['model_status']}")
        st.write(f"모델 종류: {model_info['model_type']}")

    except requests.exceptions.ConnectionError:
        st.error("FastAPI 서버에 연결할 수 없습니다. 서버가 실행 중인지 확인해주세요.")

    except requests.exceptions.HTTPError as e:
        st.error(f"API 요청 중 오류가 발생했습니다: {e}")

    except Exception as e:
        st.error(f"예상하지 못한 오류가 발생했습니다: {e}")