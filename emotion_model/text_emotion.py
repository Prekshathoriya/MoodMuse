# emotion_model/text_emotion.py

from transformers import pipeline

# Load emotion detection model
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)

def detect_emotion(text):
    result = emotion_classifier(text)[0]
    label = result['label']
    score = result['score']
    return label, score

# For testing
if __name__ == "__main__":
    test_text = "I feel so lonely and sad."
    emotion, confidence = detect_emotion(test_text)
    print(f"Detected Emotion: {emotion} (Confidence: {confidence:.2f})")
