from .models import Secret
import importlib
from . import views
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

import string 
import random
random_id = random.choice(range(33048, 88948))

# Create your views here.

def homepage(request):
    unknown_word = get_object_or_404(Secret, pk=random_id)
    return render(request, 'hangman/homepage.html', {'unknown_word': unknown_word})

def display(request):
    unknown_word = get_object_or_404(Secret, pk=random_id)
    return render(request, 'hangman/display.html', {'unknown_word': unknown_word})

def guess(request):
    unknown_word = get_object_or_404(Secret, pk=random_id)
    guess_letter = request.POST['letter']
    unknown_word.no_guess_yet()
    unknown_word.hint_list.clear()
    
    if unknown_word.check_game_success() != 0:
        unknown_word.no_guesses_allowed()
    elif guess_letter == unknown_word.secret_word:
        for letter in unknown_word.secret_word:
            if letter not in unknown_word.letters_guessed:
                unknown_word.letters_guessed.append(letter)
        unknown_word.letter_in_word()
    elif guess_letter not in string.ascii_lowercase:
        unknown_word.not_valid_guess()
        unknown_word.lose_a_warning()
    elif guess_letter in unknown_word.letters_guessed:
        unknown_word.letter_already_guessed()
        unknown_word.lose_a_warning()
    elif guess_letter not in unknown_word.secret_word:
        unknown_word.lose_a_guess()
        unknown_word.letter_not_in_word()
    else:
        unknown_word.letter_in_word()
    
    if unknown_word.check_guess() == 1 or unknown_word.check_guess() == 2:
        unknown_word.letters_guessed.append(guess_letter)
    if unknown_word.get_warnings_times() <= 0:
        unknown_word.set_warnings_times(3)
        unknown_word.lose_a_guess()
    if unknown_word.word_complete():
        unknown_word.game_success()
    if unknown_word.get_guesses_times() <= 0:
        unknown_word.game_failure()
    unknown_word.save()
    return HttpResponseRedirect(reverse('hangman:display'))

def quit_game(request):
    unknown_word = get_object_or_404(Secret, pk=random_id)
    unknown_word.game_failure()
    unknown_word.set_guesses_times(0)
    unknown_word.hint_list.clear()
    unknown_word.hints_remaining = 0
    unknown_word.no_guess_yet()
    unknown_word.save()
    return HttpResponseRedirect(reverse('hangman:display'))

def restart(request):
    unknown_word = get_object_or_404(Secret, pk=random_id)
    unknown_word.letters_guessed.clear()
    unknown_word.hint_list.clear()
    unknown_word.set_guesses_times(6)
    unknown_word.set_warnings_times(3)
    unknown_word.start_the_game()
    unknown_word.no_guess_yet()
    unknown_word.hints_remaining = 2
    unknown_word.save()
    importlib.reload(views)
    return HttpResponseRedirect(reverse('hangman:display'))

def hint(request):
    unknown_word = get_object_or_404(Secret, pk=random_id)
    unknown_word.show_hints()
    unknown_word.hints_remaining -= 1
    unknown_word.require_hints()
    unknown_word.save()
    return HttpResponseRedirect(reverse('hangman:display'))