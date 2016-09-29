from Parser import Parser
import re

class PONSParser(Parser):

    def setUrl(self, searchTerm, sourceLang, targetLang):
        return "http://en.pons.com/translate?q=" + searchTerm + "&l=deen&in=en&lf=en"


    def getTranslation(self):
        doc = self.getSoup()

        divs = doc.findAll("div", { "class" : re.compile("translations") })
        sources = divs[0].findAll("div", {"class" : "source"})
        targets = divs[0].findAll("div", {"class" : "target"})

        with open("/home/jannewulf/Dropbox/Projekte/Anki-Translator/out.txt", "w") as f:
            for i in range(len(sources)):
                print >> f, sources[i].text.encode("utf-8")
                print >> f, targets[i].text.encode("utf-8")
