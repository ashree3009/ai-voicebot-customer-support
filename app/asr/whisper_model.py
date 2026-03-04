import whisper
import tempfile
from app.core.logger import get_logger
from app.core.config import settings

logger = get_logger()

class WhisperASR:

    def __init__(self):
        logger.info("Loading Whisper model...")
        self.model = whisper.load_model(settings.ASR_MODEL_NAME)
        logger.info("Whisper model loaded successfully")

    def transcribe_audio(self, audio_file):

        try:
            # Save uploaded audio temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                temp_audio.write(audio_file.file.read())
                temp_path = temp_audio.name

            logger.info(f"Processing audio file: {temp_path}")

            result = self.model.transcribe(temp_path)

            text = result["text"]

            logger.info(f"Transcription: {text}")

            return text

        except Exception as e:
            logger.error(f"ASR Error: {e}")
            return "Unable to transcribe audio"