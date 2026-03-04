from fastapi import APIRouter, UploadFile, File
from app.asr.whisper_model import WhisperASR
from app.nlp.intent_model import IntentClassifier
from app.nlp.response_generator import ResponseGenerator
from app.tts.tts_engine import TTSEngine
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api", tags=["Voicebot"])
asr_model = WhisperASR()
intent_model = IntentClassifier()
response_generator = ResponseGenerator()
tts_engine = TTSEngine()


@router.post("/transcribe")
async def transcribe(audio: UploadFile = File(...)):
    
    text = asr_model.transcribe_audio(audio)

    return {
        "transcription": text
    }

@router.post("/predict-intent")
async def predict_intent(text: str):

    intent, confidence = intent_model.predict_intent(text)

    return {
        "intent": intent,
        "confidence": confidence
    }

@router.post("/generate-response")
async def generate_response(intent: str):

    response = response_generator.generate(intent)

    return {
        "intent": intent,
        "response": response
    }

@router.post("/synthesize")
async def synthesize(text: str):

    audio_path = tts_engine.synthesize(text)

    return FileResponse(
        audio_path,
        media_type="audio/mpeg",
        filename="response.mp3"
    )

@router.post("/voicebot")
async def voicebot(audio: UploadFile = File(...)):

    # Step 1 — Speech to Text
    text = asr_model.transcribe_audio(audio)

    # Step 2 — Intent Prediction
    intent, confidence = intent_model.predict_intent(text)

    # Step 3 — Generate Response
    response_text = response_generator.generate(intent)

    # Step 4 — Convert Response to Speech
    audio_path = tts_engine.synthesize(response_text)

    return FileResponse(
        audio_path,
        media_type="audio/mpeg",
        filename="voicebot_response.mp3"
    )
