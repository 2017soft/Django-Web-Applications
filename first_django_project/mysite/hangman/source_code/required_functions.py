from django.db import models

# Create your models here.

import random
import string

WORDLIST_FILENAME = "words.txt"

guesses_remaining = 6
warnings_remaining = 3
complete_guess_score = 1
failure = False
available_letters = string.ascii_lowercase
letters_guessed = []


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist

'''

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
'''

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
# wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for x in secret_word:
        if x not in letters_guessed:
            return False
    return True
            
        
        



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_so_far = ''
    for x in secret_word:
        if x in letters_guessed:
            word_so_far += x
        else:
            word_so_far += '_ '
    return word_so_far



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_possible_letters = string.ascii_lowercase
    list_so_far = ''
    for x in all_possible_letters:
        if x not in letters_guessed:
            list_so_far += x
    return list_so_far


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
            
    myWord = my_word.replace(' ', '')
    if len(myWord) != len(other_word):
        return False
    else:
        for i in range(len(other_word)):
            if myWord[i] != other_word[i]:
                if myWord[i] != '_':
                    return False
                elif other_word[i] in myWord:
                    return False
        return True

                
                


'''
def show_possible_matches(my_word):

    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    
    
    index = 0
    for x in wordlist:
        if match_with_gaps(my_word, x):
            print(x)
            index += 1

    if index == 0:
        print('No matches found')
'''