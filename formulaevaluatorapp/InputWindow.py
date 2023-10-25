# input_window.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QApplication


class InputWindow(QWidget):
    def __init__(self, result_window):
        super().__init__()
        self.result_window = result_window
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('公式计算器')
        self.setGeometry(0, 0, 800, 600)
        self.center()

        main_layout = QVBoxLayout()

        self.formula_input = QTextEdit()
        self.formula_input.setPlaceholderText('在这里输入JavaScript的if公式')
        main_layout.addWidget(self.formula_input)

        self.variables_input = QTextEdit()
        self.variables_input.setPlaceholderText('输入变量替换值，例如: a=10, b=5')
        main_layout.addWidget(self.variables_input)

        submit_button = QPushButton('提交')
        submit_button.clicked.connect(self.submit_data)
        main_layout.addWidget(submit_button)

        self.setLayout(main_layout)

    def center(self):
        frame_geometry = self.frameGeometry()
        center_point = QApplication.desktop().screenGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def submit_data(self):
        formula = self.formula_input.toPlainText()
        variable_values = self.variables_input.toPlainText()
        self.result_window.process_data(formula, variable_values)
