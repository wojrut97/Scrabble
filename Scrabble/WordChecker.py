import APILoader


class WordChecker:
    def __init__(self):
        self._apiloader = APILoader.APILoader()
        pass

    def check_word(self, word):
        url = self._apiloader.url_chooser(word)
        dom = self._apiloader.url_connection(url)

        xml_element = dom.getElementsByTagName('wwf')
        word_exist = int(xml_element[0].firstChild.nodeValue)

        if word_exist == 1:
            return True
        else:
            return False
