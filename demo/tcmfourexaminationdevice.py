import re


class HealthEvaluator:
    def __init__(self):
        self.data_pattern = re.compile(r'(\D+)(\d+\.\d+)')  # 正则表达式模式，用于匹配体质名称和数值
        self.consum = {
            'constitution': {},  # 存储体质数据的字典，包括前置体质和后置体质
            'substitution': {}
        }

    def parse_data(self, data_str):
        data_dict = {}  # 用于存储解析后的体质数据的字典
        matches = self.data_pattern.findall(data_str)  # 使用正则表达式匹配数据
        for match in matches:
            name, value = match
            data_dict[name] = float(value)  # 将匹配到的数据存储到字典中
        return data_dict

    @staticmethod
    def calculate_precontype_and_postconstype(data):
        """

        :param data: 接收字典并判断有无空值，如果有赋值0后累加
        :return: 返回前置和后置体质之和结果
        """
        precontype = sum(value if value else 0 for value in data['constitution'].values())  # 计算前置体质之和
        postconstype = sum(value if value else 0 for value in data['substitution'].values())  # 计算后置体质之和
        return precontype, postconstype

    @staticmethod
    def evaluate_health_effect(precontype, postconstype, precons, postcons):
        """

        :param precontype: 前置体质之和
        :param postconstype: 后置体质之和
        :param precons: 前置平和质
        :param postcons: 后置平和质
        :return: 返回效评结论
        """

        if postcons != 0:
            return '养护有效'
        diff = round(((precontype - precons) - (postconstype - postcons)) / (precontype - precons), 2)
        # 计算前后置体质差异，并四舍五入保留两位小数
        if diff >= 0.1:
            return '养护有效'
        elif diff < -0.1:
            return '养护无效'
        else:
            return '不做认定'

    def evaluate_health(self, data_str_1, data_str_2):
        """

        :param data_str_1: 接收前置数据处理成字典并判断有无平和质，如果没有赋值0
        :param data_str_2: 接收后置数据处理成字典并判断有无平和质，如果没有赋值0
        :return:
        """
        self.consum['constitution'] = self.parse_data(data_str_1)  # 解析并存储第一组体质数据
        self.consum['substitution'] = self.parse_data(data_str_2)  # 解析并存储第二组体质数据

        for key in ['constitution', 'substitution']:
            if '平和质' not in self.consum[key]:
                self.consum[key]['平和质'] = 0  # 如果平和质数据不存在，设置为0

        precontype, postconstype = self.calculate_precontype_and_postconstype(self.consum)
        precons = self.consum['constitution']['平和质']  # 获取平和质值
        postcons = self.consum['substitution']['平和质']  # 获取平和质值

        result = self.evaluate_health_effect(precontype, postconstype, precons, postcons)  # 评估健康效果
        return result


if __name__ == '__main__':
    evaluator = HealthEvaluator()  # 创建 HealthEvaluator 类的实例
    data_str_1 = "痰湿质12.0阴虚质7.0血瘀质6.0气虚质6.0湿热质5.0特禀质4.0气郁质4.0阳虚质5.0"
    data_str_2 = "痰湿质14.0阴虚质9.0血瘀质7.0气虚质5.0湿热质6.0特禀质5.0气郁质4.0阳虚质6.0"
    result = evaluator.evaluate_health(data_str_1, data_str_2)  # 调用 evaluate_health 方法评估健康
    print(f"效评结论----{result}")  # 打印评估结果
