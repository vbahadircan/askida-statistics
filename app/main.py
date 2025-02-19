from fastapi import FastAPI
from .core.firebase_utils import initialize_firebase
from .routers import analytics

def create_app() -> FastAPI:

    # Initialize Firebase when the app starts
    initialize_firebase()

    app = FastAPI(
        title="Firebase Analytics API",
        description="Endpoints for user and transaction analytics",
        version="0.1.0",
    )

    # Include the analytics router with a prefix
    app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])

    return app

app = create_app()