import os
import base64
import json
import firebase_admin
from firebase_admin import credentials

def initialize_firebase():
    firebase_key = os.getenv("FIREBASE_KEY")
    if not firebase_key:
        raise ValueError("FIREBASE_KEY environment variable not set")

    decoded_key = base64.b64decode(firebase_key).decode()
    cred = credentials.Certificate(json.loads(decoded_key))
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)
        
initialize_firebase()
