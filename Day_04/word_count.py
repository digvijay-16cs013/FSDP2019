# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:47:28 2019

@author: Administrator
"""

file_name = input('Enter file name => ') + '.txt'

def wc(f_name):
    
    # to store word freq
    word_freq = {}
    
    # to store unique words
    unique_words = []
    
    # open file in read mode
    with open('code_files/' + f_name) as fp:
        
        # read all the lines
        no_of_lines = len(fp.readlines())
        
        # to set cursor to start of file
        fp.seek(0, 0)
        
        # to get list of all words
        words = fp.read().replace('\n', ' ').split()
        
        # to get no of words
        no_of_words = len(words)
        
        # to set cursor to start of file
        fp.seek(0, 0)
        
        # get all the letters
        letters = list(fp.read().replace('\n', ''))
        
        # total no of characters
        no_of_letters = len(letters)
        
        # get individual word
        for word in words:
            
            # if word comes first time
            if word not in word_freq:
                
                # set word frequency to 1
                word_freq[word] = 1
            
            # if word has already come before
            else:
                
                # increment frequency by 1
                word_freq[word] += 1
        
        # find unique words 
        for word, count in word_freq.items():
             
            # count 1 specifies unique value
            if count == 1:
                
                # add unique word to list
                unique_words.append(word)
                
        # no of unique words 
        no_unique_words = len(unique_words)
                
        return no_of_letters, no_of_words, no_of_lines, no_unique_words
                
                
             
letters, words, lines, unique_words = wc(file_name)  
     
print('Letters : {}\nWords : {}\nLines : {}\nUnique Words : {}'.format(letters, words, lines, unique_words))
