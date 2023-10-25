# result_window.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit


class ResultWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.setWindowTitle('公式计算器')
        self.setGeometry(800, 800, 400, 200)
        self.result_display = QTextEdit()
        self.result_display.setPlaceholderText('这里显示替换后的if公式和结果')
        self.result_display.setReadOnly(True)
        main_layout.addWidget(self.result_display)

        self.setLayout(main_layout)

    def process_data(self, formula, variable_values):
        variables = {}
        try:
            exec(variable_values, variables)
            result = eval(formula, variables)
            self.result_display.setPlainText(f'Result: {result}')
        except Exception as e:
            self.result_display.setPlainText(f'Error: {str(e)}')
