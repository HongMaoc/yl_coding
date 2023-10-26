import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QPushButton, QWidget, QScrollArea, QSizePolicy

class FormulaEvaluatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('公式计算器')
        self.setGeometry(100, 100, 600, 360)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()

        # 上部分：输入if公式
        self.formula_input = QTextEdit()
        self.formula_input.setPlaceholderText('在这里输入JavaScript的if公式')
        main_layout.addWidget(self.formula_input)

        # 中部分：输入变量替换值
        self.variables_input = QTextEdit()
        self.variables_input.setPlaceholderText('输入变量替换值，例如: a=10, b=5')
        main_layout.addWidget(self.variables_input)

        # 提交按钮
        submit_button = QPushButton('提交')
        submit_button.clicked.connect(self.calculate_formula)
        main_layout.addWidget(submit_button)

        # 底部：显示替换后的公式和结果
        self.result_display = QTextEdit()
        self.result_display.setPlaceholderText('这里显示替换后的if公式和结果')
        self.result_display.setReadOnly(True)
        self.result_display.setFixedHeight(100)  # 设置底部展示框的高度
        self.result_scroll_area = QScrollArea()
        self.result_scroll_area.setWidget(self.result_display)
        self.result_scroll_area.setWidgetResizable(True)
        self.result_scroll_area.hide()
        main_layout.addWidget(self.result_scroll_area)

        main_widget.setLayout(main_layout)

    def calculate_formula(self):
        formula = self.formula_input.toPlainText()
        variable_values = self.variables_input.toPlainText()
        variables = {}
        try:
            exec(variable_values, variables)
            result = eval(formula, variables)
            self.result_display.append(f'替换后的公式: {formula}')
            self.result_display.append(f'计算结果: {result}')
            self.result_scroll_area.show()  # 显示底部展示框
        except Exception as e:
            self.result_display.append(f'计算出错: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormulaEvaluatorApp()
    window.show()
    sys.exit(app.exec_())
