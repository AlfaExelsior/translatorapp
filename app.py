from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QComboBox, QLabel
from PyQt5.QtGui import QFont
from googletrans import LANGUAGES, Translator

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.translator = Translator()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 220)
        self.setWindowTitle('Translator App')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label1 = QLabel("Text to translate:")
        self.layout.addWidget(self.label1)

        self.text_to_translate = QTextEdit()
        self.text_to_translate.setStyleSheet("border-radius: 10px; font-size: 12px; padding: 10px;")
        self.layout.addWidget(self.text_to_translate)

        self.label2 = QLabel("Destination language:")
        self.layout.addWidget(self.label2)

        self.language_menu = QComboBox()
        self.language_menu.addItems(list(LANGUAGES.values()))
        self.layout.addWidget(self.language_menu)

        self.translate_button = QPushButton("Translate")
        self.translate_button.setStyleSheet("background-color: #4285F4; color: white; border-radius: 5px; padding: 10px; font-size: 16px;")
        self.translate_button.clicked.connect(self.translate_text)
        self.layout.addWidget(self.translate_button)

        self.label3 = QLabel("Translated text:")
        self.layout.addWidget(self.label3)

        self.translated_text = QTextEdit()
        self.translated_text.setStyleSheet("border-radius: 10px; font-size: 12px; padding: 10px;")
        self.layout.addWidget(self.translated_text)

    def translate_text(self):
        text = self.text_to_translate.toPlainText()
        dest_language = self.language_menu.currentText()
        dest_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(dest_language)]
        translated = self.translator.translate(text, dest=dest_language_code)
        self.translated_text.setText(translated.text)

def main():
    app = QApplication([])
    translator = TranslatorApp()
    translator.show()
    app.exec_()

if __name__ == "__main__":
    main()