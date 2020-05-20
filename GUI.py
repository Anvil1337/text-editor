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
        self.main_text.setObjectName("main_text")
        self.apply_button = QtWidgets.QPushButton(self.centralwidget)
        self.apply_button.setGeometry(QtCore.QRect(580, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.apply_button.setFont(font)
        self.apply_button.setObjectName("apply_button")
        self.font_size_label = QtWidgets.QLabel(self.centralwidget)
        self.font_size_label.setGeometry(QtCore.QRect(80, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.font_size_label.setFont(font)
        self.font_size_label.setObjectName("font_size_label")
        self.font_size_spinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.font_size_spinBox.setGeometry(QtCore.QRect(180, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.font_size_spinBox.setFont(font)
        self.font_size_spinBox.setDecimals(0)
        self.font_size_spinBox.setMinimum(5.0)
        self.font_size_spinBox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.font_size_spinBox.setProperty("value", 14.0)
        self.font_size_spinBox.setObjectName("font_size_spinBox")
        self.select_font_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.select_font_comboBox.setGeometry(QtCore.QRect(350, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.select_font_comboBox.setFont(font)
        self.select_font_comboBox.setObjectName("select_font_comboBox")
        self.select_font_comboBox.addItem("")
        self.select_font_comboBox.addItem("")
        self.font_label = QtWidgets.QLabel(self.centralwidget)
        self.font_label.setGeometry(QtCore.QRect(290, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.font_label.setFont(font)
        self.font_label.setObjectName("font_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_open = QtWidgets.QAction(MainWindow)
        self.menu_open.setObjectName("menu_open")
        self.menu_save = QtWidgets.QAction(MainWindow)
        self.menu_save.setObjectName("menu_save")
        self.menuFile.addAction(self.menu_open)
        self.menuFile.addAction(self.menu_save)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.apply_button.setText(_translate("MainWindow", "Apply"))
        self.font_size_label.setText(_translate("MainWindow", "Font size:"))
        self.select_font_comboBox.setItemText(0, _translate("MainWindow", "Times New Roman"))
        self.select_font_comboBox.setItemText(1, _translate("MainWindow", "Arial"))
        self.font_label.setText(_translate("MainWindow", "Font:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menu_open.setText(_translate("MainWindow", "Open"))
        self.menu_save.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
