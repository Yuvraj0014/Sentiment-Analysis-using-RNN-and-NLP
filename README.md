# 🎬 IMDB Movie Review Sentiment Analysis 🍿

## 📝 Project Overview
This is a Streamlit-based web application that uses a pre-trained deep learning model to analyze the sentiment of movie reviews. The application classifies movie reviews as either Positive or Negative using a machine learning model trained on the IMDB dataset.

## 🛠️ Requirements
- Python 3.8+ 🐍
- Streamlit
- TensorFlow
- NumPy
- Pillow (PIL)

## 💾 Installation

1. Clone the repository:
```bash
git clone https://your-repository-url.git
cd movie-sentiment-analysis
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Ensure you have the pre-trained model file `simple_rnn_imdb.h5` in the project directory.

## 🚀 Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

## 🔍 How to Use the Application
1. Open the web application in your browser 💻
2. Navigate to the sidebar 👉
3. Enter a movie review in the text area ✍️
4. Click "Classify Sentiment" button 🏁
5. View the sentiment prediction and score 📊

## 📈 Output Prediction
- **Positive Sentiment** 😄: Prediction score > 0.6
- **Negative Sentiment** 😞: Prediction score ≤ 0.6
- Displays sentiment label and confidence score

## 🖥️ Application Interface
- Centered layout with a cinema-themed design 🎥
- Sidebar for review input and sentiment analysis 📋
- Color-coded sentiment display 🌈
- Informative tips and instructions 💡

## 📌 Note
Ensure you have the pre-trained model (`simple_rnn_imdb.h5`) in the same directory before running the application. 🔍
