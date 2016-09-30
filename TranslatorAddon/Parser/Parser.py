from abc import ABCMeta, abstractmethod
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

# Abstract Parser class
class Parser(object):
    __metaclass__ = ABCMeta

    # returns the html document of the website
    def getHTML(self, searchTerm, sourceLang, targetLang):
        return urlopen(self.createUrl(searchTerm, sourceLang, targetLang)).read()

    # returns a BeautifulSoup element of the website
    def getSoup(self, searchTerm, sourceLang, targetLang):
        return BeautifulSoup(self.getHTML(searchTerm, sourceLang, targetLang))

    # Abstract Method that needs to be implemented in a Parser inheritance
    # Returns a url to the website with the translations
    @abstractmethod
    def createUrl(self, searchTerm, sourceLang, targetLang):
        pass

    # Abstract Method that needs to be implemented in a Parser inheritance
    # Extracts all the translations of a website
    @abstractmethod
    def getTranslation(self, searchTerm, sourceLang, targetLang):
        pass
