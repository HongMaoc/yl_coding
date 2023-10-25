import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton


class FormulaEvaluatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('公式计算器')  # 设置窗口标题
        self.setGeometry(0, 0, 800, 600)  # 设置窗口尺寸
        self.center()  # 屏幕居中显示

        main_layout = QVBoxLayout()  # 主垂直布局

        # 上部分：输入if公式
        self.formula_input = QTextEdit()  # 创建文本输入框
        self.formula_input.setPlaceholderText('在这里输入JavaScript的if公式')  # 设置占位文本
        main_layout.addWidget(self.formula_input)  # 将输入框添加到主布局

        # 中部分：输入变量替换值
        self.variables_input = QTextEdit()  # 创建文本输入框
        self.variables_input.setPlaceholderText('输入变量替换值，例如: a=10, b=5')  # 设置占位文本
        main_layout.addWidget(self.variables_input)  # 将输入框添加到主布局

        # 提交按钮
        submit_button = QPushButton('提交')  # 创建提交按钮
        submit_button.clicked.connect(self.calculate_formula)  # 连接按钮点击事件到计算方法
        main_layout.addWidget(submit_button)  # 将按钮添加到主布局

        # 底部：显示替换后的公式和结果
        self.result_display = QTextEdit()  # 创建文本显示框
        self.result_display.setPlaceholderText('这里显示替换后的if公式和结果')  # 设置占位文本
        self.result_display.setReadOnly(True)  # 设置为只读
        main_layout.addWidget(self.result_display)  # 将文本显示框添加到主布局

        self.setLayout(main_layout)  # 设置主布局

    def center(self):
        # 屏幕居中
        frame_geometry = self.frameGeometry()
        center_point = QApplication.desktop().screenGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def calculate_formula(self):
        # 获取输入的if公式和变量替换值
        formula = self.formula_input.toPlainText()
        variable_values = self.variables_input.toPlainText()
        variables = {}
        try:
            # 执行变量替换值
            exec(variable_values, variables)
            # 计算if公式结果
            result = eval(formula, variables)
            self.result_display.setPlainText(f'Result: {result}')  # 显示结果
        except Exception as e:
            self.result_display.setPlainText(f'Error: {str(e)}')  # 显示错误消息


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormulaEvaluatorApp()
    window.show()
    sys.exit(app.exec_())
