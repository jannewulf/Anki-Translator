from Parser import Parser
import re

class PONSParser(Parser):

    def setUrl(self, searchTerm, sourceLang, targetLang):
        return "http://en.pons.com/translate?q=" + searchTerm + "&l=deen&in=en&lf=en"


    def getTranslation(self):
        doc = self.getSoup()

        translations = []

        divs = doc.findAll("div", { "class" : re.compile("translations") })

        for div in divs:
            sources = div.findAll("div", {"class" : "source"})
            targets = div.findAll("div", {"class" : "target"})
            for i in range(len(sources)):
                source = sources[i].text.encode("utf-8")
                target = targets[i].text.encode("utf-8")
                translations.append([source, target])

        return translations
