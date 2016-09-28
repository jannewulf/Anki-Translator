import sys
from PyQt4.QtGui import QDialog

class TranslatorDialog(QDialog):

    def __init__(self, editor):
        super(TranslatorDialog, self).__init__()

        self.editor = editor
        self.vocable = editor.note.fields[0]

    # Check how to implement a QDialog (which functions needed etc.)

    def setupUi(self):
        # TODO create widget
        self.setWindowTitle("Translator")
        self.setModal(True)

    def show(self):
        self.setupUi()
        self.exec_()
