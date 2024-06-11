import re

# Define regular expression patterns for POS tagging
patterns = [
    (r'\b(\w+ing)\b', 'VBG'),  # Gerunds
    (r'\b(\w+ed)\b', 'VBD'),   # Past tense verbs
    # Add more patterns for other POS tags
]

# Test text
text = "I am running and jumping."

# Apply the patterns to tag words
for pattern, tag in patterns:
    text = re.sub(pattern, tag, text)

print(text)
