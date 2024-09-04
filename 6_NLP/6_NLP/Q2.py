from nltk.tokenize import WordPunctTokenizer

text = "Reset your password if you just can't remember your old one."
result = WordPunctTokenizer().tokenize(text)
print(result)