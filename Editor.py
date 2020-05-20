from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from GUI import Ui_MainWindow
import sys


class Editor(QMainWindow):
    def __init__(self):
        super(Editor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.apply_button.clicked.connect(self.apply_changes)

        self.ui.menu_save.triggered.connect(self.save)

        self.ui.menu_open.triggered.connect(self.open)

    def apply_changes(self):
        self.ui.main_text.setFont(QFont(self.ui.select_font_comboBox.currentText(),
                                        int(self.ui.font_size_spinBox.value())))

    def save(self):
        file_name = QFileDialog.getSaveFileName(self, 'Save File')[0]
        if file_name != '':
            with open(file_name, 'a') as f:
                f.seek(0)
                f.truncate()
                f.write(self.ui.main_text.toPlainText())

    def open(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File')[0]
        if file_name != '':
            with open(file_name, 'r') as file:
                self.ui.main_text.setText(file.read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Editor()
    window.show()
    sys.exit(app.exec_())
