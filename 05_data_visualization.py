import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("📊 Data Visualization in Streamlit")

# Sample traffic data (relevant to your hackathon idea!)
data = {
    "intersection": ["Kalanki", "Koteshwor", "Maitighar", 
                     "Ratnapark", "Baneshwor", "Tinkune"],
    "morning_traffic": [95, 88, 72, 85, 78, 91],
    "evening_traffic": [92, 95, 68, 88, 82, 89],
    "avg_speed_kmh": [8, 6, 15, 10, 12, 7]
}

df = pd.DataFrame(data)

# Show the dataframe
st.subheader("Traffic Data Table")
st.dataframe(df)

# Bar chart
st.subheader("Morning vs Evening Traffic Density")
fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(len(df["intersection"]))
width = 0.35
ax.bar(x - width/2, df["morning_traffic"], 
       width, label="Morning", color="steelblue")
ax.bar(x + width/2, df["evening_traffic"], 
       width, label="Evening", color="salmon")
ax.set_xticks(x)
ax.set_xticklabels(df["intersection"], rotation=15)
ax.set_ylabel("Traffic Density (%)")
ax.legend()
st.pyplot(fig)

# Line chart using streamlit native
st.subheader("Average Speed by Intersection")
st.line_chart(df.set_index("intersection")["avg_speed_kmh"])

# Metrics
st.subheader("Quick Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Most Congested", "Koteshwor", "Evening peak")
col2.metric("Least Congested", "Maitighar", "Avg 15 km/h")
col3.metric("Overall Avg Speed", "9.7 km/h", "-2.3 from yesterday")

# Selectbox to filter
st.subheader("Filter by Intersection")
selected = st.selectbox("Choose intersection:", 
                         df["intersection"])
row = df[df["intersection"] == selected].iloc[0]
st.write(f"**Morning traffic:** {row['morning_traffic']}%")
st.write(f"**Evening traffic:** {row['evening_traffic']}%")
st.write(f"**Average speed:** {row['avg_speed_kmh']} km/h")