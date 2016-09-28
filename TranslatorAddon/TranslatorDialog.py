import sys
from PyQt4.QtGui import *

class TranslatorDialog(QDialog):

    def __init__(self, editor):
        super(TranslatorDialog, self).__init__()
        
        self.vocable = editor.note.fields[0]

    def setupUi(self):
        return

    def show():
        setupUi()
