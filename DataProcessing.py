from sklearn.datasets import fetch_20newsgroups
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import re

text_data = fetch_20newsgroups()
raw_text = text_data.data[:4]
# print(raw_text)

# Convert to lower case
clean_text_1 = []
for words in raw_text:
    clean_text_1.append(str.lower(words))
# print(clean_text_1)

# Tokenize
sent_tok = []
for sent in clean_text_1:
    sent = sent_tokenize(sent)
    sent_tok.append(sent)
# print(sent_tok)


# Word tokenize
clean_text_2 = [word_tokenize(i) for i in clean_text_1]
# print(clean_text_2)

clean_text_3 = []
for words in clean_text_2:
    clean = []
    for w in words:
        res = re.sub(r'[^\w\s]', "", w)
        if res != "":
            clean.append(res)
        clean_text_3.append(clean)
# print(clean_text_3)


# Stop word removal
clean_text_4 = []
for words in clean_text_3:
    w = []
    for word in words:
        if not word in stopwords.words('english'):
            w.append(word)
        clean_text_4.append(w)
# print(clean_text_4)


# Stemming (example 1)
clean_text_5 = []
port = PorterStemmer()
for words in clean_text_4:
    w = []
    for word in words:
        w.append(port.stem(word))
    clean_text_5.append(w)
# print(clean_text_5)


# Lemmatize (example 2)
wnet = WordNetLemmatizer()
lem = []
for words in clean_text_4:
    w = []
    for word in words:
        w.append(wnet.lemmatize(word))
    lem.append(w)
# print(lem)


print(clean_text_5[:1])
print(lem[:1])
