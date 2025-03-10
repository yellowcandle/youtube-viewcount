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