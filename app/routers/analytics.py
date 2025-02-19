from fastapi import APIRouter, Depends
from ..core.api_key_utils import verify_api_key
from datetime import datetime
from ..core.firebase_utils import get_firestore_client, get_auth_client

router = APIRouter()

@router.get("/total-transactions")
def total_transactions(api_key=Depends(verify_api_key)):
    """
    Fetches all businesses and counts the total number of documents
    inside their 'islemler' subcollections.
    """
    db = get_firestore_client()
    total_transaction_count = 0

    try:
        # Get all businesses
        businesses_docs = db.collection("businesses").get()

        # Loop through each business document
        for business in businesses_docs:
            business_id = business.id  # Business document ID

            # Reference the 'islemler' subcollection inside the business document
            islemler_ref = db.collection("businesses").document(business_id).collection("islemler")

            # Count transactions in this subcollection
            islemler_count = len(islemler_ref.get())  # Count number of documents
            total_transaction_count += islemler_count

        return {"total_transactions": total_transaction_count}

    except Exception as e:
        return {"error": str(e)}


@router.get("/total-users")
def total_users(api_key=Depends(verify_api_key)):
    """
    Returns the total number of users in Firebase Auth.
    """
    auth_client = get_auth_client()
    total = 0

    try:
        page = auth_client.list_users()  # First page
        while page:
            for _ in page.users:
                total += 1
            page = page.get_next_page()
        return {"total_users": total}
    except Exception as e:
        return {"error": str(e)}