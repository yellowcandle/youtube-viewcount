import streamlit as st
import pandas as pd
from datetime import datetime

# Streamlit app
st.set_page_config(page_title="YouTube Video Viewer", layout="wide")

# Display YouTube video
st.title("YouTube Video Viewer")
st.markdown("Watch the YouTube video below:")

# Specific video ID
video_id = '4d7a8jEW3K4'

# Display video embed
st.video(f"https://www.youtube.com/watch?v={video_id}")

# Add instructions for viewing count on YouTube
st.markdown("""
### How to see the current view count:
1. Click on the video to open it in YouTube
2. The view count is displayed below the video title
""")

# Add some additional information about the video
st.subheader("Video Information")
st.markdown(f"""
- **Video ID**: {video_id}
- **YouTube URL**: [https://www.youtube.com/watch?v={video_id}](https://www.youtube.com/watch?v={video_id})
""")

# Note about the app
st.info("""
This simple app embeds a YouTube video using Streamlit's st.video component.
To see the actual view count, you need to click through to YouTube.

This version doesn't require the YouTube Data API.
""")
