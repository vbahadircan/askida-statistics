# Firebase FastAPI Analytics API

This project provides a FastAPI service to expose endpoints for Firebase-based analytics. It uses the Firebase Admin SDK to work with Firestore and Firebase Auth.

## Project Structure

- **Root Directory**
  - `.env` – Environment variables.
  - `serviceAccountKey.json` – Firebase service account credentials.
  - `requirements.txt` – Python dependencies.
  - `Dockerfile` – Docker build instructions.
- **app/**
  - `main.py` – Application entry point.
  - **core/**
    - [`config.py`](app/core/config.py) – Loads env variables and configures Firebase credentials.
    - [`firebase_utils.py`](app/core/firebase_utils.py) – Initializes Firebase App and provides Firestore/Auth clients.
    - [`api_key_utils.py`](app/core/api_key_utils.py) – Contains API key verification logic.
  - **routers/**
    - [`analytics.py`](app/routers/analytics.py) – Contains routes related to analytics (transactions and users).

