from fastapi import  HTTPException, Header
from ..core.firebase_utils import get_firestore_client

def verify_api_key(x_api_key: str = Header(...)):
    """
    Middleware that extracts and verifies the API key from request headers.
    The key is validated against Firestore's 'api_keys' collection.
    """
    if not x_api_key:
        raise HTTPException(status_code=401, detail="Unauthorized: API Key is required")

    db = get_firestore_client()
    api_key_doc = db.collection("api_keys").document("x_api_key").get()

    if not api_key_doc.exists:
        raise HTTPException(status_code=403, detail="Forbidden: Invalid API Key")

    api_key_data = api_key_doc.to_dict()
    if api_key_data.get("key") != x_api_key:
        raise HTTPException(status_code=403, detail="Forbidden: Invalid API Key2")

    return api_key_doc.to_dict()  # Return API key details (like owner info)
