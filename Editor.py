from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI import Ui_MainWindow
import sys


class Editor(QMainWindow):
    def __init__(self):
        super(Editor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.apply_button.clicked.connect(self.apply_changes)

    def apply_changes(self):
        self.ui.main_text.setFont(QFont(self.ui.select_font_comboBox.currentText(), int(self.ui.font_size_spinBox.value())))

    def save(self):
        pass

    def open(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Editor()
    window.show()
    sys.exit(app.exec_())
