import random

# Example corpus
corpus = "I love eating pizza. Pizza is delicious. Pizza makes me happy."

# Tokenize the corpus
tokens = corpus.split()

# Generate bigrams
bigrams = [(tokens[i], tokens[i+1]) for i in range(len(tokens)-1)]

# Function to generate text using bigram model
def generate_text(bigrams, length=10):
    text = []
    for _ in range(length):
        next_word = random.choice([bigram[1] for bigram in bigrams if bigram[0] == text[-1]])
        text.append(next_word)
    return ' '.join(text)

# Generate text using bigram model
generated_text = generate_text(bigrams)
print(generated_text)
