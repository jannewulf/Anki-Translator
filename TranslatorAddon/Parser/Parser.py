from abc import ABCMeta, abstractmethod
import requests
from bs4 import BeautifulSoup

# Abstract Parser class
class Parser(object):
    __metaclass__ = ABCMeta

    # returns the html document of the website
    def getHTML(self, searchTerm, sourceLang, targetLang):
        try:
            return requests.get(self.createUrl(searchTerm, sourceLang, targetLang)).text
        except Exception as e:
            from aqt.utils import tooltip
            tooltip(e)
            print(e)
    # returns a BeautifulSoup element of the website
    def getSoup(self, searchTerm, sourceLang, targetLang):
        html = self.getHTML(searchTerm, sourceLang, targetLang)
        if html is not None:
            return BeautifulSoup(html,'html.parser')

    # Abstract Method that needs to be implemented in a Parser inheritance
    # Returns a url to the website with the translations
    @abstractmethod
    def createUrl(self, searchTerm, sourceLang, targetLang):
        pass

    # Abstract Method that needs to be implemented in a Parser inheritance
    # Extracts all the translations of a website
    @abstractmethod
    def getTranslation(self, searchTerm, sourceLang, targetLang, loadGrammarInfos):
        pass

    # Abstract Method that needs to be implemented in a Parser inheritance
    # Returns a dictionary with all country codes and languages from which you can translate something
    @abstractmethod
    def getSourceLanguages(self):
        pass

    # Abstract Method that needs to be implemented in a Parser inheritance
    # Returns a dictionary with all language codes and language names of languages in which you can translate something
    # from a specific source language
    @abstractmethod
    def getTargetLanguages(self, sourceLanguage):
        pass

    # Abstract Method that needs to be implemented in a Parser inheritance
    # Returns the language code to a given language name
    @abstractmethod
    def getLangCode(self, language):
        pass
