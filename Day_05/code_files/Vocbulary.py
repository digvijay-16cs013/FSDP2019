# -*- coding: utf-8 -*-
"""
Created on Sun May 12 17:11:09 2019

@author: Administrator
"""
# to get regular expression module
import re

# each set will contain words of different files
list_of_sets = []

# list of novels
novels = ['sons_and_lovers_lawrence.txt','metamorphosis_kafka.txt','the_way_of_all_flash_butler.txt','robinson_crusoe_defoe.txt','to_the_lighthouse_woolf.txt','james_joyce_ulysses.txt','moby_dick_melville.txt']

# count unique words, total words and different words
def word_count(file_name):
    
    # to store word ocurrance in file
    word_freq = {}

    # to store unique words
    unique_words = []
    
    # open file in read mode
    with open(file_name, 'r', encoding = 'utf8') as fp:
        
        # to read individual line
        line = fp.readline()
        
        # to read the file until EOF is encountered
        while line:
            
            # get all the matches
            words = re.findall(r'[a-zA-Z]+', line.rstrip('\n'))
            
            # to get the word frequency
            if words:
                for word in words:
                    if word not in word_freq:
                        word_freq[word] = 1
                    else:
                        word_freq[word] += 1
                        
            line = fp.readline()
            
        # to get unique words from file
        for word, count in word_freq.items():
            if count == 1:
                unique_words.append(word)
            
        # to get the total words
        print('\n{} :- \nTotal Words :'.format(file_name), sum(word_freq.values()))
    
        # to get the number of different words
        print('Different words :', len(set(word_freq.keys())))
        
        # to get the number of unique words
        print('Unique Words :', len(unique_words))

        # returns set of words of file
        return set(word_freq.keys())
        
# to get word count of each novel
for novel in novels:
        list_of_sets.append(word_count(novel))
        
# to insert set of words of ulysses at the beginning to get the difference
list_of_sets.insert(0, list_of_sets.pop(5))

#storing words in a file which are only in ulysses and not in others
with open('ulysses.txt', 'w') as fp:
    
    # to get list of words which are only in ulysses file and not in others
    words = list(list_of_sets[0].difference(list_of_sets[1], list_of_sets[2], list_of_sets[3], list_of_sets[4], list_of_sets[5], list_of_sets[6]))
    
    # to write individual word
    for word in words:
        fp.write(word + '\n')
        
# to get the common words
print('Common words :', len(list_of_sets[0].intersection(list_of_sets[1], list_of_sets[2], list_of_sets[3], list_of_sets[4], list_of_sets[5], list_of_sets[6])))        