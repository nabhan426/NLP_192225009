# You would typically train your model on a tagged corpus to calculate transition probabilities.
# For simplicity, we'll just use NLTK's pre-trained POS tagger for tagging.

import nltk

# Sample text
text = "This is a sample sentence."

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Perform part-of-speech tagging
pos_tags = nltk.pos_tag(tokens)
print(pos_tags)
