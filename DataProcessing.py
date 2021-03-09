from sklearn.datasets import fetch_20newsgroups
from nltk.tokenize import sent_tokenize, word_tokenize

text_data = fetch_20newsgroups()
raw_text = text_data.data[:4]
print(raw_text)

# Convert to lower case
clean_text_1 = []


def to_lower_case():
    for words in raw_text:
        clean_text_1.append(str.lower(words))


to_lower_case()
print(clean_text_1)

# Tokenize
import nltk
nltk.downloader('punkt')
sent_tok = []

for sent in clean_text_1:
    sent = sent_tokenize(sent)
    sent_tok.append(sent)

print(sent_tok)

