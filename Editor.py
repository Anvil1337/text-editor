from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from GUI import Ui_MainWindow
import sys


class Editor(QMainWindow):
    def __init__(self):
        super(Editor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.main_text.setText('Hello!')

        self.ui.menu_save.triggered.connect(self.save)

        self.ui.menu_open.triggered.connect(self.open)

        self.ui.menu_print.triggered.connect(self.print_file)

        self.ui.menu_print_preview.triggered.connect(self.print_preview)

        self.ui.menu_export_pdf.triggered.connect(self.export_pdf)
        
        self.ui.left_alignment.triggered.connect(
            lambda: self.ui.main_text.setAlignment(Qt.AlignLeft))

        self.ui.center_alignment.triggered.connect(
            lambda: self.ui.main_text.setAlignment(Qt.AlignCenter))

        self.ui.right_alignment.triggered.connect(
            lambda: self.ui.main_text.setAlignment(Qt.AlignRight))

        self.ui.justify_alignment.triggered.connect(
            lambda: self.ui.main_text.setAlignment(Qt.AlignJustify))

        self.ui.bold_checkBox.toggled.connect(
            lambda: self.ui.main_text.setFontWeight(QFont.Bold if self.ui.bold_checkBox.isChecked() else 0))

        self.ui.italic_checkBox.toggled.connect(
            lambda: self.ui.main_text.setFontItalic(self.ui.italic_checkBox.isChecked()))

        self.ui.underline_checkBox.toggled.connect(
            lambda: self.ui.main_text.setFontUnderline(self.ui.underline_checkBox.isChecked()))

        self.ui.font_size_spinBox.valueChanged.connect(
            lambda: self.ui.main_text.setFontPointSize(self.ui.font_size_spinBox.value()))

        self.ui.select_font_comboBox.currentTextChanged.connect(
            lambda: self.ui.main_text.setCurrentFont(QFont(self.ui.select_font_comboBox.currentText(),
                                                           self.ui.font_size_spinBox.value())))

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

    def print_file(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.ui.main_text.print_(printer)

    def print_preview(self):
        printer = QPrinter(QPrinter.HighResolution)
        print(123)
        preview_dialog = QPrintPreviewDialog(printer, self)
        preview_dialog.paintRequested.connect(
            lambda: self.ui.main_text.print_(printer))
        preview_dialog.exec_()

    def export_pdf(self):
        fn, _ = QFileDialog.getSaveFileName(self, 'Export to PDF', None, 'PDF files (.pdf) ;; All Files')
        if fn != '':
            if QFileInfo(fn).suffix() == '':
                fn += '.pdf'
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.ui.main_text.document().print_(printer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Editor()
    window.show()
    sys.exit(app.exec_())
