import pandas as pd
import torch
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

# Load dataset
df = pd.read_csv("dataset/intents.csv")

texts = df["text"].tolist()
labels = df["intent"].tolist()

# Load label encoder
with open("models/intent_model/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

true_labels = label_encoder.transform(labels)

# Load tokenizer and model
tokenizer = DistilBertTokenizerFast.from_pretrained("models/intent_model")
model = DistilBertForSequenceClassification.from_pretrained("models/intent_model")

model.eval()

predictions = []

for text in texts:
    inputs = tokenizer(text, return_tensors="pt", truncation=True)

    with torch.no_grad():
        outputs = model(**inputs)

    predicted = torch.argmax(outputs.logits, dim=1).item()
    predictions.append(predicted)

# Metrics
accuracy = accuracy_score(true_labels, predictions)
precision = precision_score(true_labels, predictions, average="weighted")
recall = recall_score(true_labels, predictions, average="weighted")
f1 = f1_score(true_labels, predictions, average="weighted")

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# Confusion matrix
cm = confusion_matrix(true_labels, predictions)

plt.figure(figsize=(10,8))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Intent Classification Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.savefig("evaluation/confusion_matrix.png")
plt.show()