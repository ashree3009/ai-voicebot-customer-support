from gtts import gTTS
import tempfile
from app.core.logger import get_logger

logger = get_logger()

class TTSEngine:

    def __init__(self, language="en"):
        self.language = language

    def synthesize(self, text):

        try:
            logger.info("Generating speech from text")

            tts = gTTS(text=text, lang=self.language)

            temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")

            tts.save(temp_audio.name)

            logger.info(f"Audio generated: {temp_audio.name}")

            return temp_audio.name

        except Exception as e:
            logger.error(f"TTS Error: {e}")
            return None