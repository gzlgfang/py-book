# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'close.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1839, 1051)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(430, 240, 301, 87))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 400, 291, 71))
        font = QtGui.QFont()
        font.setFamily("楷体_GB2312")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(440, 580, 291, 101))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setBold(False)
        font.setWeight(50)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setProperty("intValue", 8)
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 360, 151, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1839, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "scut-China Post"))
        self.label.setText(_translate("MainWindow", "欢迎进入GUI开发学习"))
        self.pushButton.setText(_translate("MainWindow", "清屏"))
import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体
   ui = Ui_MainWindow() # 创建PyQt5设计的窗体
   ui.setupUi(MainWindow) # 调用PyQt5窗体
   MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # 显示关闭按钮
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 退出进程