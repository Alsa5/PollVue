import random
import praw
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os
import praw

# Load environment variables from .env file
load_dotenv()

# Access environment variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
user_agent = os.getenv('USER_AGENT')

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Initialize Firebase (only once)
if not firebase_admin._apps:
    cred = credentials.Certificate("./serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# List of valid states in India
valid_states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
    "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

# Function to fetch data about Indian politics from Reddit and store it in Firebase
def fetch_and_store_indian_politics_data(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.search('flair:Politics OR flair:"Indian Politics" OR flair:"Political Discussion"', sort='new', limit=100):
        # Randomly select a state
        random_state = random.choice(valid_states)
        
        # Extract relevant data
        data = {
            'title': submission.title,
            'score': submission.score,
            'id': submission.id,
            'url': submission.url,
            'created': submission.created,
            'num_comments': submission.num_comments,
            'body': submission.selftext,
            'author': submission.author.name if submission.author else None,
            'location': random_state  # Set random state as the location
        }
        # Store data in Firestore
        db.collection('politics100').document(submission.id).set(data)

# Example usage: Fetch data from r/IndiaSpeaks or another relevant subreddit
fetch_and_store_indian_politics_data('IndiaSpeaks')
