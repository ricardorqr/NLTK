# NLTK

Project using NLTK ()

This is a Sentiment Analysis project using the module NLTK in Python.

## Table of Contents
1. [Purpose](#purpose)
1. [Setup](#setup) 
	1. [scikit-learn](#scikit-learn)
	1. [NLTK](#nltk)
	1. [NLTK Data](#nltk data)
	1. [Finances](#finance-permissions)
	1. [Users](#users-permissions)
1. [Roles](#roles)

## Setup

# scikit-learn
```% pip install -U scikit-learn```

Source: https://scikit-learn.org/stable/index.html

# NLTK
```% pip install --user -U nltk```

Source: https://scikit-learn.org/stable/index.html

# NLTK Data

To install the data, first install NLTK, then use NLTK’s data downloader as described below. 

Run the Python interpreter and type the commands:

```
>>> import nltk
>>> nltk.download()
```

A new window should open, showing the NLTK Downloader. Click on the File menu and select Change Download Directory. For central installation, set this to:

- ```C:\nltk_data``` (Windows)
- ```/usr/local/share/nltk_data``` (Mac) 
- ```or /usr/share/nltk_data``` (Unix)

Next, select the packages or collections you want to download. Leave like the picture below.

![LyricFind](/resources/01.png)

If you did not install the data to one of the above central locations, you will need to set the NLTK_DATA environment variable to specify the location of the data. (On a Windows machine, right click on “My Computer” then select Properties > Advanced > Environment Variables > User Variables > New...)

Test that the data has been installed as follows. (This assumes you downloaded the Brown Corpus):A new window should open, showing the NLTK Downloader. Click on the File menu and select Change Download Directory. For central installation, set this to C:\nltk_data (Windows), /usr/local/share/nltk_data (Mac), or /usr/share/nltk_data (Unix). Next, select the packages or collections you want to download.

If you did not install the data to one of the above central locations, you will need to set the NLTK_DATA environment variable to specify the location of the data. (On a Windows machine, right click on “My Computer” then select Properties > Advanced > Environment Variables > User Variables > New...)

Test that the data has been installed as follows. (This assumes you downloaded the Brown Corpus):

Source: https://scikit-learn.org/stable/index.html

