from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
from TranslatorAddon.Parser.PONSParser import PONSParser

class TranslatorDialog(QDialog):

    col0Width = 40

    def __init__(self, vocable):
        super(TranslatorDialog, self).__init__()

        # Save the looked up vocable (not updated -> use lineEdit to get current value)
        self.editorVocable = vocable
        self.translations = []

        # set up gui
        self.setupUi()


    def setupUi(self):
        # Set up window
        self.setWindowTitle("Translator")
        self.setModal(True)
        self.resize(800, 600)

        # create vocab line edit, translations table etc.
        self.createTranslContent()

        # Add Ok and Cancel buttons
        self.createButtonBox()

        # bring ui elements together in main layout
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(self.translContentLayout)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)

    # creates all the gui elements except for the button box on the bottom
    def createTranslContent(self):
        self.translContentLayout = QVBoxLayout()
        self.translContentLayout.setStretch(1, 1)
        layout = QFormLayout()
        #self.translContentLayout = QFormLayout()

        # vocabulary line edit
        self.lineEditVocable = QLineEdit(self.editorVocable)

        # translate button
        self.buttonTranslate = QPushButton("Translate")
        self.buttonTranslate.clicked.connect(self.translate)

        # translations table
        self.tableTranslations = QTableWidget()
        self.tableTranslations.setColumnCount(3)
        self.tableTranslations.setHorizontalHeaderLabels(["Use", "Vocable", "Translation"])
        self.tableTranslations.horizontalHeader().setResizeMode(QHeaderView.Interactive)
        self.tableTranslations.horizontalHeader().setStretchLastSection(True)
        self.tableTranslations.horizontalHeader().resizeSection(0, self.col0Width)
        self.tableTranslations.horizontalHeader().resizeSection(1, (self.tableTranslations.size().width() - self.col0Width) / 2)
        self.tableTranslations.verticalHeader().hide()
        policy = QSizePolicy()
        policy.setHorizontalPolicy(policy.Expanding)
        policy.setVerticalPolicy(policy.Expanding)
        policy.setVerticalStretch(1)
        self.tableTranslations.setSizePolicy(policy)

        layout.addRow(QLabel("Vocable"), self.lineEditVocable)
        layout.addRow(None, self.buttonTranslate)
        layout.addRow(QLabel("Translations"), self.tableTranslations)

        self.translContentLayout.addLayout(layout)


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

        self.setTableContent(translations)


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

        # adjust the height of the table
        rowHeight = self.tableTranslations.verticalHeader().sectionSize(0)
        rowCount = self.tableTranslations.rowCount()
        self.tableTranslations.setMinimumHeight(rowHeight * min(rowCount, 12))


    def setFieldsAndAccept(self):
        rows = self.tableTranslations.rowCount()

        for i in range(rows):
            if self.tableTranslations.item(i, 0).checkState() == Qt.Checked:
                self.translations.append(
                    [self.tableTranslations.item(i, 1).text(),
                    self.tableTranslations.item(i, 2).text()])

        self.accept()
