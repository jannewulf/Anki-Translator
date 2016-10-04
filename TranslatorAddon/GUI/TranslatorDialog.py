from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
from aqt.utils import tooltip
from TranslatorAddon.Parser.PONSParser import PONSParser

# This class describes the Dialog Window in which a vocable can be translated
class TranslatorDialog(QDialog):

    col0Width = 40

    def __init__(self, vocable, defaultSourceLanguage, defaultTargetLanguage, defaultLoadGrammarInfos):
        super(TranslatorDialog, self).__init__()

        # save default values
        self.defaultSrc = defaultSourceLanguage
        self.defaultTgt = defaultTargetLanguage
        self.defaultGram = defaultLoadGrammarInfos

        # Save the looked up vocable (not updated -> use lineEdit to get current value)
        self.editorVocable = vocable
        self.translations = []

        self.parser = PONSParser()

        # set up gui
        self.setupUi()


    # setting up ui elements
    def setupUi(self):
        # Set up window
        self.setWindowTitle("Translator")
        self.setModal(True)
        self.resize(800, 600)

        self.createSettings()

        # create vocab line edit, translations table etc.
        self.createTranslContent()

        # Add Ok and Cancel buttons
        self.createButtonBox()

        # bring ui elements together in main layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.settingsBox)
        mainLayout.addWidget(self.translContentLayout)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)
        self.lineEditVocable.setFocus()


    def createSettings(self):
        self.settingsBox = QGroupBox("Settings")

        self.cmbBoxSourceLang = QComboBox()
        self.cmbBoxSourceLang.addItems(sorted(self.parser.getSourceLanguages().values()))
        try:
            defaultLangCode = self.parser.getSourceLanguages()[self.defaultSrc]
        except Exception:
            defaultLangCode = ""
        index = self.cmbBoxSourceLang.findText(defaultLangCode)
        if index >= 0:
            self.cmbBoxSourceLang.setCurrentIndex(index)

        self.cmbBoxTargetLang = QComboBox()
        self.updateTargetLanguages()
        self.cmbBoxSourceLang.currentIndexChanged.connect(self.updateTargetLanguages)

        self.chkBoxGrammarInfo = QCheckBox()
        self.chkBoxGrammarInfo.setChecked(self.defaultGram)

        layout = QHBoxLayout()
        layout.addWidget(QLabel("Source Language"))
        layout.addWidget(self.cmbBoxSourceLang)
        layout.addStretch(1)
        layout.addWidget(QLabel("Target Language"))
        layout.addWidget(self.cmbBoxTargetLang)
        layout.addStretch(1)
        layout.addWidget(self.chkBoxGrammarInfo)
        layout.addWidget(QLabel("Load Grammar Infos"))
        self.settingsBox.setLayout(layout)


    # creates all the gui elements except for the button box on the bottom
    def createTranslContent(self):
        self.translContentLayout = QGroupBox("Translations")
        layout = QFormLayout()

        # translate button
        self.buttonTranslate = QPushButton("Translate")
        self.buttonTranslate.clicked.connect(self.translate)

        # vocabulary line edit
        self.lineEditVocable = QLineEdit(self.editorVocable)
        self.lineEditVocable.returnPressed.connect(self.buttonTranslate.click)

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

        self.translContentLayout.setLayout(layout)


    # creates the 'Ok' and 'Cancel' buttons
    def createButtonBox(self):
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
            QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.setFieldsAndAccept)
        self.buttonBox.rejected.connect(self.reject)


    # called function on click on translate button
    def translate(self):
        vocab = self.lineEditVocable.text()
        src = self.parser.getLangCode(str(self.cmbBoxSourceLang.currentText()))
        tgt = self.parser.getLangCode(str(self.cmbBoxTargetLang.currentText()))
        grammarInfos = self.chkBoxGrammarInfo.isChecked()

        translations = self.parser.getTranslation(vocab, src, tgt, grammarInfos)
        self.setTableContent(translations)


    # updating the content of the table
    def setTableContent(self, content):
        if content is None:
            return
        if len(content) == 0:
            tooltip("No translations found.")
            return

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


    # collect selected translations and return to editor window
    def setFieldsAndAccept(self):
        rows = self.tableTranslations.rowCount()

        for i in range(rows):
            if self.tableTranslations.item(i, 0).checkState() == Qt.Checked:
                self.translations.append(
                    [self.tableTranslations.item(i, 1).text(),
                    self.tableTranslations.item(i, 2).text()])

        self.accept()


    # Prevent the dialog from closing on enter pressed
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Enter or QKeyEvent.key() == Qt.Key_Return:
            return

    # Update the target languages in the target combo box
    def updateTargetLanguages(self):
        self.cmbBoxTargetLang.clear()
        current = str(self.cmbBoxSourceLang.currentText())
        key = self.parser.getLangCode(current)
        self.cmbBoxTargetLang.addItems(sorted(self.parser.getTargetLanguages(key).values()))

        try:
            defaultLangCode = self.parser.getSourceLanguages()[self.defaultTgt]
        except Exception:
            defaultLangCode = ""
        index = self.cmbBoxTargetLang.findText(defaultLangCode)
        if index >= 0:
            self.cmbBoxTargetLang.setCurrentIndex(index)