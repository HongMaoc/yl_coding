import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QDialog
from result_window import ResultWindow  # 引入 result_window 子窗口

class InputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # 添加输入框
        self.input_text = QTextEdit(self)
        layout.addWidget(self.input_text)

        # 添加按钮，点击打开 result_window 子窗口
        open_result_button = QPushButton('打开结果窗口', self)
        open_result_button.clicked.connect(self.show_result_window)
        layout.addWidget(open_result_button)

        self.setLayout(layout)

    def show_result_window(self):
        self.result_window = ResultWindow()
        self.result_window.show()

class ResultWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # 添加结果显示框
        self.result_text = QTextEdit(self)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    input_window = InputWindow()
    input_window.setWindowTitle('输入窗口')
    input_window.show()

    sys.exit(app.exec_())
