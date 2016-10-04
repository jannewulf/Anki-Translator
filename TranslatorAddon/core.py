from anki.hooks import wrap
from aqt.editor import Editor
from GUI.TranslatorDialog import TranslatorDialog


defaultSourceLanguage = ""
defaultTargetLanguage = ""
defaultLoadGrammarInfos = ""

# This function gets executed when the button in the editor is pressed
def getTranslation(editor):
    dialog = TranslatorDialog(editor.note.fields[0], defaultSourceLanguage, defaultTargetLanguage, defaultLoadGrammarInfos)
    if dialog.exec_():
        vocabs = [vocab[0] for vocab in dialog.translations]
        vocabs = set(vocabs)
        for vocab in vocabs:
            if editor.note.fields[0]:
                editor.note.fields[0] += ",\n"
            editor.note.fields[0] += vocab

        translations = [translation[1] for translation in dialog.translations]
        for translation in translations:
            if editor.note.fields[1]:
                editor.note.fields[1] += ",\n"
            editor.note.fields[1] += translation

        editor.loadNote()


# Definition of the new button
def mySetupButtons(self):
    self._addButton("Translate", lambda ed=self: getTranslation(ed),
                    text="T", tip="Translate Word (Ctrl+T)", key="Ctrl+t")


def init():
    # Concatenate Editor.setupButtons with mySetupButtons
    # So that a new button is inserted into the Editor
    Editor.setupButtons = wrap(Editor.setupButtons, mySetupButtons)
