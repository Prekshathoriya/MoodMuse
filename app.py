# app.py

from emotion_model.text_emotion import detect_emotion
from playlist.spotify_recommender import get_playlists_for_emotion

def main():
    print("🎧 Welcome to MoodMuse 🎵")
    user_input = input("How are you feeling today? (Type a sentence): ")

    emotion, confidence = detect_emotion(user_input)
    print(f"\n🧠 Detected Emotion: {emotion} (Confidence: {confidence:.2f})")

    print("\n🎶 Recommended Playlists for your mood:\n")
    playlists = get_playlists_for_emotion(emotion)

    if playlists:
        for p in playlists:
            print(f"• {p['name']} ➤ {p['url']}")
    else:
        print("No playlists found. Try another emotion!")

if __name__ == "__main__":
    main()
