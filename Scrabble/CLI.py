import argparse
import FileReader
import ScoreCounter

class CLI:
    def __init__(self):
        print("CLI initiation")# params to tablica parametrów na wejsciu programu
        pass

    def parser(self):
        parser = argparse.ArgumentParser()
        #parser.add_argument("num", help="Number",type=int)
        parser.add_argument("-f", "--file", help="Read words from file", default=print("default"))
        parser.add_argument("-c", "--count", help="Counts a score for the inserted word")
        parser.add_argument("-s", "--score", help="Returns a word with specified score")

        args = parser.parse_args()
        self.validator(args)

    def validator(self, _args):
        if _args.file:
            file = FileReader.FileReader(_args.file)
            file.read_file()


        if _args.count:
            value = ScoreCounter.ScoreCounter(_args.count)
            print(value.result())
            #TODO: counter valuer

        if _args.score:
            print("costam")
            #TODO: scores API SRAPI JAPIERDOLE
        pass



