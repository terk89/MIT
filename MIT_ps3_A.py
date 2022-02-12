# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
#

import random
#import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
#HAND_SIZE = 10

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "C:\Python\words_scrabble.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

	The score for a word is the sum of the points for letters
	in the word multiplied by the length of the word, plus 50
	points if all n letters are used on the first go.

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO...
    score = 0
    bonus = 50
    for i in word:
        score += SCRABBLE_LETTER_VALUES[i]
    score = score * len(word)
    # 50 bonus when used all letters from hand at single guess
    if len(word) == n:
        score += bonus
    return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end = ' ')  # print all on the same line
    print()
    return

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n // 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
	In other words, this assumes that however many times
	a letter appears in 'word', 'hand' has at least as
	many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # shallow copy hand to avoid changing the hand variable
    hand_temp = hand.copy()
    new_hand = {}
    word_freq = get_frequency_dict(word)
    # subtracting used letters from hand
    for i in hand:
        hand_temp[i] = (hand[i] - word_freq.get(i, 0))
    # removing keys with value of 0
    for i in hand_temp.keys():
        if hand_temp[i] != 0:
            new_hand[i] = hand_temp[i]
    return new_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    word_dictionary = get_frequency_dict(word)
    # check if word in word_list
    if word not in word_list:
        return False
    # check if the type of letters is matching up
    for i in range(len(word)):
        if word[i] not in hand:
            return False
    # check if the letters quantities are correct, hand[letter] >= word[letter]
    for i in word_dictionary.keys():
        if (hand[i] - word_dictionary[i]) < 0:
            return False
        else:
            return True


def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen


#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings

    """
    # TO DO ...
    total_score = 0
    single_play_score = 0
    wrong_letter = True
    play_the_game = True
    # start the game
    while play_the_game:
        # double while loop to allow multiple rounds
        wrong_letter = True
        while wrong_letter:
            print(f'Current Hand: '), display_hand(hand)
            players_word = input("Enter word, or a '.' to indicate that you are finished: ")
            if players_word == '.':
                print(f"You have chosen to quit by pressing {players_word}")
                print(f'You have earned {total_score} scores')
                return
            # Check if input word is valid
            elif not is_valid_word(players_word, hand, word_list):
                print(f"{players_word} is not a valid word, please try again or enter '.' to quit")
            # jump out of inner while loop into the game with users word
            else:
                wrong_letter = False
        # scoring users input word
        single_play_score = get_word_score(players_word,HAND_SIZE)
        total_score += single_play_score
        print(f'"{players_word}" earned {single_play_score}. Total: {total_score}')
        # updating players hand
        hand = update_hand(hand, players_word)
        # if all letters are used exit the game
        if calculate_handlen(hand) == 0:
            play_the_game = False
    return

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
#
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO...
    number_of_hands = int(input("Please choose the number of hands you are about to play: "))
    play_the_game = True
    hand = deal_hand(HAND_SIZE)
    while play_the_game and number_of_hands > 0:
        previous_hand = hand
        user_input = input('Enter "n" to play new random hand, "r" to play last hand, or "e" to exit: ')
        if user_input == "n":
            hand = deal_hand(HAND_SIZE)
            play_hand(hand, word_list)
        elif user_input == "r":
            play_hand(previous_hand, word_list)
        elif user_input == "e":
            print("Quitting, thanks for playing !")
            return
        else:
            print("Something went wrong, please try again")
        number_of_hands -= 1
        print(f'{number_of_hands} hands left')
    return



#
# Build data structures used for entire session and play game


if __name__ == '__main__':
    word_list = load_words()
    HAND_SIZE = int(input("Please choose the hand size: "))
    play_game(word_list)



