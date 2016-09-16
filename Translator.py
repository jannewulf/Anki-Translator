from anki.hooks import addHook
from aqt.editor import Editor
from aqt.utils import showInfo


def getTranslation(editor):
	showInfo("Looking for Translation")

def initTranslatorGUI(editor):
	editor._addButton("Translate", lambda ed=editor: getTranslation(ed),
					text="T", tip="Translate Word (Ctrl+T)", key="Ctrl+t")

Editor.getTranslation = getTranslation
addHook("setupEditorButtons", initTranslatorGUI)
