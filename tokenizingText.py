#how to tokenize text into words using NLTK

import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')  # Download tokenizer models

# Sample text
text = "Hello there! How are you doing today?"

# Tokenize into words
tokens = word_tokenize(text)
print("Word Tokens:", tokens)
