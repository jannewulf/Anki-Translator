from PyQt4.QtGui import *
from PyQt4.QtCore import Qt, QRect
from Parser.PONSParser import PONSParser
from aqt.utils import showInfo

class TranslatorDialog(QDialog):

    def __init__(self, vocable):
        super(TranslatorDialog, self).__init__()

        # Extract the looked up vocable (not updated -> use lineEdit to get current value)
        self.editorVocable = vocable
        self.translations = []

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
        self.formGroupBox = QGroupBox()
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
        self.tableTranslations.setMinimumWidth(600)
        self.tableTranslations.setColumnCount(3)
        self.tableTranslations.setHorizontalHeaderLabels(["Use", "Vocable", "Translation"])
        self.tableTranslations.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        self.tableTranslations.horizontalHeader().setStretchLastSection(True)
        self.tableTranslations.verticalHeader().hide()
        layout.addRow(QLabel("Translations"), self.tableTranslations)

        self.formGroupBox.setLayout(layout)


    # creates the 'Ok' and 'Cancel' buttons
    def createButtonBox(self):
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
            QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.setFieldsAndAccept)
        self.buttonBox.rejected.connect(self.reject)


    def translate(self):
        vocab = self.lineEditVocable.text()
        p = PONSParser()
        translations = p.getTranslation(vocab, "en", "de")

        try:
            self.setTableContent(translations)
        except Exception as e:
            self.setTableContent([["NO", "DATA"]])


    def setTableContent(self, content):
        self.tableTranslations.setRowCount(len(content))

        for i, row in enumerate(content):
            for j, col in enumerate(row):
                if j == 0:
                    chkBoxItem = QTableWidgetItem()
                    chkBoxItem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(Qt.Unchecked)
                    self.tableTranslations.setItem(i, j, chkBoxItem)
                item = QTableWidgetItem(col)
                self.tableTranslations.setItem(i, j + 1, item)


    def setFieldsAndAccept(self):
        cols = self.tableTranslations.columnCount()
        rows = self.tableTranslations.rowCount()

        for i in range(rows):
            if self.tableTranslations.item(i, 0).checkState() == Qt.Checked:
                self.translations.append(
                    [self.tableTranslations.item(i, 1).text(),
                    self.tableTranslations.item(i, 2).text()])

        self.accept()
