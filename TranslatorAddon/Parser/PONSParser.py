from Parser import Parser
from urllib import quote_plus
from HTMLParser import HTMLParser

class PONSParser(Parser):

    def createUrl(self, searchTerm, sourceLang, targetLang):
        return "http://en.pons.com/translate?q=" + quote_plus(searchTerm) + "&l=deen&in=" + sourceLang + "&lf=en"


    def getTranslation(self, searchTerm, sourceLang, targetLang):
        doc = self.getSoup(searchTerm, sourceLang, targetLang)

        translations = []

        hp = HTMLParser()

        sources = doc.findAll("div", {"class" : "source"})
        targets = doc.findAll("div", {"class" : "target"})
        for i in range(len(sources)):
            source = hp.unescape("".join(sources[i].findAll(text=True)).strip())
            target = hp.unescape("".join(targets[i].findAll(text=True)).strip())
            translations.append([source, target])

        return translations
