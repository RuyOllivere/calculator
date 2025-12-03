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
        self.selectedOperator = None
        self.operationList = {
            "+": self.Plus,
            "-": self.Substraction,
            "*": self.Multiply,
            "/": self.Divide,
            "%": self.percent
        }

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
        self.plus.clicked.connect(lambda: self.setOperation("+"))
        self.plus_2.clicked.connect(lambda: self.setOperation("+"))
        self.multiply.clicked.connect(lambda: self.setOperation("*"))
        self.divideNum.clicked.connect(lambda: self.setOperation("/"))
        self.clean_last.clicked.connect(self.cleanLastNumber)
        self.invertNum.clicked.connect(self.invertNumber)
        self.percentage.clicked.connect(self.percent)
        
        self.minus.clicked.connect(self.Substraction)

        self.equal.clicked.connect(self.Equal)

        self.comma.clicked.connect(self.dot)
        self.clean.clicked.connect(self.Clean)

    def dot(self):
        if(self.current_input.find('.') == -1):
            self.current_input += "."
        self.lcdNumber.display(self.current_input)
    
    def percent(self):
        if len(self.current_input) > 0:
            num = float(self.current_input)
            num = num / 100
            self.current_input = str(num)
        self.lcdNumber.display(self.current_input)

    def cleanLastNumber(self):
        if len(self.current_input) > 0:
            self.current_input = self.current_input[:-1]
        self.lcdNumber.display(self.current_input)

    def setOperation(self, operationList):
        # print(operationList)
        self.selectedOperator = self.operationList[operationList]
        self.current_input += operationList
        self.lcdNumber.display(self.current_input)
        print(self.operationList[operationList])
        print(self.current_input)

    def invertNumber(self):
        if self.current_input.startswith('-'):
            self.current_input = self.current_input[1:]
        else:
            self.current_input = '-' + self.current_input
        self.lcdNumber.display(self.current_input)


    def Substraction(self):
        result = self.current_input
        self.display2.setText(result + "-")
        self.Clean()
    
    def Divide(self):
        result = self.current_input
        self.display2.setText(result + "/")
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
        # continue making the last operation
        
        self.display2.setText("")

    def Multiply(self):
        self.current_input += "*"
        print(self.current_input)
        # self.current_input = str(num + newNum)
        print(self.current_input)


