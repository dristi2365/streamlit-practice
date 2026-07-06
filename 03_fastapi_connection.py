import streamlit as st
import requests

st.title("🌸 Iris Classifier — FastAPI + Streamlit")
st.write("Frontend talks to FastAPI backend for predictions")

sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 5.0, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 3.0, 1.0)

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
            st.success(f"🌸 Predicted: **{result['prediction']}**")
            st.write("Confidence scores:")
            for flower, conf in result["confidence"].items():
                st.progress(conf, text=f"{flower}: {conf:.2%}")
        else:
            st.error(f"Backend error: {response.status_code}")
    except requests.exceptions.ConnectionError:
        st.error("⚠️ Can't reach the backend. Is FastAPI running?")
    except requests.exceptions.Timeout:
        st.error("⚠️ Backend took too long to respond.")