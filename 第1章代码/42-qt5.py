# GUI界面编程42-qt5.py
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'flgsum.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from scipy import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("楷体_GB2312")
        font.setPointSize(18)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 90, 221, 161))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 130, 231, 61))
        self.lineEdit.setObjectName("lineEdit")

        # 在文本框中输入数字并回车，程序自动与自定义槽函数关联并进行计算
        self.lineEdit.editingFinished.connect(self.sumflg)
        # 注意上面的连接函数必须放在lineEdit的设置后面

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 270, 181, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 350, 151, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 420, 161, 41))
        self.label_4.setObjectName("label_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(310, 270, 241, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(310, 340, 241, 41))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(310, 420, 241, 41))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        # 通过程序增加数字显示位数到18位
        self.lcdNumber.setProperty("digitCount", 18)
        self.lcdNumber_2.setProperty("digitCount", 18)
        self.lcdNumber_3.setProperty("digitCount", 18)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 36))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 自定义函数
    def sumflg(self):
        s1 = self.lineEdit.text()  # 获取文本框字符串
        s1 = int(s1)  # 字符串转变成数字
        sum1 = 0
        sum2 = 0
        sum3 = 0  # 设置初值

        for i in range(s1):
            sum1 = i + 1 + sum1
            sum2 = sum2 + (i + 1) * (i + 1)
            sum3 = sum3 + (i + 1) * (i + 1) * (i + 1)
        sum1 = str(sum1)
        sum2 = str(sum2)
        sum3 = str(sum3)  # 数值转字符串
        self.lcdNumber.setProperty("value", sum1)
        self.lcdNumber_2.setProperty("value", sum2)
        self.lcdNumber_3.setProperty("value", sum3)
        print("s1=", sum1)
        print("s2=", sum2)
        print("s3=", sum3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p>请输入需要求累</p><p>计的转换的数字</p></body></html>",
            )
        )
        self.label_2.setText(_translate("MainWindow", "一次加和"))
        self.label_3.setText(_translate("MainWindow", "平方加和"))
        self.label_4.setText(_translate("MainWindow", "立方加和"))


import sys

# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体
    ui = Ui_MainWindow()  # 创建PyQt5设计的窗体
    ui.setupUi(MainWindow)  # 调用PyQt5窗体
    MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # 显示关闭按钮
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 退出进程
