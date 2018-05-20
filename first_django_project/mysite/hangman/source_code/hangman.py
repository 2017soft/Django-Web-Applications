# Problem Set 2, hangman.py
# Name: Eric Luo
# Collaborators: MIT Assignment Instructions
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


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
    import string
    all_possible_letters = string.ascii_lowercase
    list_so_far = ''
    for x in all_possible_letters:
        if x not in letters_guessed:
            list_so_far += x
    return list_so_far

'''
def hangman(secret_word):
    
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.

    
    guesses_remaining = 6
    warnings_remaining = 3
    available_letters = string.ascii_lowercase
    letters_guessed = []
    answer = input('Welcome to the game Hangman! \n I am thinking of a word that is '
             + str(len(secret_word)) + ' letters long. \n You have ' 
             + str(warnings_remaining) + ' warnings left \n You have ' 
             + str(guesses_remaining) + ' guesses left. \n Available letters: ' 
             + string.ascii_lowercase + '. \n Please guess a letter: ')
    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        
        if answer not in string.ascii_lowercase:
            if warnings_remaining == 1:
                guesses_remaining -= 1
                warnings_remaining = 3
                answer = input('Oops! That is not a valid letter. \n You have'
                               + ' no warnins left \n so you lose one guess:'
                               + get_guessed_word(secret_word, letters_guessed) 
                               + ' \n You have' + str(guesses_remaining) + 
                               'guesses left. \n Available letters:' + 
                               str(available_letters) + ' \n Please guess a letter:')
            else: 
                warnings_remaining -= 1
                answer = input('Oops! That is not a valid letter. \n You have'
                               + str(warnings_remaining) + ' warnings left:'
                               + get_guessed_word(secret_word, letters_guessed) 
                               + ' \n You have ' + str(guesses_remaining) 
                               + ' guesses left. \n Available letters: ' 
                               + available_letters + ' \n Please guess a letter:')
        elif answer in letters_guessed:
            if warnings_remaining == 1: 
                guesses_remaining -= 1
                warnings_remaining = 3
                answer = input('Oops! You have already guessed that letter. \n You have'
                               + ' no warnins left \n so you lose one guess:'
                               + get_guessed_word(secret_word, letters_guessed) 
                               + ' \n You have' + str(guesses_remaining) + 
                               'guesses left. \n Available letters:' + 
                               str(available_letters) + ' \n Please guess a letter:')
            else: 
                warnings_remaining -= 1
                answer = input('Oops! You have already guessed that letter. \n You have'
                               + str(warnings_remaining) + ' warnings left:'
                               + get_guessed_word(secret_word, letters_guessed) 
                               + ' \n You have ' + str(guesses_remaining) 
                               + ' guesses left. \n Available letters: ' 
                               + available_letters + ' \n Please guess a letter:')
        elif answer in secret_word:
            letters_guessed.append(answer)
            available_letters = get_available_letters(letters_guessed)
            answer = input('Good guess: ' 
                           + get_guessed_word(secret_word, letters_guessed)
                           + ' \n You have' + str(guesses_remaining) 
                           + 'guesses left. \n Available letters:' 
                           + available_letters + ' \n Please guess a letter:')
        elif answer in 'aeiou':
            letters_guessed.append(answer)
            available_letters = get_available_letters(letters_guessed)
            guesses_remaining -= 2
            answer = input('Oops! That letter is not in my word:' 
                           + get_guessed_word(secret_word, letters_guessed)
                           + ' \n You have' + str(guesses_remaining) + 
                           'guesses left \n Available Letters:' 
                           + available_letters + ' \n Please guess a letter:')
        else:
            letters_guessed.append(answer)
            available_letters = get_available_letters(letters_guessed)
            guesses_remaining -= 1
            answer = input('Oops! That letter is not in my word:' 
                           + get_guessed_word(secret_word, letters_guessed)
                           + ' \n You have' + str(guesses_remaining) + 
                           'guesses left \n Available Letters:' 
                           + available_letters + ' \n Please guess a letter:')
    if guesses_remaining <= 0:
        print('Oops! That letter is not in my word:'
              + get_guessed_word(secret_word, letters_guessed)
              + ' \n Sorry, you ran out of guesses. The word was else.')
    else:
        print('Good guess:' + secret_word + 
              ' \n Congradulations, you won! \n Your total score for this game is:'
              + str(guesses_remaining * len(secret_word)))

'''
            
                
            
        
                
    
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



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

                
                



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    index = 0
    for x in wordlist:
        if match_with_gaps(my_word, x):
            print(x)
            index += 1
    if index == 0:
        print('No matches found')
    else:
        return
        
    
    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
   
    guesses_remaining = 6
    warnings_remaining = 3
    complete_guess_score = 1
    failure = False
    available_letters = string.ascii_lowercase
    letters_guessed = []
    answer = input('Welcome to the game Hangman! \n I am thinking of a word that is '
             + str(len(secret_word)) + ' letters long. \n You have ' 
             + str(warnings_remaining) + ' warnings left \n You have ' 
             + str(guesses_remaining) + ' guesses left. \n Available letters: ' 
             + string.ascii_lowercase + '. \n Please guess a letter: ')
    while True:
        
        if answer == 'quit':
            failure = True
            break
        elif answer == 'complete':
            final_answer = input('please enter your final answer: ')
            if final_answer == secret_word:
                complete_guess_score = 2
                break
            else:
                guesses_remaining -= 1
                if guesses_remaining <= 0:
                    break
                answer = input('Oops! That is not the correct word:' 
                           + get_guessed_word(secret_word, letters_guessed)
                           + ' \n You have ' + str(guesses_remaining) + 
                           ' guesses left \n Available Letters:' 
                           + available_letters + ' \n Please guess a letter:')
        elif answer == '*':
            print('Possible word matches are:')
            my_word = get_guessed_word(secret_word, letters_guessed)
            show_possible_matches(my_word)
            answer = input('You have ' + str(guesses_remaining) + 
                               ' guesses left. \n Available letters:' + 
                               str(available_letters) + ' \n Please guess a letter:')
        elif answer not in string.ascii_lowercase:
            if warnings_remaining == 1:
                guesses_remaining -= 1
                warnings_remaining = 3
                if guesses_remaining <= 0:
                    break
                answer = input('Oops! That is not a valid letter. \n You have'
                               + ' no warnins left \n so you lose one guess:'
                               + get_guessed_word(secret_word, letters_guessed) 
                               + ' \n You have ' + str(guesses_remaining) + 
                               ' guesses left. \n Available letters:' + 
                               str(available_letters) + ' \n Please guess a letter:')
            else: 
                warnings_remaining -= 1
                answer = input('Oops! That is not a valid letter. \n You have '
                               + str(warnings_remaining) + ' warnings left:'
                               + get_guessed_word(secret_word, letters_guessed) 
                               + ' \n You have ' + str(guesses_remaining) 
                               + ' guesses left. \n Available letters: ' 
                               + available_letters + ' \n Please guess a letter:')
        elif answer in letters_guessed:
            if warnings_remaining == 1: 
                guesses_remaining -= 1
                warnings_remaining = 3
                if guesses_remaining <= 0:
                    break
                answer = input('Oops! You have already guessed that letter. \n You have'
                               + ' no warnings left \n so you lose one guess:'
                               + get_guessed_word(secret_word, letters_guessed) 
                               + ' \n You have ' + str(guesses_remaining) + 
                               ' guesses left. \n Available letters:' + 
                               str(available_letters) + ' \n Please guess a letter:')
            else: 
                warnings_remaining -= 1
                answer = input('Oops! You have already guessed that letter. \n You have '
                               + str(warnings_remaining) + ' warnings left:'
                               + get_guessed_word(secret_word, letters_guessed) 
                               + ' \n You have ' + str(guesses_remaining) 
                               + ' guesses left. \n Available letters: ' 
                               + available_letters + ' \n Please guess a letter:')
        elif answer in secret_word:
            letters_guessed.append(answer)
            available_letters = get_available_letters(letters_guessed)
            if is_word_guessed(secret_word, letters_guessed):
                break
            answer = input('Good guess: ' 
                           + get_guessed_word(secret_word, letters_guessed)
                           + ' \n You have ' + str(guesses_remaining) 
                           + ' guesses left. \n Available letters:' 
                           + available_letters + ' \n Please guess a letter:')
        elif answer in 'aeiou':
            letters_guessed.append(answer)
            available_letters = get_available_letters(letters_guessed)
            guesses_remaining -= 2
            if guesses_remaining <= 0:
                break
            answer = input('Oops! That letter is not in my word:' 
                           + get_guessed_word(secret_word, letters_guessed)
                           + ' \n You have ' + str(guesses_remaining) + 
                           ' guesses left \n Available Letters:' 
                           + available_letters + ' \n Please guess a letter:')
        else:
            letters_guessed.append(answer)
            available_letters = get_available_letters(letters_guessed)
            guesses_remaining -= 1
            if guesses_remaining <= 0:
                break
            answer = input('Oops! That letter is not in my word:' 
                           + get_guessed_word(secret_word, letters_guessed)
                           + ' \n You have ' + str(guesses_remaining) + 
                           ' guesses left \n Available Letters:' 
                           + available_letters + ' \n Please guess a letter:')
    
    if failure:
        print("Successfully quit the game.")
    elif guesses_remaining <= 0:
        print('Sorry, you ran out of guesses. The word was else.')
        print('The correct word is "' + secret_word + '".')
    else:
        print('Good guess:' + secret_word + 
              ' \n Congradulations, you won! \n Your total score for this game is: '
              + str(guesses_remaining * len(secret_word) * complete_guess_score))




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    '''
    secret_word = choose_word(wordlist)
    hangman(secret_word)
'''
###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    '''
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    '''