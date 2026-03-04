from jiwer import wer

reference = "cancel my order"
prediction = "cancel my order"

error = wer(reference, prediction)

print("WER:", error)