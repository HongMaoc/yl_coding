import pandas as pd


class EvaluationScorer:
    def __init__(self, name_column, value, grade_columns):
        self.name_column = name_column
        self.value = value
        self.grade_columns = grade_columns
        self.file_path = "E:\dev_coding\yi_code\makingtable.xlsx"  # 表格文件路径

    def calculate_score(self):
        try:
            # 读取Excel表格
            data = pd.read_excel(self.file_path)

            # 判断是否存在指定的列
            if self.name_column not in data.columns:
                return "指定的列名不存在"

            # 初始化评分
            score = 0

            # 根据名称列匹配数据
            matched_data = data[data[self.name_column] == self.value]

            # 如果匹配到多行数据，选择第一行
            if len(matched_data) > 0:
                matched_row = matched_data.iloc[0]

                # 根据评分区间列获取相应的分数
                for grade_col in self.grade_columns:
                    score += matched_row.get(grade_col, 0)

                return score
            else:
                return "未找到匹配的数据"
        except Exception as e:
            return str(e)


# 实例化对象
scorer = EvaluationScorer("name", "SampleName", ["grade_score0", "grade_score1", "grade_score2"])

# 调用方法进行评分
result = scorer.calculate_score()
print("评分结果:", result)
