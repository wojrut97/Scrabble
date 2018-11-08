import WordChecker
import Config
import Max


class ScoreCounter:

    def __init__(self, words):
        self._wordchecker = WordChecker.WordChecker()
        self._words = words

    def result(self, word):
        sum = 0
        word = word.upper()
        if self._wordchecker.check_word(word):
            for letter in range(0, len(word)):
                sum += Config.LETTER_SCORES[word[letter]]
            return sum

        else:
            print("This word does not exist!")
            return 0

    def count_for_all(self):
        words_and_scores = []
        for word in self._words:
            score = self.result(word)
            words_and_scores.append((word, score))
        return words_and_scores

    def max_from_file(self):
        words_and_scores = self.count_for_all()
        max_counter = Max.Max()
        return max_counter.count_maximum(words_and_scores)
