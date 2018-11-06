class Max:

    def count_maximum(self, words_and_scores):
        max_word, max_score = '', -1
        for touple in words_and_scores:
            word, score = touple
            if score > max_score:
                max_score = score
                max_word = word
        return max_word, max_score
