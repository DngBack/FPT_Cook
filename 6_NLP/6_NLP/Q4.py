def percent_containing_string(words, substring):
    word_list = words.split()
    counter = 0
    for word in word_list:
        if substring in word:
            counter += 1
            
    return counter / len(word_list) * 100

print(percent_containing_string('xin chao viet nam, chao cac ban', 'ao'))