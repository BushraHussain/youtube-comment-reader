# uv run youtube-all-comment-reader
from googleapiclient.discovery import build
from dotenv import load_dotenv
from youtube_comment_reader.reader import get_video_comments
import os

# Load environment variables from .env file
load_dotenv()

# Get API Key from environment variables
API_KEY = os.getenv("API_KEY")

# Initialize YouTube API Client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Function to get videos from a channel
def get_channel_videos(channel_id):
    videos = []
    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        maxResults=10,  # Number of videos to fetch
        order='date'    # Latest videos first
    )
    response = request.execute()

    for item in response['items']:
        # Check if the item has 'videoId'
        if item['id']['kind'] == "youtube#video":
            video_id = item['id']['videoId']
            videos.append(video_id)

    return videos

def main():
    # Example usage:
    CHANNEL_ID = 'UCu8v7dLyAix44NXjKCNNgRA'  
    video_ids = get_channel_videos(CHANNEL_ID)

    # Read all videos comments
    for vid in video_ids:
        comments = get_video_comments(vid)
        print(f"Comments for Video ID: {vid}")
        for c in comments:
            print(c)
