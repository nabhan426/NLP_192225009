# Define transformation rules
rules = [
    (r'\b(\w+ing)\b', 'VBG'),  # Gerunds
    (r'\b(\w+ed)\b', 'VBD'),   # Past tense verbs
    # Add more rules for other POS tags
]

# Test text
text = "I am running and jumping."

# Apply the rules to tag words
for pattern, tag in rules:
    text = re.sub(pattern, tag, text)

print(text)
