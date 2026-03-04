import torch
from transformers import DistilBertTokenizerFast
from transformers import DistilBertForSequenceClassification
import torch.nn.functional as F
from app.core.config import settings
from app.core.logger import get_logger
import pickle

logger = get_logger()

class IntentClassifier:

    def __init__(self):

        logger.info("Loading intent classification model...")

        self.tokenizer = DistilBertTokenizerFast.from_pretrained(
            settings.INTENT_MODEL_PATH
        )

        self.model = DistilBertForSequenceClassification.from_pretrained(
            settings.INTENT_MODEL_PATH
        )

        self.model.eval()

        with open("models/intent_model/label_encoder.pkl", "rb") as f:
            self.label_encoder = pickle.load(f)

        logger.info("Intent model loaded successfully")

    def predict_intent(self, text):

        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)

        with torch.no_grad():
            outputs = self.model(**inputs)

        probs = F.softmax(outputs.logits, dim=1)

        confidence, predicted = torch.max(probs, dim=1)

        intent = self.label_encoder.inverse_transform([predicted.item()])[0]

        return intent, confidence.item()