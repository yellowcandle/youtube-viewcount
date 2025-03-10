import streamlit as st
import pandas as pd
from googleapiclient.discovery import build
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get YouTube API key from environment variable
API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_video_stats(video_id):
    """
    Fetch YouTube video statistics using the YouTube Data API
    
    Args:
        video_id (str): YouTube video ID
        
    Returns:
        tuple: (title, view_count, upload_date) or (None, None, None) if error occurs
    """
    try:
        # Create YouTube API client
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        
        # Get video details
        video_response = youtube.videos().list(
            part='snippet,statistics',
            id=video_id
        ).execute()
        
        # Check if video exists
        if not video_response['items']:
            return None, None, None
            
        # Extract relevant information
        video_data = video_response['items'][0]
        title = video_data['snippet']['title']
        view_count = int(video_data['statistics']['viewCount'])
        
        # Format the upload date
        upload_date_raw = video_data['snippet']['publishedAt']
        upload_date = datetime.fromisoformat(upload_date_raw.replace('Z', '+00:00')).strftime('%Y-%m-%d')
        
        return title, view_count, upload_date
        
    except Exception as e:
        st.error(f"Error fetching video statistics: {e}")
        return None, None, None

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
