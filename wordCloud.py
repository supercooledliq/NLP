# generating a word cloud from a given text input related to Natural Language Processing (NLP).
# It uses the NLTK library for text processing and the WordCloud library for visualization.

import nltk
import re  # Regular expressions for cleaning text
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#import string

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Sample text input
text = """
Natural Language Processing (NLP) is a sub-field of artificial intelligence that enables computers to understand, interpret, and generate human language. 
It combines computational linguistics with statistical and machine learning models.
"""

# Step 1: Tokenization
tokens = word_tokenize(text)

# Step 2: Convert to lower case and remove punctuation
tokens = [word.lower() for word in tokens if word.isalpha()]

# Step 3: Remove stopwords (commonly used words like "the", "is", "and")
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]

# Step 4: Join words back into a single string for WordCloud
processed_text = ' '.join(filtered_tokens)

# Step 5: Create Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(processed_text)

# Step 6: Display Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axis
plt.title('Word Cloud from NLP Text', fontsize=16)
plt.show()
