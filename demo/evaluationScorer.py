import execjs


class FormulaEvaluator:
    def __init__(self, if_formula):
        self.if_formula = if_formula

    def evaluate(self, context):
        # 替换公式中的变量
        for key, value in context.items():
            self.if_formula = self.if_formula.replace(key, str(value))

        if self.if_formula != '':
            # 执行替换后的公式
            result = self.if_formula
            return result
        else:
            return '公式不能为空'

    @staticmethod
    def execute_javascript(result):
        try:
            # 创建一个JavaScript环境
            ctx = execjs.compile(result)

            # 执行JavaScript代码
            results = ctx.call("main")
            if results:
                print(f"{results} 分")
            else:
                print('手动打分')

        except Exception as e:
            return str(e)


# 示例用法
if_formula = 'if ( 性别 == "男" && [71:YTB] < 0.85 ) return 0; else if ( 性别 == "女" && [71:YTB] < 0.8 ) return 0;else if ( ( 性别 == "男" && [71:YTB] >= 0.85 && [71:YTB] < 0.89 ) || ( 性别 == "女" && [71:YTB] >= 0.8 && [71:YTB] < 0.84 ) ) return 1;else if ( ( 性别 == "男" && [71:YTB] >= 0.89 && [71:YTB] < 0.92 ) || ( 性别 == "女" && [71:YTB] >= 0.84 && [71:YTB] < 0.87 ) ) return 2;else if ( ( 性别 == "男" && [71:YTB] >= 0.92 && [71:YTB] < 0.95 ) || ( 性别 == "女" && [71:YTB] >= 0.87 && [71:YTB] < 0.9 ) ) return 3;else if ( ( 性别 == "男" && [71:YTB] >= 0.95 && [71:YTB] < 1 ) || ( 性别 == "女" && [71:YTB] >= 0.9 && [71:YTB] < 0.95 ) ) return 4;else if ( ( 性别 == "男" && [71:YTB] >= 1 ) || ( 性别 == "女" && [71:YTB] >= 0.95 ) ) return 5;'
context = {"性别": '\"女\"', "[71:YTB]": 0.91}

evaluator = FormulaEvaluator(if_formula)
result = evaluator.evaluate(context)
evaluator.execute_javascript(result)
