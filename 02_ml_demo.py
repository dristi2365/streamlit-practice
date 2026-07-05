import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Train a simple model on the iris dataset
from sklearn.datasets import load_iris

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Streamlit UI
st.title("🌸 Iris Flower Classifier")
st.write("Adjust the sliders to predict the flower type")

sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 5.0, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 3.0, 1.0)

input_data = pd.DataFrame([[sepal_length, sepal_width, 
                             petal_length, petal_width]],
                          columns=iris.feature_names)

prediction = model.predict(input_data)[0]
flower_names = iris.target_names

st.subheader("Prediction:")
st.success(f"🌸 This is a **{flower_names[prediction]}**!")

confidence = model.predict_proba(input_data)[0]
st.write("Confidence scores:")
for flower, conf in zip(flower_names, confidence):
    st.progress(float(conf), text=f"{flower}: {conf:.2%}")