from PyQt5.QtWidgets import QApplication
from view.calculator import Calculator

if __name__ == '__main__':

    app = QApplication([])

    calculator = Calculator()

    app.exec_()