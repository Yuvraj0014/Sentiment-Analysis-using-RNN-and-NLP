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
model = load_model('C:/Users/yuvra/OneDrive/Desktop/Self Projects/SELF/IMDB simple RNN/simple_rnn_imdb.h5')

# Function to decode reviwes
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i-3, '?') for i in encoded_review])
# Function to preprocess user inputs
def preprocess_text(text):
    words=text.lower().split()
    encoded_review=[word_index.get(word, 2)+3 for word in words] 
    padded_review=sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

# Streamlit app
st.title("IMDB movie review Sentiment Analysis")
st.write("The model will classify the given review as Positive or Negative")

# USer Input 
user_input=st.text_area("Movie Review")

if st.button('classify'):
    preprocessed_input=preprocess_text(user_input)

    # Make prediction
    prediction=model.predict(preprocessed_input)
    sentiment='positive' if prediction[0][0]>0.6 else "Negative"

    # Display result
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Prediction Score: {prediction[0][0]}')
else:
    st.write('please enter a movie review')