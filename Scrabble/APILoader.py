import http
import urllib
import xml

class APILoader:
    API_KEY = '2.8244815430997972e29'
    #ta klasa łączy sie z api i wczytuje rzeczy kurwa
    def __init__(self):

        pass

    def url_chooser(self, api_word):
        url = 'http://www.wordgamedictionary.com/api/v1/references/scrabble/' + api_word + '?key=2.8244815430997972e29'



