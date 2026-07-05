import streamlit as st

# Title and description
st.title("My First Streamlit App 🎉")
st.write("This is a simple demo of Streamlit basics")

# Text input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello {name}! 👋")

# Slider
age = st.slider("Select your age:", 1, 100, 21)
st.write(f"You are {age} years old")

# Selectbox
city = st.selectbox("Select your city:", 
                    ["Kathmandu", "Bhaktapur", 
                     "Pokhara", "Lalitpur"])
st.write(f"You are from {city}")

# Button
if st.button("Click me!"):
    st.success("Button clicked! 🎊")
    st.balloons()

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is a sidebar")
option = st.sidebar.radio("Choose one:",
                          ["Option A", 
                           "Option B", 
                           "Option C"])
st.sidebar.write(f"You chose: {option}")