from abc import ABCMeta, abstractmethod
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

# Abstract Parser class
class Parser(object):
    __metaclass__ = ABCMeta


    def getHTML(self, searchTerm, sourceLang, targetLang):
        return urlopen(self.createUrl(searchTerm, sourceLang, targetLang)).read()


    def getSoup(self, searchTerm, sourceLang, targetLang):
        return BeautifulSoup(self.getHTML(searchTerm, sourceLang, targetLang))


    @abstractmethod
    def createUrl(self, searchTerm, sourceLang, targetLang):
        pass


    @abstractmethod
    def getTranslation(self, searchTerm, sourceLang, targetLang):
        pass
