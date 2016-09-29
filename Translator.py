from anki.hooks import wrap
from aqt.editor import Editor
from aqt.utils import showInfo
from TranslatorAddon.TranslatorDialog import TranslatorDialog

# This function gets executed when the button in the editor is pressed
def getTranslation(editor):
	dialog = TranslatorDialog(editor.note.fields[0])
	if dialog.exec_():
		for translation in dialog.translations:
			if editor.note.fields[0]:
				editor.note.fields[0] += ",\n"
			editor.note.fields[0] += translation[0]

			if editor.note.fields[1]:
				editor.note.fields[1] += ",\n"
			editor.note.fields[1] += translation[1]

		editor.loadNote()

# Definition of the new button
def mySetupButtons(self):
	self._addButton("Translate", lambda ed=self: getTranslation(ed),
				text="T", tip="Translate Word (Ctrl+T)", key="Ctrl+t")

# Concatenate Editor.setupButtons with mySetupButtons
# So that a new button is inserted into the Editor
Editor.setupButtons = wrap(Editor.setupButtons, mySetupButtons)
