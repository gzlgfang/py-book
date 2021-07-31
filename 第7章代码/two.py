from PyQt5.uic import loadUi

class childUI(): #这里直接复制转换出来的代码即可，也可以直接读取UI文件如下
    def setupUi(self,form):
        loadUi('two.ui',self)