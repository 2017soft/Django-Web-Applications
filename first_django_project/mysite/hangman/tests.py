from django.test import TestCase
from .models import Secret
# Create your tests here.

class SecretModelTests(TestCase):
    def test_default_parameters(self):
        check = True
        sample_word = Secret(secret_word = "apple")
        if sample_word.secret_word != "apple":
            check = False
        if sample_word.get_guesses_times() != 6:
            check = False
        if sample_word.get_warnings_times() != 3:
            check = False
        if sample_word.get_hints_times() != 2:
            check = False
        if len(sample_word.letters_guessed) != 0:
            check = False
        if len(sample_word.get_all_hints()) != 0:
            check = False
        if len(sample_word.available_letters) != 26:
            check = False
        if sample_word.check_guess() != 0:
            check = False
        if sample_word.check_game_success() != 0:
            check = False
        self.assertIs(check, True)
