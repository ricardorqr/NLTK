This is a Sentiment Analysis project using the library NLTK in Python.

### Contents

1. [NLTK](#NLTK)
1. [Pipeline](#pipeline)
    1. [Data Cleaning](#Data-Cleaning)
    1. [Vectorization](#Vectorization)
    1. [Perform Classification](#Perform-Classification)
1. [Libraries](#libraries)
    1. [Scikit-learn](#scikit-learn)
    1. [NLTK](#nltk)
    1. [NLTK Data](#nltk-data)
    1. [NLTK Stopwords Corpus](#nltk-stopwords-corpus)
    1. [NLTK WordNet](#nltk-wordnet)
    
# NLTK

Natural Language Processing, or NLP for shot, is broadly defined as the automatic manipulation of natural language, like speech and text by software.
In addition, Natural Language Toolkit (NLTK) is a leading platform for building Python programs to work with human language data.

# Pipeline

A pipeline is just a way to design a program where the output of one step is the input of the next step.

1. Text Document (begin)
1. [Data Cleaning](#Data-Cleaning)
1. [Vectorization](#Vectorization)
1. [Perform Classification (end)](#Perform-Classification)

## Data Cleaning

Convert the raw text into a list of words that are clean text (this is a very important step).

1. Data Cleaning (pre-processing)
    1. Convert to Lower Case
    1. Tokenization
    1. Remove Punctuation and Special Characters
    1. Stopwords Removal
    1. Stemming
    1. Lemmatization

- Tokenization - Convert a sentence into a single words.
- Stopwords Removal - Remove words which are present in the sentence and make no difference to the analysis.
- Stemming - Reduce the word to the base form. Ex.: Reading -> read.
- Lemmatization - Process of grouping together the different inflected forms of a word then they can be analysed as a single item.

## Vectorization

Convert words into numbers.

## Perform Classification

Process of assigning tags or categories to the text according to its content.

# Libraries

## scikit-learn

Run the Python interpreter and type the command:

`% pip install scikit-learn`

Source: https://scikit-learn.org/stable/index.html

## NLTK

Run the Python interpreter and type the command:

`% pip install nltk`

Source: https://scikit-learn.org/stable/index.html

## NLTK Data

To install the data, first install [NLTK](#nltk), then follow the instructions below.

Run the Python interpreter and type the commands:

```
>>> import nltk
>>> nltk.download()
```

A new window should open, showing the NLTK Downloader. Click on the File menu and select Change Download Directory. For central installation, set this to:

- `C:\nltk_data` (Windows)
- `/usr/local/share/nltk_data` (Mac)
- `/usr/share/nltk_data` (Unix)

Next, go to the tab _**All Pakages**_ select the packages **_punky_**, and press the buttons **_Download_**. Leave like
the picture below.

![Data](/resources/01.png)

Source: https://www.nltk.org/data.html

## NLTK Stopwords Corpus

The steps to download the **_stopwords_** data is similar then [NLTK](#nltk). Follow the instructions below.

Go to the tab _**All Pakages**_ select the packages **_stopwords_**, and press the buttons **_Download_**. Leave like
the picture below.

![Stopwords](/resources/02.png)

## NLTK WordNet

The steps to download the **_wordnet_** data is similar then [NLTK](#nltk). Follow the instructions below.

Go to the tab _**All Pakages**_ select the packages **_wordnet_**, and press the buttons **_Download_**. Leave like the
picture below.

![WordNet](/resources/03.png)
