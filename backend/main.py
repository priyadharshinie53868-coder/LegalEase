import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import router

app = FastAPI(
    title="LegalEase API",
    description="Backend service for AI-Powered Legal Document Generator",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include main API routes
app.include_router(router)


if __name__ == "__main__":
    host = os.getenv("BACKEND_HOST", "127.0.0.1")
    port = int(os.getenv("BACKEND_PORT", 8000))
    uvicorn.run("backend.main:app", host=host, port=port, reload=True)
