from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox, QLCDNumber, QPushButton, QShortcut
from PyQt5.uic import loadUi

# from PyQt5.QtCore import pyqtSlot
# from notifypy import Notify

class Calculator(QDialog):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # self.__number = 0
        # Load the .ui file

        loadUi('view/calculator.ui', self)
        self.show()
        # self.btnClick.clicked.connect(self.showInfo)
        # self.btnExit.clicked.connect(self.finishProgram)
        # number = self.one.text()

        # QShortcut(QKeySequence('0'), self).activated.connect(lambda: self.showNumber(0))


        self.one.clicked.connect(lambda: self.showNumber(1))
        self.two.clicked.connect(lambda: self.showNumber(2))
        self.three.clicked.connect(lambda: self.showNumber(3))
        self.four.clicked.connect(lambda: self.showNumber(4))
        self.five.clicked.connect(lambda: self.showNumber(5))
        self.six.clicked.connect(lambda: self.showNumber(6))
        self.seven.clicked.connect(lambda: self.showNumber(7))
        self.eight.clicked.connect(lambda: self.showNumber(8))
        self.nine.clicked.connect(lambda: self.showNumber(9))
        self.zero.clicked.connect(lambda: self.showNumber(0))


    def showNumber(self, number):
        self.lcdNumber.display(number)
        print(number)
        
        



