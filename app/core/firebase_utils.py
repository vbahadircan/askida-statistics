import firebase_admin
from firebase_admin import credentials, firestore, auth
from .config import FIREBASE_SERVICE_ACCOUNT_PATH

def initialize_firebase():
    """
    Initializes the Firebase Admin SDK using a service account if not already initialized.
    """
    try:
        firebase_admin.get_app()
        # If the default app is already initialized, do nothing
    except ValueError:
        cred = credentials.Certificate(FIREBASE_SERVICE_ACCOUNT_PATH)
        firebase_admin.initialize_app(cred)

def get_firestore_client():
    """
    Returns a Firestore client. Make sure to call `initialize_firebase()` first.
    """
    return firestore.client()

def get_auth_client():
    """
    Returns an Auth client. Make sure to call `initialize_firebase()` first.
    """
    return auth