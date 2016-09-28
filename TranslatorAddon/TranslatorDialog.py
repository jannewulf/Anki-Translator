from PyQt4.QtGui import *
from PyQt4.QtCore import Qt

class TranslatorDialog(QDialog):

    def __init__(self, editor):
        super(TranslatorDialog, self).__init__()

        # Extract the looked up vocable
        self.vocable = editor.note.fields[0]

        # set up gui
        self.setupUi()

    def setupUi(self):
        # Set up window
        self.setWindowTitle("Translator")
        self.setModal(True)

        # create vocab line edit, translations table etc.
        self.createGroupBox()

        # Add Ok and Cancel buttons
        self.createButtonBox()

        # bring ui elements together in main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)

    # creates all the gui elements except for the button box on the bottom
    def createGroupBox(self):
        self.formGroupBox = QGroupBox("Group Box")
        layout = QFormLayout()
        layout.addRow(QLabel("Vocable"), QLineEdit(self.vocable))
        layout.addRow(None, QPushButton("Translate"))
        layout.addRow(QLabel("Translations"), QTableView())
        self.formGroupBox.setLayout(layout)

    # creates the 'Ok' and 'Cancel' buttons
    def createButtonBox(self):
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
            QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
