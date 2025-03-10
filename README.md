# YouTube View Count App

A simple Streamlit application to display the latest view count for a YouTube video.

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your YouTube API key:
   - Get an API key from the [Google Cloud Console](https://console.cloud.google.com/)
   - Enable the YouTube Data API v3
   - Copy the `.env.example` file to `.env` and add your API key
   ```
   cp .env.example .env
   ```
   - Edit the `.env` file and replace `your-api-key-here` with your actual API key

## Running the App

To run the Streamlit app:

```
streamlit run streamlit_app.py
```

The app will open in your browser and display the latest view count for the specified YouTube video.

## Changing the Video ID

To display statistics for a different YouTube video, edit the `youtube_data.py` file and change the `video_id` variable to the desired YouTube video ID. For example:

```python
video_id = 'dQw4w9WgXcQ'  # Replace with your video ID
```

You can get the video ID from the YouTube URL. For example, in `https://www.youtube.com/watch?v=dQw4w9WgXcQ`, the video ID is `dQw4w9WgXcQ`.

## Alternative Versions

This repository includes multiple versions of the app for different deployment scenarios:

### 1. Full Version (streamlit_app.py)
- Uses the YouTube Data API to fetch real-time statistics
- Requires a YouTube API key
- Shows detailed statistics including view count, upload date, and views per day
- To run: `streamlit run streamlit_app.py`

### 2. Simplified Demo Version (streamlit_cloud_app.py)
- Uses hardcoded values instead of API calls
- Does not require a YouTube API key
- Shows the same UI as the full version
- Perfect for deploying to Streamlit Cloud without API key setup
- To run: `streamlit run streamlit_cloud_app.py`

### 3. Minimal iframe Version (iframe_app.py)
- Simply embeds the YouTube video
- To see the view count, users need to click through to YouTube
- No API dependencies at all
- To run: `streamlit run iframe_app.py`

## Deployment on Streamlit Cloud

If you're deploying to Streamlit Cloud and having issues with the Google API dependencies, use one of the alternative versions:

1. Rename `streamlit_cloud_app.py` to `streamlit_app.py` before deployment
2. Use `minimal_requirements.txt` instead of the full `requirements.txt`

This way, you can still deploy a working app without dealing with API key setup in Streamlit Cloud.