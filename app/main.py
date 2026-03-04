from fastapi import FastAPI
from app.api.routes import router
from app.core.logger import get_logger

logger = get_logger()

logger.info("Voicebot API started")

app = FastAPI(
    title="AI Voicebot API",
    description="Customer Support Voicebot",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "Voicebot API running"}