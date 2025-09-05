import re
import requests

# --- Assignment 1: Find if a string has only octal digits --- #
print("--- Assignment 1: Octal Check ---")
def is_octal(s):
    return re.fullmatch(r'[0-7]+', s) is not None

strings_to_check = ['789', '123', '0904']
for s in strings_to_check:
    print(f"'{s}' is octal: {is_octal(s)}")
print("-" * 30 + "\n")


# --- Assignment 2: Extract from emails --- #
print("--- Assignment 2: Email Parser ---")
emails = ["zuck@facebook.com", "sunder33@google.com", "jeff42@amazon.com"]
for email in emails:
    match = re.match(r'([\w.]+)@([\w.]+)\.([a-zA-Z]+)', email)
    if match:
        user_id, domain, suffix = match.groups()
        print(f"Email: {email} -> User: {user_id}, Domain: {domain}, Suffix: {suffix}")
print("-" * 30 + "\n")


# --- Assignment 3: Split an irregular sentence --- #
print("--- Assignment 3: Sentence Splitter ---")
sentence = "****a, very   very; irregular_sentence***"
words = re.split(r'\W+', sentence)
result = " ".join(word for word in words if word).capitalize()
print(f"Original: {sentence}")
print(f"Cleaned: {result}")
print("-" * 30 + "\n")


# --- Assignment 4: Clean up a tweet --- #
print("--- Assignment 4: Tweet Cleaner ---")
tweet = "'Good advice! RT @TheNextWeb: what I would do differently if I was learning to code today http://t.co/lbwej0px0d cc: @garybernhardt #stats'"
def clean_tweet(text):
    text = re.sub(r'RT|cc:|@\w+|#\w+|http\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return " ".join(text.split()).strip()

print(f"Original Tweet: {tweet}")
print(f"Cleaned Tweet: {clean_tweet(tweet)}")
print("-" * 30 + "\n")


# --- Assignment 5: Extract text from HTML --- #
print("--- Assignment 5: HTML Text Extractor ---")
url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
try:
    response = requests.get(url)
    html_text = response.text
    text_portions = [text.strip() for text in re.findall(r'>([^<]+)<', html_text) if text.strip()]
    print("Extracted Text Portions:", text_portions)
except Exception as e:
    print(f"Could not fetch URL: {e}")
print("-" * 30 + "\n")


# --- Assignment 6: Words that begin and end with the same character --- #
print("--- Assignment 6: Same Start/End Character Check ---")
word_list = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
matching_words = [word for word in word_list if re.match(r'^(\w).*\1$', word, re.I)]
print(f"Original list: {word_list}")
print(f"Matching words: {matching_words}")
print("-" * 30 + "\n")