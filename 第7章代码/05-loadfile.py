# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadfile.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1262, 882)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 240, 461, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 350, 221, 81))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 470, 221, 81))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 590, 221, 81))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 350, 221, 81))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 470, 221, 81))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(630, 590, 221, 81))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1262, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        timer = QtCore.QTimer(MainWindow)  # 创建一个QTimer计时器对象
        timer.timeout.connect(self.showtime)  # 发射timeout信号，与自定义槽函数关联
        timer.start()  # 启动计

        self.pushButton.clicked.connect(self.loadhelp1)
        self.pushButton_2.clicked.connect(self.loadhelp2)
        self.pushButton_3.clicked.connect(self.loadhelp3)
        self.pushButton_4.clicked.connect(self.loadhelp4)
        self.pushButton_5.clicked.connect(self.loadhelp5)
        self.pushButton_6.clicked.connect(self.loadhelp6)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "欢迎进入帮助文档操作系统"))
        self.pushButton.setText(_translate("MainWindow", "第一章目录"))
        self.pushButton_2.setText(_translate("MainWindow", "第二章目录"))
        self.pushButton_3.setText(_translate("MainWindow", "第三章目录"))
        self.pushButton_4.setText(_translate("MainWindow", "第四章目录"))
        self.pushButton_5.setText(_translate("MainWindow", "第五章目录"))
        self.pushButton_6.setText(_translate("MainWindow", "第六章目录"))


    def loadhelp1(self):
        import os
        os.startfile("help1.pdf")

    def loadhelp2(self):
        import os
        os.startfile("help2.pdf")

    def loadhelp3(self):
        import os
        os.startfile("help3.pdf")
    def loadhelp4(self):
        import os
        os.startfile("help4.pdf")
    def loadhelp5(self):
        import os
        os.startfile("help5.pdf")
    def loadhelp6(self):
        import os
        os.startfile("help6.pdf")


    def showtime(self):
            import time
            my_format1 = "%Y/%m/%d %H:%M:%S"  # 定义时间格式
            time1 = time.strftime(my_format1)
            self.statusbar.showMessage('当前日期时间：' + time1, 0)  # 在状态栏中显示日期时间



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