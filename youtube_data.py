from googleapiclient.discovery import build
from datetime import datetime
import pandas as pd
import os
import dotenv

dotenv.load_dotenv()

video_id = '4d7a8jEW3K4'

def get_video_stats(video_id):
    """
    Fetch video statistics from YouTube Data API v3.
    
    Args:
        video_id (str): YouTube video ID (e.g., 'dQw4w9WgXcQ' from https://www.youtube.com/watch?v=dQw4w9WgXcQ)
    
    Returns:
        tuple: (title, view_count, upload_date) where:
            - title (str): Video title
            - view_count (int): Number of views 
            - upload_date (str): Video upload date in YYYY-MM-DD format
    """
    # API credentials
    API_KEY = os.getenv('YOUTUBE_API_KEY')
    
    try:
        # Create YouTube API client
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        
        # Request video details
        request = youtube.videos().list(
            part='statistics,snippet',
            id=video_id
        )
        response = request.execute()
        
        # Check if video exists
        if not response['items']:
            raise ValueError(f"No video found with ID: {video_id}")
        
        # Extract data
        video_data = response['items'][0]
        title = video_data['snippet']['title']
        view_count = int(video_data['statistics']['viewCount'])
        upload_date = video_data['snippet']['publishedAt'][:10]  # Get YYYY-MM-DD format
        
        return title, view_count, upload_date
        
    except Exception as e:
        print(f"Error fetching video data: {str(e)}")
        return None, None, None

def write_to_csv(video_id, title, views, upload_date):
    """
    Print YouTube video statistics (simplified version).
    
    Args:
        video_id (str): YouTube video ID
        title (str): Video title
        views (int): View count
        upload_date (str): Upload date in YYYY-MM-DD format
    """
    try:
        # Calculate views per day
        days_since_upload = (datetime.now() - datetime.strptime(upload_date, '%Y-%m-%d')).days
        views_per_day = round(views / days_since_upload) if days_since_upload > 0 else views
        
        print(f"Video: {title}")
        print(f"ID: {video_id}")
        print(f"Views: {views:,}")
        print(f"Upload Date: {upload_date}")
        print(f"Views Per Day: {views_per_day:,}")
            
    except Exception as e:
        print(f"Error processing video data: {str(e)}")
