# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1235, 877)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 20, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_3.setStyleSheet("color:white")
        self.label_3.setIndent(-1)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 150, 201, 41))
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_2.setMaxLength(25)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 230, 201, 41))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_4.setMaxLength(11)
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setDragEnabled(False)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 310, 201, 41))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setMaxLength(25)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setDragEnabled(False)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(460, 230, 201, 41))
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setMaxLength(50)
        self.lineEdit_5.setFrame(True)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setDragEnabled(False)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_5.setClearButtonEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(460, 150, 201, 41))
        self.lineEdit_7.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setMaxLength(25)
        self.lineEdit_7.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_7.setClearButtonEnabled(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 90, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_4.setStyleSheet("color:white")
        self.label_4.setIndent(-1)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 380, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 207, 139);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(910, 300, 201, 41))
        self.lineEdit_8.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setMaxLength(20)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_8.setDragEnabled(False)
        self.lineEdit_8.setClearButtonEnabled(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(910, 230, 201, 41))
        self.lineEdit_9.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_9.setMaxLength(20)
        self.lineEdit_9.setFrame(True)
        self.lineEdit_9.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_9.setDragEnabled(False)
        self.lineEdit_9.setReadOnly(False)
        self.lineEdit_9.setClearButtonEnabled(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(910, 150, 201, 41))
        self.lineEdit_10.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_10.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_10.setMaxLength(30)
        self.lineEdit_10.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_10.setClearButtonEnabled(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(930, 90, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_5.setStyleSheet("color:white")
        self.label_5.setIndent(-1)
        self.label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(920, 370, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 191, 117);\n"
"QPushButton{\n"
"    background-color: rgb(125, 117, 116);\n"
"color:white;\n"
"border-radius:10;}\n"
"QPushButton::hover{\n"
"background-color: rgb(0, 34, 53);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(470, 310, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 197, 138);\n"
"QPushButton{\n"
"    background-color: rgb(125, 117, 116);\n"
"color:white;\n"
"border-radius:10;}\n"
"QPushButton::hover{\n"
"background-color: rgb(0, 34, 53);\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(960, 600, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 207, 139);")
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1235, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "İKU Bilet Satış Platformu"))
        self.label_3.setText(_translate("MainWindow", "Etkinlikler"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Etkinlik Adı"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Etkinlik Tarihi"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Etkinlik Mekanı"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Etkinlik Bilgileri"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "Bilet Numarası"))
        self.label_4.setText(_translate("MainWindow", "Bilet"))
        self.pushButton_4.setText(_translate("MainWindow", "Etkinlik Ekle"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "Bilet Alımı"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "Kullanıcı No"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "Kullanıcı Ad/Soyad"))
        self.label_5.setText(_translate("MainWindow", "Kullanıcılar"))
        self.pushButton_5.setText(_translate("MainWindow", "Kullanıcı Ekle"))
        self.pushButton_6.setText(_translate("MainWindow", "Bilet Al / Sat"))
        self.pushButton_7.setText(_translate("MainWindow", "Bilgiler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
