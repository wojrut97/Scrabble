class WordFinder:
    def __init__(self, sorted_words_and_scores, searching_score):
        self._sorted_words_and_scores = sorted_words_and_scores
        self._searching_score = int(searching_score)
        pass

    def search_a_word(self):
        first = 0
        last = len(self._sorted_words_and_scores)-1
        found = False

        try:
            while first <= last and not found:
                midpoint = (first + last)//2
                if self._sorted_words_and_scores[midpoint][1] == self._searching_score:
                    found = True
                    searched_word = self._sorted_words_and_scores[midpoint][0]
                else:
                    if self._searching_score < self._sorted_words_and_scores[midpoint][1]:
                        last = midpoint-1
                    else:
                        first = midpoint+1
            return searched_word, midpoint
        except UnboundLocalError:
            print("There is no word for this score :(")

    def find_all_matching_words(self):
        word, start_index = self.search_a_word()
        index = start_index
        all_matching_words = [word]
        all_above_found = False
        all_under_found = False
        if word is not None:
            while not all_above_found:
                if self._sorted_words_and_scores[index-1][1] == self._searching_score:
                    all_matching_words.append(self._sorted_words_and_scores[index-1][0])
                    index -= 1
                else:
                    all_above_found = True
            index = start_index
            while not all_under_found:
                if self._sorted_words_and_scores[index+1][1] == self._searching_score:
                    all_matching_words.append(self._sorted_words_and_scores[index+1][0])
                    index += 1
                else:
                    all_under_found = True
        return all_matching_words




