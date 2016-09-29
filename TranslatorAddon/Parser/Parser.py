from abc import ABCMeta, abstractmethod
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

# Abstract Parser class
class Parser(object):
    __metaclass__ = ABCMeta

    def __init__(self, searchTerm, sourceLang, targetLang):
        self.searchTerm = searchTerm
        self.sourceLang = sourceLang
        self.targetLang = targetLang
        self.url = self.setUrl(searchTerm, sourceLang, targetLang)


    def getHTML(self):
        return urlopen(self.url).read()


    def getSoup(self):
        return BeautifulSoup(self.getHTML())


    @abstractmethod
    def setUrl(self, searchTerm, sourceLang, targetLang):
        pass


    @abstractmethod
    def getTranslation(self):
        pass
