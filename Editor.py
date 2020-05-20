from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from GUI import Ui_MainWindow
import sys


class Editor(QMainWindow):
    def __init__(self):
        super(Editor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



app = QApplication(sys.argv)
window = Editor()
window.show()
sys.exit(app.exec_())
