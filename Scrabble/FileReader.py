from typing import List, Any


class FileReader:
    _words: List[Any]

    def __init__(self, file_name="dictionary.txt"):
        self._filename = file_name
        self._words = []

    def read_file(self):
        print("reading file " + self._filename)
        file = open(self._filename, "r")
        if file.mode == "r":
            file_content = file.readlines()
            for chunk in file_content:
                self._words.append(chunk.rstrip())
        return self._words
