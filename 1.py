import re

# Sample text
text = """
Hello, my name is John Doe. My email is john.doe@example.com.
You can also contact my friend Jane at jane_doe123@sample.net.
Visit us at https://www.example.org or call us at (123) 456-7890.
"""

# 1. Matching email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)
print("Email addresses found:", emails)

# 2. Matching URLs
url_pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
urls = re.findall(url_pattern, text)
print("URLs found:", urls)

# 3. Matching phone numbers (format: (123) 456-7890)
phone_pattern = r'\(\d{3}\) \d{3}-\d{4}'
phones = re.findall(phone_pattern, text)
print("Phone numbers found:", phones)

# 4. Matching names (assuming names are capitalized words)
name_pattern = r'\b[A-Z][a-z]*\b'
names = re.findall(name_pattern, text)
print("Names found:", names)

# 5. Searching for a specific word
search_word = "John"
search_pattern = rf'\b{search_word}\b'
search_result = re.search(search_pattern, text)
if search_result:
    print(f"'{search_word}' found at position:", search_result.start())
else:
    print(f"'{search_word}' not found")

# 6. Splitting text by a pattern (e.g., split by sentences)
sentence_pattern = r'[.!?]\s+'
sentences = re.split(sentence_pattern, text)
print("Sentences:", sentences)

# 7. Replacing patterns (e.g., replace emails with a placeholder)
replaced_text = re.sub(email_pattern, '[EMAIL]', text)
print("Text with emails replaced:", replaced_text)
