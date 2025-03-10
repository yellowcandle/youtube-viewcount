import streamlit as st
import pandas as pd

# Cache the YouTube data fetching to avoid repeated API calls
@st.cache_data(ttl=86400)  # Cache for 1 day
def get_cached_video_stats(video_id):
    return get_video_stats(video_id)

# Streamlit app
st.set_page_config(page_title=" YouTube MV 觀看次數", layout="wide")

# Display latest YouTube view count
st.title("Latest YouTube Statistics")
st.markdown("Displaying the latest statistics for the specified YouTube video:")

# Use the specific video ID
video_id = '4d7a8jEW3K4'

with st.spinner("Fetching video statistics..."):
    title, view_count, upload_date = get_cached_video_stats(video_id)
    
    if title and view_count and upload_date:
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
    else:
        st.error("Failed to retrieve video statistics. Please check the video ID and try again.")
