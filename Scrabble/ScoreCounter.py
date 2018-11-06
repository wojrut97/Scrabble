import WordChecker
import Config

class ScoreCounter:
    def __init__(self, word):
        self._wordchecker = WordChecker.WordChecker()
        self._word = word.upper()

    def result(self):
        if self._wordchecker.check_word(self._word):
            sum = 0
            for letter in range(0, len(self._word)):
                sum += Config.LETTER_SCORES[self._word[letter]]
            return sum

        else:
            print("This word does not exist!")
            pass

    def for_all_counter(self, _words):
        words_and_scores = []
        for i in _words:
            words_and_scores[i] = (_words, self.result())
        return words_and_scores



