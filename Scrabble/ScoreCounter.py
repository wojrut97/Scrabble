
import Config
import Max


class ScoreCounter:

    def __init__(self, words):
        self._words = words

    @staticmethod
    def result(word):
        sum = 0
        word = ''.join(filter(str.isalpha, word))
        word = word.upper()
        for letter in range(0, len(word)):
            sum += Config.LETTER_SCORES[word[letter]]
        return sum

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
