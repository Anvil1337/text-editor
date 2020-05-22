# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 644)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_text = QtWidgets.QTextEdit(self.centralwidget)
        self.main_text.setGeometry(QtCore.QRect(20, 60, 801, 521))
        self.main_text.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.main_text.setObjectName("main_text")
        self.font_size_label = QtWidgets.QLabel(self.centralwidget)
        self.font_size_label.setGeometry(QtCore.QRect(630, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.font_size_label.setFont(font)
        self.font_size_label.setObjectName("font_size_label")
        self.select_font_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.select_font_comboBox.setGeometry(QtCore.QRect(420, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.select_font_comboBox.setFont(font)
        self.select_font_comboBox.setObjectName("select_font_comboBox")
        allFonts = QtGui.QFontDatabase().families()
        self.select_font_comboBox.addItems(allFonts)
        self.font_label = QtWidgets.QLabel(self.centralwidget)
        self.font_label.setGeometry(QtCore.QRect(360, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.font_label.setFont(font)
        self.font_label.setObjectName("font_label")
        self.font_size_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.font_size_spinBox.setGeometry(QtCore.QRect(730, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.font_size_spinBox.setFont(font)
        self.font_size_spinBox.setMinimum(5)
        self.font_size_spinBox.setMaximum(100)
        self.font_size_spinBox.setProperty("value", 12)
        self.font_size_spinBox.setObjectName("font_size_spinBox")
        self.bold_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.bold_checkBox.setGeometry(QtCore.QRect(60, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bold_checkBox.setFont(font)
        self.bold_checkBox.setObjectName("bold_checkBox")
        self.italic_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.italic_checkBox.setGeometry(QtCore.QRect(150, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.italic_checkBox.setFont(font)
        self.italic_checkBox.setObjectName("italic_checkBox")
        self.underline_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.underline_checkBox.setGeometry(QtCore.QRect(240, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.underline_checkBox.setFont(font)
        self.underline_checkBox.setObjectName("underline_checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAllignment = QtWidgets.QMenu(self.menubar)
        self.menuAllignment.setObjectName("menuAllignment")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_open = QtWidgets.QAction(MainWindow)
        self.menu_open.setObjectName("menu_open")
        self.menu_save = QtWidgets.QAction(MainWindow)
        self.menu_save.setObjectName("menu_save")
        self.left_alignment = QtWidgets.QAction(MainWindow)
        self.left_alignment.setObjectName("left_alignment")
        self.right_alignment = QtWidgets.QAction(MainWindow)
        self.right_alignment.setObjectName("right_alignment")
        self.center_alignment = QtWidgets.QAction(MainWindow)
        self.center_alignment.setObjectName("center_alignment")
        self.justify_alignment = QtWidgets.QAction(MainWindow)
        self.justify_alignment.setObjectName("justify_alignment")
        self.menu_print = QtWidgets.QAction(MainWindow)
        self.menu_print.setObjectName("menu_print")
        self.menu_print_preview = QtWidgets.QAction(MainWindow)
        self.menu_print_preview.setObjectName("menu_print_preview")
        self.menu_export_pdf = QtWidgets.QAction(MainWindow)
        self.menu_export_pdf.setObjectName("menu_export_pdf")
        self.menuFile.addAction(self.menu_open)
        self.menuFile.addAction(self.menu_save)
        self.menuFile.addAction(self.menu_print)
        self.menuFile.addAction(self.menu_print_preview)
        self.menuFile.addAction(self.menu_export_pdf)
        self.menuAllignment.addAction(self.left_alignment)
        self.menuAllignment.addAction(self.right_alignment)
        self.menuAllignment.addAction(self.center_alignment)
        self.menuAllignment.addAction(self.justify_alignment)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAllignment.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.font_size_label.setText(_translate("MainWindow", "Font size:"))
        self.select_font_comboBox.setItemText(0, _translate("MainWindow", "Arial"))
        self.select_font_comboBox.setItemText(1, _translate("MainWindow", "Times New Roman"))
        self.select_font_comboBox.setItemText(2, _translate("MainWindow", "Impact"))
        self.select_font_comboBox.setItemText(3, _translate("MainWindow", "Palatino"))
        self.select_font_comboBox.setItemText(4, _translate("MainWindow", "Garamond"))
        self.select_font_comboBox.setItemText(5, _translate("MainWindow", "Bookman"))
        self.select_font_comboBox.setItemText(6, _translate("MainWindow", "Avant Garde"))
        self.select_font_comboBox.setItemText(7, _translate("MainWindow", "Helvetica"))
        self.select_font_comboBox.setItemText(8, _translate("MainWindow", "Courier New"))
        self.select_font_comboBox.setItemText(9, _translate("MainWindow", "Verdana"))
        self.select_font_comboBox.setItemText(10, _translate("MainWindow", "Georgia"))
        self.select_font_comboBox.setItemText(11, _translate("MainWindow", "Comic Sans"))
        self.select_font_comboBox.setItemText(12, _translate("MainWindow", "Trebuchet"))
        self.font_label.setText(_translate("MainWindow", "Font:"))
        self.bold_checkBox.setText(_translate("MainWindow", "Bold"))
        self.italic_checkBox.setText(_translate("MainWindow", "Italic"))
        self.underline_checkBox.setText(_translate("MainWindow", "Underline"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAllignment.setTitle(_translate("MainWindow", "Alignment"))
        self.menu_open.setText(_translate("MainWindow", "Open"))
        self.menu_save.setText(_translate("MainWindow", "Save"))
        self.left_alignment.setText(_translate("MainWindow", "Left"))
        self.right_alignment.setText(_translate("MainWindow", "Right"))
        self.center_alignment.setText(_translate("MainWindow", "Center"))
        self.justify_alignment.setText(_translate("MainWindow", "Justify"))
        self.menu_print.setText(_translate("MainWindow", "Print"))
        self.menu_print_preview.setText(_translate("MainWindow", "Print Preview"))
        self.menu_export_pdf.setText(_translate("MainWindow", "Export to PDF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
