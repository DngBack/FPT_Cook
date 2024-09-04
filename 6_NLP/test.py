import nltk
dir(nltk.corpus)

text = """
NLTK, the Natural Language Toolkit, is a suite of program
modules, data sets and tutorials supporting research and teaching in
computational linguistics and natural language processing.
"""

# split by line
tokens = nltk.LineTokenizer().tokenize(text)

# split by whitespace
tokens = nltk.WhitespaceTokenizer().tokenize(text)

tokens = nltk.WordPunctTokenizer().tokenize(text)

print(tokens)