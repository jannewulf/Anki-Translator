from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
from Parser import Parser
from aqt.utils import showInfo

class TranslatorDialog(QDialog):

    def __init__(self, editor):
        super(TranslatorDialog, self).__init__()

        # Extract the looked up vocable (not updated -> use lineEdit to get current value)
        self.editorVocable = editor.note.fields[0]

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

        # vocabulary line edit
        self.lineEditVocable = QLineEdit(self.editorVocable)
        layout.addRow(QLabel("Vocable"), self.lineEditVocable)

        # translate button
        self.buttonTranslate = QPushButton("Translate")
        self.buttonTranslate.clicked.connect(self.translate)
        layout.addRow(None, self.buttonTranslate)

        # translations table
        self.tableTranslations = QTableWidget()
        layout.addRow(QLabel("Translations"), self.tableTranslations)
        self.tableTranslations.setColumnCount(3)

        self.formGroupBox.setLayout(layout)


    # creates the 'Ok' and 'Cancel' buttons
    def createButtonBox(self):
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
            QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


    def translate(self):
        vocab = self.lineEditVocable.text()
        p = Parser()
        translations = p.getTranslation(vocab)

        self.tableTranslations.setRowCount(len(translations))

        for i, row in enumerate(translations):
            for j, col in enumerate(row):
                item = QTableWidgetItem(col)
                self.tableTranslations.setItem(i, j + 1, item)
