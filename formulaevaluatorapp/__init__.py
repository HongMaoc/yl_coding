import sys
from PyQt5.QtWidgets import QApplication
from InputWindow import InputWindow
from ResultWindow import ResultWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    result_window = ResultWindow()
    input_window = InputWindow(result_window)

    input_window.show()
    result_window.show()

    sys.exit(app.exec_())
