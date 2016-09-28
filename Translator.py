from anki.hooks import wrap
from aqt.editor import Editor
from aqt.utils import showInfo
from TranslatorAddon.TranslatorDialog import TranslatorDialog

# This functino gets executed when the button in the editor is pressed
def getTranslation(editor):
	#showInfo("Looking for Translation for " + editor.note.fields[0])
	dialog = TranslatorDialog(editor)
	dialog.exec_()

# Definition of the new button
def mySetupButtons(self):
	self._addButton("Translate", lambda ed=self: getTranslation(ed),
				text="T", tip="Translate Word (Ctrl+T)", key="Ctrl+t")

# Concatenate Editor.setupButtons with mySetupButtons
# So that a new button is inserted into the Editor
Editor.setupButtons = wrap(Editor.setupButtons, mySetupButtons)
