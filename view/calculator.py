from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox, QLCDNumber, QPushButton, QShortcut
from PyQt5.uic import loadUi

from PyQt5.QtCore import pyqtSlot
from time import sleep 
        
class Calculator(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loadUi('view/calculator.ui', self)
        self.show()

        self.current_input = ""

        # Connect - self.[btnName].[action].connect()
        self.one.clicked.connect(lambda: self.showNumber("1"))
        self.two.clicked.connect(lambda: self.showNumber("2"))
        self.three.clicked.connect(lambda: self.showNumber("3"))
        self.four.clicked.connect(lambda: self.showNumber("4"))
        self.five.clicked.connect(lambda: self.showNumber("5"))
        self.six.clicked.connect(lambda: self.showNumber("6"))
        self.seven.clicked.connect(lambda: self.showNumber("7"))
        self.eight.clicked.connect(lambda: self.showNumber("8"))
        self.nine.clicked.connect(lambda: self.showNumber("9"))
        self.zero.clicked.connect(lambda: self.showNumber("0"))
        self.plus.clicked.connect(self.Plus)
        self.plus_2.clicked.connect(self.Plus)
        
        self.minus.clicked.connect(self.Substraction)

        self.equal.clicked.connect(self.Equal)

        self.comma.clicked.connect(self.dot)
        self.clean.clicked.connect(self.Clean)

    def dot(self):
        if(self.current_input.find('.') == -1):
            self.current_input += "."
        self.lcdNumber.display(self.current_input)


    def Substraction(self):
        result = self.current_input
        self.display2.setText(result + "-")
        self.Clean()

    def showNumber(self, number):
        self.current_input += number
        self.lcdNumber.display(self.current_input)

    def result(self, display):
        num2 = self.display2.text()
        

    def Clean(self):
        self.current_input = ""
        self.lcdNumber.display("0")

    def Plus(self):
        # num = float(self.current_input) if self.current_input else 0
        # self.Clean()
        # newNum = 5
        self.current_input += "+"
        print(self.current_input)
        # self.current_input = str(num + newNum)
        print(self.current_input)
    
    def Equal(self):
        # numCalculated = eval(self.current_input)
        # self.Clean()
        # self.lcdNumber.display(numCalculated)

        # self.lcdNumber.display(eval(str(self.display2.text() + self.lcdNumber.value())))
        self.display2.setText(self.display2.text() + self.current_input)

        self.lcdNumber.display("0")
        self.lcdNumber.display(eval(self.display2.text()))

    def Multiply(self):
        self.current_input += "*"
        print(self.current_input)
        # self.current_input = str(num + newNum)
        print(self.current_input)


