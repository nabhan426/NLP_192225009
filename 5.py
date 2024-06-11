import nltk
from nltk.stem import PorterStemmer

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# List of words to stem
words = ['running', 'plays', 'jumps', 'happier', 'largest']

# Perform stemming on each word
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)
