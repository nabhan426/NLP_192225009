import nltk

# Sample text
text = "This is a sample sentence."

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Perform part-of-speech tagging
pos_tags = nltk.pos_tag(tokens)
print(pos_tags)
