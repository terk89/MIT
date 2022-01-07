# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
#import string

WORDLIST_FILENAME = 'C:\Python\words.txt'


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program

wordlist = load_words()
computer_word = choose_word(wordlist)
computer_word_length = len(computer_word)
hidden_word = '_' * computer_word_length
# your code begins here!
print('Welcome to the game, Hangman!')
print(f"I'm thinking of a word that is {computer_word_length} letters long")
not_guessed = True
available_letters = 'abcdefghijklmnopqrstuvwxyz'
number_of_guesses = int(input('Number of guesses:'))


def check_if_valid(guess):
    """Returns True if a guess is made of a valid character"""
    if guess in available_letters:
        return True
    else:
        return False



def display_dashes(hidden_word, guess, computer_word):
    """ transforms string of dashes ------ into correctly answered letters """
    hidden_word = list(hidden_word)
    computer_word = list(computer_word)
    for i in range(0, len(computer_word)):
        if computer_word[i] == guess:
            hidden_word[i] = guess
    hidden_word = "".join(hidden_word)
    return hidden_word


def print_aster():
    print('*****************')


while not_guessed and number_of_guesses > 0:
    print_aster()
    print(f'You have {number_of_guesses} guesses left.')
    print(f'Available letters: {available_letters}')
    guess = str.lower(input('Please guess a letter:'))
    # Checking if player submits correct letter
    if guess in available_letters:
        available_letters = available_letters.replace(guess, '')
        hidden_word = display_dashes(hidden_word, guess, computer_word)
        # Checking if guess is correct
        if guess in computer_word:
            print(f'Good guess: {hidden_word}')
            if hidden_word == computer_word:
                print_aster()
                print('Congratulations, you won!')
                not_guessed = False
        else:
            print(f'Oops! That letter is not in my word: {hidden_word}')
            number_of_guesses -= 1
    else:
        print('You have entered invalid character...please try again!')
if not_guessed:
   print(f'You loose, my word is: {computer_word}')


