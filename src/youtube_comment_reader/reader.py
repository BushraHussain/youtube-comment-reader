# uv run youtube-comment-reader
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get variables from environment
API_KEY = os.getenv('API_KEY')
VIDEO_ID = os.getenv('VIDEO_ID')

# Initialize YouTube API Client 
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_video_comments(video_id):
    comments = []
    # API call to get comments
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=50,  # Maximum 100 tak le sakte hain
        textFormat='plainText'
    )
    response = request.execute()

    # Extract comments
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments


def main():
    # Call function to print the comments
    video_comments = get_video_comments(VIDEO_ID)
    for idx, comment in enumerate(video_comments, start=1):
        print(f"{idx}: {comment}")