import torch
from transformers import pipeline 

# Load the pre-trained sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Define function for analyzing sentiment
def analyze_sentiment(text):   # Analyzes the sentiment of the given text and returns the sentiment label and score.
    result = sentiment_pipeline(text)[0]
    return result

#Sample texts for testing
sample_texts = [
    "I love this product! It works great and has changed my life for the better.",
    "This is the worst experience I've ever had. I'm very disappointed.",
    "The movie was okay, but it could have been better.",
    "I'm so happy with the service I received!",
    ""
    "This is absolutely terrible. I will never come back here again."
]

#Run sentiment analysis on each sentence
for text in sample_texts:
    sentiment_result = analyze_sentiment(text)
    print(f"Text: {text}")
    print(f"Sentiment: {sentiment_result['label']}, Score: {sentiment_result['score']:.2f}\n")
