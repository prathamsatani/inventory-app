import firebase_admin
from firebase_admin import credentials, firestore, auth

def initialize_firebase():
    """
    Initializes the Firebase Admin SDK with the provided credentials.
    """
    # Load the service account key JSON file
    cred = credentials.Certificate('./backend/secrets/harisumiran-19997-firebase-adminsdk-fbsvc-d7a3d2272c.json')
    
    # Initialize the Firebase app
    firebase_admin.initialize_app(cred)
    
    # Optionally, you can also initialize Firestore and Auth services
    db = firestore.client()
    auth_client = auth.Client()
    
    return db, auth_client