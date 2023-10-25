# result_window.py

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit


class ResultWindow(QWidget):
    def __init__(self):
        super().__init__()
        # super().__init()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # 底部：显示替换后的公式和结果
        self.result_display = QTextEdit()
        self.result_display.setPlaceholderText('这里显示替换后的if公式和结果')
        self.result_display.setReadOnly(True)
        main_layout.addWidget(self.result_display)
        self.move(800, 0)  # 设置子窗口在 x=800, y=0 的位置

        self.setLayout(main_layout)

    def process_data(self, formula, variable_values):
        variables = {}
        try:
            # 执行变量替换值
            exec(variable_values, variables)
            # 计算if公式结果
            result = eval(formula, variables)
            self.result_display.setPlainText(f'Result: {result}')
        except Exception as e:
            self.result_display.setPlainText(f'错误: {str(e)}')

    # def closeEvent(self, event):
    #     # 关闭子窗口时一起关闭主窗口
    #     event.accept()
