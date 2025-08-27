import random
import string

from typing import List

WORDLIST_FILENAME = "words.txt"
NUMBER_OF_GUESSES = 8


def load_words() -> List[str]:
    print("Loading word list from file...")
    in_file = open(WORDLIST_FILENAME, "r")
    line = in_file.readline()
    word_list = line.split()
    print(f"   {len(word_list)} words loaded.")
    return word_list


def choose_word(word_list: List[str]) -> str:
    return random.choice(word_list)
    # return "secret"


wordlist = load_words()


def is_word_guessed(secret_word: str, letters_guessed: List[str]):
    correct_letters_guessed = [i for i in letters_guessed if i in secret_word]
    secret_letters = list(set(secret_word))

    if len(correct_letters_guessed) == len(secret_letters):
        return True
    else:
        return False


def get_guessed_word(secret_word: str, letters_guessed: List[str]) -> str:
    correct_letters_guessed = [i for i in letters_guessed if i in secret_word]
    ans = ""

    for i in secret_word:
        if i in correct_letters_guessed:
            ans += i
        else:
            ans += "_"
    return ans


def get_available_letters(letters_guessed: List[str]) -> str:
    lower_case_alphabet = list(string.ascii_lowercase)
    for letter in letters_guessed:
        lower_case_alphabet.remove(letter)
    return "".join(lower_case_alphabet)


def main(secret_word: str):
    print("----------------")
    print("Welcome to the game, Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    incorrect_guesses = 0
    letters_guessed = []

    while NUMBER_OF_GUESSES > incorrect_guesses:
        print("----------------")
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            break

        else:
            print(f"You have {NUMBER_OF_GUESSES - incorrect_guesses} guesses left.")
            print(f"available letters: {get_available_letters(letters_guessed)}")
            guess = ""
            while guess not in list(string.ascii_lowercase):
                guess = str(input("Please guess a letter: ")).lower()

            if guess in letters_guessed:
                print("Oops! You've already guessed that letter.")

            elif guess in secret_word and guess not in letters_guessed:
                letters_guessed.append(guess)
                print("Good guess!")

            else:
                letters_guessed.append(guess)
                incorrect_guesses += 1
                print("Oops! That letter is not in my word.")

            print(get_guessed_word(secret_word, letters_guessed))

        if NUMBER_OF_GUESSES <= incorrect_guesses:
            print("----------------")
            print(f"Sorry, you ran out of guesses. The word was: {secret_word}")
            break

        else:
            continue


if __name__ == "__main__":
    main(choose_word(wordlist).lower())
