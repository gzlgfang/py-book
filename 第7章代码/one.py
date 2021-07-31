import sys
import two
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi



class MainUI(): #这里直接复制转换出来的代码即可，也可以直接读取UI文件如下：
    def setupUi(self, Form):
        loadUi('one.ui',self)

class Main(QWidget, MainUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Child(QWidget,two.childUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    Main = Main()
    Child=Child()
    Main.show()


    def showmain():
        Child.close()
        Main.show()
    def showchild():
        Main.close()
        Child.show()


    Main.pushButton.clicked.connect(showchild)
    Child.pushButton.clicked.connect(showmain)
    sys.exit(app.exec_())
