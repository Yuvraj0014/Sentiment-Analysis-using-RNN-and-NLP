import streamlit as st
from PIL import Image
#Importing libraries
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import  sequence
from tensorflow.keras.models import load_model

# Load the IMDB dataset word index
word_index = imdb.get_word_index()
reverse_word_index={value: key for key, value in word_index.items()}

# Load the pre-trained model with ReLU activation 
model = load_model('simple_rnn_imdb.h5')

# Function to decode reviwes
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i-3, '?') for i in encoded_review])
# Function to preprocess user inputs
def preprocess_text(text):
    words=text.lower().split()
    encoded_review=[word_index.get(word, 2)+3 for word in words] 
    padded_review=sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

# App Title and Styling
st.set_page_config(page_title="IMDB Sentiment Analysis", page_icon="🎬", layout="centered")
st.markdown("<h1 style='text-align: center; color: #FF6347;'>IMDB Movie Review Sentiment Analysis 🎥</h1>", unsafe_allow_html=True)
st.write("**Analyze the sentiment of movie reviews as Positive or Negative!**")

# Display an image (optional, can be an IMDB logo or cinema-related image)
#image = Image.open("movie_poster.jpg")  # Ensure you have an image file with this name in the same folder
#st.image(image, caption="Sentiment Analysis on Movie Reviews", use_column_width=True)

# Sidebar for User Input
st.sidebar.header("Movie Review Sentiment Analyzer")
st.sidebar.write("Input a movie review to classify its sentiment.")
user_input = st.sidebar.text_area("Enter Movie Review:", placeholder="Type your review here...")

# Sidebar button to trigger prediction
if st.sidebar.button("Classify Sentiment"):
    with st.spinner("Analyzing... Please wait"):
        preprocessed_input = preprocess_text(user_input)  # Preprocess function
        prediction = model.predict(preprocessed_input)  # Model prediction

        # Display Result with Color Coding
        sentiment = 'Positive' if prediction[0][0] > 0.6 else 'Negative'
        st.sidebar.markdown(
            f"<h2 style='color: #1E90FF;'>Sentiment: {sentiment}</h2>", unsafe_allow_html=True
        )
        st.sidebar.write(f"**Prediction Score:** {prediction[0][0]:.2f}")
else:
    st.sidebar.write("Awaiting your review...")

# Additional UI Elements for User Experience
st.sidebar.info("Tip: Enter descriptive reviews for better results!")
st.markdown("<hr>", unsafe_allow_html=True)
