from Parser import Parser
from Log import log

class PONSParser(Parser):

    def setUrl(self, searchTerm, sourceLang, targetLang):
        return "http://en.pons.com/translate?q=" + searchTerm + "&l=deen&in=en&lf=en"


    def getTranslation(self):
        doc = self.getSoup()

        translations = []

        sources = doc.findAll("div", {"class" : "source"})
        targets = doc.findAll("div", {"class" : "target"})
        for i in range(len(sources)):
            source = "".join(sources[i].findAll(text=True)).strip()
            target = "".join(targets[i].findAll(text=True)).strip()
            translations.append([source, target])

        return translations
