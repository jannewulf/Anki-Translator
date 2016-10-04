from Parser import Parser
from urllib import quote_plus
from HTMLParser import HTMLParser
import xml.etree.ElementTree as ET
import os
import re

class PONSParser(Parser):

    def __init__(self):
        self.langKeys = {}
        self.sourceTargetPairs = {}
        self.parseLangXML()

    def createUrl(self, searchTerm, sourceLang, targetLang):
        search = quote_plus(str(searchTerm))
        src = quote_plus(sourceLang)
        combo = quote_plus(self.sourceTargetPairs[sourceLang][targetLang])
        return "http://en.pons.com/translate?q=" + search + "&l=" + combo + "&in=" + src + "&lf=" + src


    def getTranslation(self, searchTerm, sourceLang, targetLang, loadGrammarInfos):
        doc = self.getSoup(searchTerm, sourceLang, targetLang)
        if doc is None:
            return

        translations = []

        hp = HTMLParser()

        sources = doc.findAll("div", {"class" : re.compile("^source$")})
        targets = doc.findAll("div", {"class" : re.compile("^target( rtl)?$")})
        for i in range(len(sources)):
            source = hp.unescape("".join(sources[i].findAll(text=True)).strip())
            if not loadGrammarInfos:
                [d.extract() for d in targets[i]("span")]
            target = hp.unescape("".join(targets[i].findAll(text=True)).strip())
            translations.append([source, target])

        return translations

    def getSourceLanguages(self):
        return self.langKeys

    def getTargetLanguages(self, sourceLanguage):
        targetLangs = {}
        for code, codePair in self.sourceTargetPairs[sourceLanguage].iteritems():
            targetLangs[code] = self.langKeys[code]
        return targetLangs

    def parseLangXML(self):
        tree = ET.parse(os.path.join(os.path.dirname(__file__), "pons_lang_codes.xml"))
        root = tree.getroot()

        for language in root:
            lang = ""
            code = ""
            targets = {}
            for languageAttribute in language:
                if languageAttribute.tag == "name":
                    lang = languageAttribute.text
                elif languageAttribute.tag == "code":
                    code = languageAttribute.text
                elif languageAttribute.tag == "targets":
                    targets = self.getTargets(languageAttribute)
            self.langKeys[code] = lang
            self.sourceTargetPairs[code] = targets

    def getTargets(self, targets):
        targetsArr = {}
        for target in targets:
            langCode = ""
            combCode = ""
            for targetAttr in target:
                if targetAttr.tag == "lang":
                    langCode = targetAttr.text
                elif targetAttr.tag == "code":
                    combCode = targetAttr.text
            targetsArr[langCode] = combCode
        return targetsArr

    def getLangCode(self, language):
        for code, name in self.langKeys.iteritems():
            if name == language:
                return code

