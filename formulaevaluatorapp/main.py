import sys
from PyQt5.QtWidgets import QApplication
from InputWindow import FormulaEvaluatorApp
# from ResultWindow import ResultWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormulaEvaluatorApp()
    window.show()
    sys.exit(app.exec_())

