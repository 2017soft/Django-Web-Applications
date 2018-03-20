from django.db import models
from hangman.source_code.required_functions import get_guessed_word, get_available_letters, is_word_guessed, match_with_gaps
import string

# Create your models here.
WORDLIST_FILENAME = "words.txt"

inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
line = inFile.readline()
    # wordlist: list of strings
wordlist = line.split()

# Now wordlist stores all the possible words from the database

class Secret(models.Model):
    secret_word = models.CharField(max_length=200)
    guesses_remaining = models.IntegerField(default=6)
    warnings_remaining = models.IntegerField(default=3)
    hints_remaining = models.IntegerField(default=2)
    letters_guessed = []
    available_letters = string.ascii_lowercase
    game_status = models.IntegerField(default=0)
    success_state = models.IntegerField(default=0)
    hint_list = []
    def __str__(self):
        return self.secret_word
    def show_guessed_word(self):
        return get_guessed_word(self.secret_word, self.letters_guessed)
    def show_available_letters(self):
        return get_available_letters(self.letters_guessed)
    def get_all_hints(self):
        return self.hint_list
    def total_number_of_hints(self):
        return len(self.hint_list)
    def get_hints_times(self):
        return self.hints_remaining
    def get_guesses_times(self):
        return self.guesses_remaining 
    def get_warnings_times(self):
        return self.warnings_remaining
    def set_guesses_times(self, times):
        self.guesses_remaining = times
    def set_warnings_times(self, times):
        self.warnings_remaining = times
    def set_hints_times(self, times):
        self.hints_remaining = times
    def lose_a_guess(self):
        self.guesses_remaining -= 1
    def lose_a_warning(self):
        self.warnings_remaining -= 1
    def check_guess(self):
        return self.game_status
    def check_game_success(self):
        return self.success_state
    def start_the_game(self):
        self.success_state = 0
    def letter_in_word(self):
        self.game_status = 1
    def letter_not_in_word(self):
        self.game_status = 2
    def letter_already_guessed(self):
        self.game_status = 3
    def not_valid_guess(self):
        self.game_status = 4
    def require_hints(self):
        self.game_status = 5
    def no_guess_yet(self):
        self.game_status = 0
    def no_guesses_allowed(self):
        self.game_status = -1
    def word_complete(self):
        return is_word_guessed(self.secret_word, self.letters_guessed)
    def game_success(self):
        self.success_state = 1
    def game_failure(self):
        self.success_state = -1
    def show_game_status(self):
        if self.game_status == -1:
            return('You have already finished this game! Please start another game.')
        elif self.game_status == 1:
            return('You made a great guess!!')
        elif self.game_status == 2:
            return('This letter is not in that word.')
        elif self.game_status == 3:
            return('You have already guessed this letter!')
        elif self.game_status == 4:
            return('You entered an invalid response!')
        elif self.game_status == 5:
            return('Please see the hints below.')
        else:
            return('You have not made a guess yet')
        
    def get_success_or_not(self):
        if self.success_state == -1:
            return('Sorry, you ran out of guesses. The correct word is "' 
                   + self.secret_word +'".')
        elif self.success_state == 1:
            return('Congratulation! You got the word!')
        else:
            return('Please continue your guesses')
    def show_hints(self):
        current_word = self.show_guessed_word()
        for word in wordlist:
            if match_with_gaps(current_word, word):
                self.hint_list.append(word)