import streamlit as st
from PIL import Image
import pandas as pd

st.title("📁 File Upload Demo")

# Image upload
st.subheader("Upload an Image")
image_file = st.file_uploader("Choose an image", 
                               type=["jpg", "jpeg", "png"])
if image_file:
    image = Image.open(image_file)
    st.image(image, caption="Uploaded Image", 
             use_column_width=True)
    st.write(f"File name: {image_file.name}")
    st.write(f"File size: {image_file.size} bytes")

# CSV upload
st.subheader("Upload a CSV")
csv_file = st.file_uploader("Choose a CSV file", 
                              type=["csv"])
if csv_file:
    df = pd.read_csv(csv_file)
    st.write(f"Shape: {df.shape}")
    st.dataframe(df.head())
    st.line_chart(df.select_dtypes(include='number').iloc[:, 0])