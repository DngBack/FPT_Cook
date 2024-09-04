import nltk

def most_common_starting_char(text):
    result_dict = {}
    word_list = nltk.word_tokenize(text)
    for word in word_list:
        if len(word) != 0 and word[0].isalpha:
            if word[0] not in result_dict:
                result_dict[word[0]] = 1
            else:
                result_dict[word[0]] += 1
    
    new_dict = sorted(result_dict, key=lambda x:result_dict[x])
    return new_dict[-1]
    

print(most_common_starting_char('xin chao viet nam, chao cac ban'))