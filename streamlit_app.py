import streamlit as st
from emotion_model.text_emotion import detect_emotion
from playlist.spotify_recommender import get_playlists_for_emotion

st.set_page_config(page_title="MoodMuse", layout="centered")

# Title and description
st.title("🎧 MoodMuse")
st.subheader("Emotion-Based Playlist Recommender")
st.markdown("Describe how you're feeling, and get music that matches your vibe!")

# Input from user
user_input = st.text_input("How are you feeling today?", placeholder="e.g. I'm feeling happy or tired...")

# On input
if user_input:
    emotion, score = detect_emotion(user_input)
    st.success(f"Emotion Detected: **{emotion.capitalize()}** (Confidence: {score:.2f})")

    playlists = get_playlists_for_emotion(emotion)
    
    if playlists:
        st.markdown("### 🎶 Playlist Recommendations:")
        for playlist in playlists:
            st.markdown(f"- [{playlist['name']}]({playlist['url']})")
    else:
        st.warning("No playlists found for this mood. Try another emotion.")
