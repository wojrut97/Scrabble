import argparse
import FileReader
import ScoreCounter
import WordFinder
import random


class CLI:

    def parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", help="Returns the highest scored word from file")
        parser.add_argument("-c", "--count", help="Counts a score for the inserted word")
        parser.add_argument("-s", "--score", help="Returns a word with specified score")

        args = parser.parse_args()
        self.validator(args)

    # Depending on given in console arguments executes proper actions
    def validator(self, _args):
        if _args.file:
            file = FileReader.FileReader(_args.file)
            word = file.read_file()
            scorecounter = ScoreCounter.ScoreCounter(word)
            print(scorecounter.max_from_file())

        if _args.count:
            value = ScoreCounter.ScoreCounter(_args.count)
            print("score for word: " + _args.count + ": " + str(value.result(_args.count)))

        if _args.score:
            file = FileReader.FileReader('dictionary.txt')
            word = file.read_file()
            scorecounter = ScoreCounter.ScoreCounter(word)
            list_of_words_and_scores = scorecounter.count_for_all()
            list_of_words_and_scores.sort(key=lambda tup: tup[1])
            word_finder = WordFinder.WordFinder(list_of_words_and_scores, _args.score)

            if word_finder.search_a_word() is not None:
                print(random.choice(word_finder.find_all_matching_words()))

        pass


