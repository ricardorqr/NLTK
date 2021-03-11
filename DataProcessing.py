import string
from collections import Counter
from collections import defaultdict

import matplotlib.pyplot as plt
import nltk
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Get the text
with open('resources/Steve Jobs Speech.txt', 'r') as file:
    text_data = file.readlines()
# print(text_data)

# Convert to lower case
clean_text_1 = []
for line in text_data:
    clean_text_1.append(str.lower(line))
# print(clean_text_1)

# Remove punctuation and special characters
clean_text_2 = []
for line in clean_text_1:
    clean_text_2.append(line.translate(str.maketrans('', '', string.punctuation)))
# print(clean_text_2)

# Tokenize
clean_text_3 = []
for line in clean_text_2:
    token = word_tokenize(line, 'english')
    clean_text_3.append(token)
# print(clean_text_3)

# Remove empty line
clean_text_4 = list(filter(None, clean_text_3))
# print(clean_text_4)

# Stopwords removal
clean_text_5 = []
for line in clean_text_4:
    clean_word = []

    for word in line:
        if word not in stopwords.words('english'):
            clean_word.append(word)
    clean_text_5.append(clean_word)
# print(clean_text_5[:10])


def get_wordnet_pos(word_to_tag):
    tag_word = nltk.pos_tag([word_to_tag])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag_word, wordnet.NOUN)


# Lemmatize (example 1)
clean_text_6 = []
lemmatizer = WordNetLemmatizer()
tag_map = defaultdict(lambda: wordnet.NOUN)
tag_map['J'] = wordnet.ADJ
tag_map['V'] = wordnet.VERB
tag_map['R'] = wordnet.ADV
for line in clean_text_5:
    clean_word = []

    for word in line:
        clean_word.append(lemmatizer.lemmatize(word, get_wordnet_pos(word)))
    clean_text_6.append(clean_word)
# print(clean_text_6[:10])

# Lemmatize (example 2)
clean_text_7 = []
for line in clean_text_6:
    clean_word = []

    for token, tag in pos_tag(line):
        clean_word.append(lemmatizer.lemmatize(token, tag_map[tag[0]]))
    clean_text_7.append(clean_word)
# print(clean_text_7[:10])

# Create emotion list
emotion_list = []
with open('resources/emotions.txt', 'r') as file:
    for emotion_line in file:
        clear_line = emotion_line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        for line in clean_text_7:
            if word in line:
                emotion_list.append(emotion)
count = Counter(emotion_list)
print(count)

# Plot the analysis
fig, ax1 = plt.subplots()
ax1.bar(count.keys(), count.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
