import json

with open("data/words_dictionary.json") as myfile:
    dict = json.load(myfile)

words = list(dict.keys())[:10000]


with open('data/corncob_lowercase.txt') as myfile2:
    words = [x.strip('\r\n') for x in myfile2.readlines()]



def center_leter_input():
    return input('Please enter the key letter : ')

def other_letters_input():
    letter_lst = input('Please enter all other letter : ')
    return [x for x in letter_lst]
    



#### now we trim the list of works to make sure they have the key letter


def check_key_letter(key_letter,words):
    '''This function will trim the full list of words for key letter'''
    return [x for x in words if key_letter in x]


## some panogram checks

def count_tgt_letters_in_word(tgt_letters, word):
    
    count = 0 

    for letter in tgt_letters:
        if letter in word:
            count += 1
        else:
            pass
    
    return count

letters = ['a', 'f', 'i', 'n','p', 't','l']


def check_panogram(word, letters):
    
    is_pano = False

    if count_tgt_letters_in_word(letters, word) == 7:        
       
        if check_word(word, letters):
            is_pano = True

    return is_pano


## now we go through the full list

def check_word(word,letters):
    word_lst = [x.lower() for x in word]

    # check the letters in the word are in the list
    return all(elem in letters  for elem in word_lst)

def check_all_words(word_lst, key_letter, letters):
    
    # filter for key letter
    shorter_lst = check_key_letter(key_letter, word_lst)

    panograms = []
    words_to_play = []

    for word in shorter_lst:
        
        if len(word) < 4:
            pass

        # panograms
        elif check_panogram(word, letters):
            panograms.append(word)
        
        # all other words
        elif check_word(word, letters):
            words_to_play.append(word)

        else:
            pass

    return panograms, words_to_play


## lets play the game

## user enters the letters
key_letter = center_leter_input()
other_letters = other_letters_input()

## some quick list manipulation
all_letters = []
all_letters.extend(other_letters)
all_letters.append(key_letter)
all_letters = list(set(all_letters))

## lets see some answers
print(check_all_words(words, key_letter, all_letters))



