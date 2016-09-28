from PyQt4.QtGui import QDialog, QDialogButtonBox
from PyQt4.QtCore import Qt

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

        # Add Ok and Cancel buttons
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

    def show(self):
        self.setupUi()
        self.exec_()
