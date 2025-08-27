import os
import unittest

import main

TMP_FILE_NAME = "tmp-words.txt"
main.WORDLIST_FILENAME = TMP_FILE_NAME


class TestHangmanMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.secret_word = "secret"
        with open(TMP_FILE_NAME, "w") as f:
            f.write("hello world")
        self.list_of_words = main.load_words()
        f.close()

    def tearDown(self) -> None:
        os.remove(TMP_FILE_NAME)

    def test_load_file_returns_the_correct_list(self):
        assert len(self.list_of_words) == 2
        assert self.list_of_words == ["hello", "world"]

    def test_word_selector_is_random(self):
        count = 50
        result = {"hello": 0, "world": 0}
        while count > 0:
            word = main.choose_word(self.list_of_words)
            result[word] += 1
            count -= 1

        assert result["hello"] != 0
        assert result["world"] != 0

    def test_correct_answer_was_guessed(self):
        letters_guessed = list(set(self.secret_word))
        assert main.is_word_guessed(self.secret_word, letters_guessed)

    def test_incorrect_answer_was_guessed(self):
        letters_guessed = list(set("incorect"))
        assert not main.is_word_guessed(self.secret_word, letters_guessed)

    def test_available_letters(self):
        letters_guessed = list(set("abc"))
        expected_list = [char for char in "defghijklmnopqrstuvwxyz"]
        expected_result = "".join(expected_list)
        assert main.get_available_letters(letters_guessed) == expected_result


if __name__ == "__main__":
    unittest.main()
