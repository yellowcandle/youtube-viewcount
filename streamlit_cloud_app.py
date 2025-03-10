import streamlit as st
import pandas as pd
from datetime import datetime

# Streamlit app
st.set_page_config(page_title="YouTube MV 觀看次數", layout="wide")

# Display latest YouTube view count
st.title("Latest YouTube Statistics")
st.markdown("Displaying the latest statistics for the specified YouTube video:")

# Use the specific video ID - this would normally come from an API call
video_id = '4d7a8jEW3K4'

# In a real app, these would come from the YouTube API
# For demo purposes, we're using hardcoded values
title = "因為你"
view_count = 1234567
upload_date = "2022-08-16" 

st.success("Video statistics retrieved successfully!")

# Create columns for displaying the data
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Video Title", title)

with col2:
    st.metric("View Count", f"{view_count:,}")

with col3:
    st.metric("Upload Date", upload_date)
    
# Calculate views per day
days_since_upload = (pd.Timestamp.now() - pd.Timestamp(upload_date)).days
views_per_day = round(view_count / days_since_upload) if days_since_upload > 0 else view_count

st.metric("Views Per Day", f"{views_per_day:,}")

# Display video embed
st.video(f"https://www.youtube.com/watch?v={video_id}")

# Add a note about the simplified version
st.info("""
This is a simplified demo version of the app that doesn't make actual API calls to YouTube.
In the full version, this app would fetch real-time statistics from the YouTube Data API.

To run the full version locally:
1. Get a YouTube Data API key from Google Cloud Console
2. Set up your .env file with your API key
3. Install the required dependencies from requirements.txt
""")
