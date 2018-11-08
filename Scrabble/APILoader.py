import urllib.request
from xml.dom import minidom


class APILoader:
    API_KEY = '2.8244815430997972e29'

    def url_chooser(self, api_word):
        url = 'http://www.wordgamedictionary.com/api/v1/references/scrabble/' + api_word + '?key=2.8244815430997972e29'
        return url

    def url_connection(self, _url):
        xml_object = urllib.request.urlopen(_url)
        dom = minidom.parse(xml_object)
        return dom
