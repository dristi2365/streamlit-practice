import streamlit as st
import requests

st.title("Iris Predictor - Session State")

# Initialize session state
if "last_result" not in st.session_state:
    st.session_state.last_result = None
if "history" not in st.session_state:
    st.session_state.history = []

sepal_length = st.slider("Sepal length", 4.0, 8.0, 5.4)
sepal_width = st.slider("Sepal width", 2.0, 4.5, 3.4)
petal_length = st.slider("Petal length", 1.0, 7.0, 1.3)
petal_width = st.slider("Petal width", 0.1, 2.5, 0.2)

if st.button("Predict"):
    try:
        response = requests.post(
            "http://localhost:8000/predict",
            json={
                "sepal_length": sepal_length,
                "sepal_width": sepal_width,
                "petal_length": petal_length,
                "petal_width": petal_width
            },
            timeout=5
        )
        if response.status_code == 200:
            result = response.json()
            st.session_state.last_result = result
            st.session_state.history.append(result["prediction"])
        else:
            st.error(f"Backend error: {response.status_code}")
    except requests.exceptions.ConnectionError:
        st.error("⚠️ Can't reach the backend. Is FastAPI running?")
    except requests.exceptions.Timeout:
        st.error("⚠️ Backend took too long to respond.")

# This block runs on EVERY rerun, not just after clicking Predict
# so the last prediction stays visible even if you move a slider after
if st.session_state.last_result:
    result = st.session_state.last_result
    st.success(f"🌸 Predicted: **{result['prediction']}**")
    for flower, conf in result["confidence"].items():
        st.progress(conf, text=f"{flower}: {conf:.2%}")

if st.session_state.history:
    st.write("Prediction history this session:", st.session_state.history)

if st.button("Clear history"):
    st.session_state.history = []
    st.session_state.last_result = None