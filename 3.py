import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('wordnet')

# Sample text
text = "The cats are chasing mice and playing with balls"

# Tokenization
tokens = word_tokenize(text)

# Initialize Porter Stemmer and WordNet Lemmatizer
porter_stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

# Perform Morphological Analysis
print("Token\t\tPorter Stemming\tWordNet Lemmatization")
print("-" * 50)
for token in tokens:
    porter_stem = porter_stemmer.stem(token)
    wordnet_lemma = wordnet_lemmatizer.lemmatize(token)
    print(f"{token}\t\t{porter_stem}\t\t\t{wordnet_lemma}")
