import nltk
#form cau 1____________________________(chapter1 )
# text = '''
# Joe waited for the train. The train was late. 
# Mary and Samantha took the bus. 
# I looked for Mary and Samanthasize at the bus size.
# '''
# from nltk.tokenize import word_tokenize
# from nltk.tokenize import sent_tokenize
# text1 = word_tokenize(text)
# a = [[w for w in text1 if 'pt' in w]] (dòng này chỉnh theo ycau đề bài )
# print(a)



# Dạng đề 2 ( có trong các chapter ex, chap 1-2 ko có thì đen)
# from nltk.book  import *
# from nltk.corpus import brown
# from nltk.corpus import stopwords # list of stopwords

# wordSet = []                              # create an empty list
# # frequency distribution for words in Brown Corpus
# fdist = nltk.FreqDist(w for w in set(brown.words()) if w.isalpha())
# # iterate over the samples
# for sample in fdist:
#     if fdist[sample] >=3:
#         wordSet.append(sample)   
# print(wordSet == atleast_3times)        


#de 2 cau lexicon 
# lexicon = {
#     'word1': {'meaning': 'definition1', 'pronunciation': 'pronunciation1'},
#     'word2': {'meaning': 'definition2', 'pronunciation': 'pronunciation2'},
#     'word3': {'meaning': 'definition3', 'pronunciation': 'pronunciation3'},
#     # Thêm các từ khác vào đây
# }

# def create_index(lexicon, property_name):
#     """
#     Tạo chỉ mục cho từ điển dựa trên một thuộc tính cụ thể.

#     Parameters:
#         lexicon (dict): Từ điển chứa thông tin về từ vựng.
#         property_name (str): Tên thuộc tính cần tra cứu (ví dụ: 'meaning', 'pronunciation').

#     Returns:
#         dict: Chỉ mục cho từ điển dựa trên thuộc tính cụ thể.
#     """
#     index = {}
#     for word, properties in lexicon.items():
#         property_value = properties.get(property_name, '')
#         if property_value not in index:
#             index[property_value] = [word]
#         else:
#             index[property_value].append(word)
#     return index

# Tạo chỉ mục cho ý nghĩa
# meaning_index = create_index(lexicon, 'meaning')

# In ra chỉ mục cho ý nghĩa
# print("Index based on meanings:")
# for meaning, words in meaning_index.items():
#     print(f"{meaning}: {', '.join(words)}")

# Tạo chỉ mục cho cách phát âm
# pronunciation_index = create_index(lexicon, 'pronunciation')

# In ra chỉ mục cho cách phát âm
# print("\nIndex based on pronunciations:")
# for pronunciation, words in pronunciation_index.items():
#     print(f"{pronunciation}: {', '.join(words)}")






# text = '''               
# Joe waited for the train. The train was late. 
# Mary and Samantha took the bus. 
# I looked for Mary and Samanthasize at the bus size.
# '''

# most_freq_50_fd=nltk.FreqDist(brown.words(categories='news'))
# #fd that includes stop words
# print(most_freq_50_fd.most_common(50))
# words=[word for word in most_freq_50_fd]
# for word in words:
#     if word in stopwords.words('english') or not word.isalpha():
#         most_freq_50_fd.pop(word)
# #fd that excludes stop words
# print(most_freq_50_fd.most_common(50))

#dang de cau 3___________________________________

#dang 3 tach theo nhieu cau 


# text = '''               
# Joe waited for the train. The train was late. 
# Mary and Samantha took the bus. 
# I looked for Mary and Samanthasize at the bus size.
# '''
# from nltk.tokenize import WordPunctTokenizer
# from nltk.tokenize import sent_tokenize
# from nltk.tokenize import word_tokenize
# sent_tokenize(text)
# print([word_tokenize(t) for t in sent_tokenize(text)])



#dang 3 tach theo 1 cau 

# from nltk.tokenize import WordPunctTokenizer
# text = "Reset your password if you just can't remember your old one."
# print("\nOriginal string:")
# print(text)
# result = WordPunctTokenizer().tokenize(text)
# print("\nSplit all punctuation into separate tokens:")
# print(result)


#dang cau 4 

# similarity percentage __________________________________
# import spacy
# nlp=spacy.load("en_core_web_md")

# text1 = "John lives in Canada"
# text2 = "James lives in America, through he's not from there"
# doc1=nlp(text1)
# doc2=nlp(text2)
# s = doc1.similarity(doc2) 
# print(s)

# from nltk.corpus import wordnet
# list  = []
# text1 = "John lives in Canada"
# text2 = "James lives in America, through he's not from there"
# list1 = text1.split(" ")
# list2 = text2.split(" ")


# for word1 in list1:
#     for word2 in list2:
#         wordFromList1 = wordnet.synsets(word1)
#         wordFromList2 = wordnet.synsets(word2)
#         if wordFromList1 and wordFromList2: #Thanks to @alexis' note
#             s = wordFromList1[0].wup_similarity(wordFromList2[0])
#             list.append(s)
            
# s = 0
# for i in list:
#     s += i

# print(1- s/len(list))



#cau 4 dang mergeing ___________________________
# # Using retokenize() method of Doc object to merge two tokens
# import spacy
# nlp = spacy.load('en_core_web_md')

# text="Robert Langdon is a famous character in various books and movies "
# doc = nlp(text)
# with doc.retokenize() as retokenizer:
#     retokenizer.merge(doc[0:2]) ( thay so den chet)

# for token in doc:
#   print(token.text)




#dang verb phrase
#We import the PhraseMatcher
# import spacy
# from spacy.matcher import Matcher

# nlp_matcher = spacy.load("en_core_web_sm")

# matcher = Matcher(nlp_matcher.vocab)


# #We create our patterns as a list of dictionaries
# pattern = [
#     [{"POS": "AUX"}, {"POS": "VERB"}]
# ]

# pattern = [
#      [{"POS": "PRON"}]
# ]

# pattern = [
#      [{"POS": "NOUN"}]
# ]

# matcher.add("verb-phrases", pattern)
# text = ("I may bake a cake for my birthday. The talk will introduce reader about Useof baking")
# text=" My sister has a dog and she loves him"
# doc2 = nlp_matcher(text)
# matches = matcher(doc2)
# for match in matches:
#     #print (match)
#     span = doc2[match[1]:match[2]]
#     print (span)




