This is a Sentiment Analysis project using the library NLTK in Python.

### Contents

1. [NLTK](#nlp)
1. [Pipeline](#pipeline)
   1. [Data Cleaning](#Data-Cleaning)
   1. [Perform Analysis](#Perform-Analysis)
1. [Libraries](#libraries)
   1. [Matplotlib](#matplotlib)
   1. [Scikit-learn](#scikit-learn)
   1. [NLTK](#nltk)
   1. [NLTK Data](#nltk-data)
   1. [NLTK Stopwords Corpus](#nltk-stopwords-corpus)
   1. [NLTK WordNet](#nltk-wordnet)
   1. [NLTK WordNet](#nltk-wordnet)
    
# NLP

Natural Language Processing, or NLP for shot, is broadly defined as the automatic manipulation of natural language, like speech and text by software.

# Pipeline

A pipeline is just a way to design a program where the output of one step is the input of the next step.

1. Text Document
1. [Data Cleaning](#Data-Cleaning)
1. [Perform Analysis] (#Perform-Analysis)

## Data Cleaning

Convert the raw text into a list of words that are clean text (this is a very important step).

1. Data Cleaning (pre-processing)
   
   1. Convert to Lower Case
   1. Remove Punctuation and Special Characters
   1. Tokenization
   1. Remove empty line
   1. Stopwords Removal
   1. Lemmatization
    
Some definitions:

- Tokenization - Convert a sentence into a single words.
- Stopwords Removal - Remove words which are present in the sentence and make no difference to the analysis.
- Stemming - Reduce the word to the base form. Ex.: Reading -> read.
- Lemmatization - Process of grouping together the different inflected forms of a word then they can be analysed as a single item.
   - Lemmatization runs 2 times with different parameters. That happens in order to clean words that were not clean the first time.  

## Vectorization

Convert words into numbers.

## Perform Analysis

Plot the analysis. The result should be like the picture below.

![Result](/resources/04.png)

# Libraries

## Matplotlib

Run the Python interpreter and type the command:

`% pip install matplotlib`

Source: https://matplotlib.org/stable/users/installing.html

## scikit-learn

Run the Python interpreter and type the command:

`% pip install scikit-learn`

Source: https://scikit-learn.org/stable/index.html

## NLTK

Natural Language Toolkit (NLTK) is a leading platform for building Python programs to work with human language data.

Run the Python interpreter and type the command:

`% pip install nltk`

Source: https://www.nltk.org/install.html

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