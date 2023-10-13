class EvaluationScore:

    def __init__(self, method_name, *args):
        self.method_name = method_name
        self.result = None
        self.calculate_score(*args)

    def calculate_score(self, *args):
        if self.method_name:
            method = getattr(self, self.method_name, None)
            if method:
                self.result = method(*args)

    @staticmethod
    def calculate_ck_value(CK, MB):  # 肌酸激酶
        """
        # 肌酸激酶
        :param MB: 肌酸激酶－MB同工酶
        :param CK: 肌酸激酶
        :return: 返回计算结果
        """
        # print(MB / CK)
        if (MB / CK) < 0.0006:
            return '>>> 0 分'
        elif (MB / CK) >= 0.06:
            return '>>> 1 分'
        else:
            print('不满足自动打分----切换手动打分')

    # 人类乳头瘤
    @staticmethod
    def calculate_hpv_risk(hpv6, hpv11, hpv16, hpv18, hpv26, hpv31, hpv33, hpv35, hpv39, hpv45, hpv51, hpv52, hpv53,
                           hpv56, hpv58, hpv59, hpv66, hpv68, hpv73, hpv81, hpv82):
        """

        :param hpv6: (低危型)
        :param hpv11: (低危型)
        :param hpv16: (高危型)
        :param hpv18: (高危型)
        :param hpv26: (高危型)
        :param hpv31: (高危型)
        :param hpv33: (高危型)
        :param hpv35: (高危型)
        :param hpv39: (高危型)
        :param hpv45: (高危型)
        :param hpv51: (高危型)
        :param hpv52: (高危型)
        :param hpv53: (中危型)
        :param hpv56: (高危型)
        :param hpv58: (高危型)
        :param hpv59: (高危型)
        :param hpv66: (中危型)
        :param hpv68: (高危型)
        :param hpv73: (中危型)
        :param hpv81: (低危型)
        :param hpv82: (中危型)
        :return: 返回计算结果
        """
        results = ['hpv16', 'hpv18', 'hpv52', 'hpv31', 'hpv33', 'hpv58', 'hpv35', 'hpv39', 'hpv45', 'hpv51', 'hpv56',
                   'hpv59', 'hpv68']
        # 初始化统计
        positiveCount = 0;
        # 遍历列表中的元素，根据元素的值进行分类统计
        for result in results:
            if '阳性' in result:
                positiveCount += 1
            elif '弱阳性' in result:
                positiveCount += 1
            elif '+' in result:
                positiveCount += 1
            elif '±' in result:
                positiveCount += 1
        # 计算公式
        if (hpv6 == '阴性' or hpv6 == '-') and (hpv11 == '阴性' or hpv11 == '-') and (
                hpv16 == '阴性' or hpv16 == '-') and (hpv18 == '阴性' or hpv18 == '-') and (
                hpv26 == '阴性' or hpv26 == '-') and (hpv31 == '阴性' or hpv31 == '-') and (
                hpv33 == '阴性' or hpv33 == '-') and (hpv35 == '阴性' or hpv35 == '-') and (
                hpv39 == '阴性' or hpv39 == '-') and (hpv45 == '阴性' or hpv45 == '-') and (
                hpv51 == '阴性' or hpv51 == '-') and (hpv52 == '阴性' or hpv52 == '-') and (
                hpv53 == '阴性' or hpv53 == '-') and (hpv56 == '阴性' or hpv56 == '-') and (
                hpv58 == '阴性' or hpv58 == '-') and (hpv59 == '阴性' or hpv59 == '-') and (
                hpv66 == '阴性' or hpv66 == '-') and (hpv68 == '阴性' or hpv68 == '-') and (
                hpv73 == '阴性' or hpv73 == '-') and (hpv81 == '阴性' or hpv81 == '-') and (
                hpv82 == '阴性' or hpv82 == '-'):
            return '>>> 0 分'
        elif (hpv6 == '阳性' or hpv6 == '弱阳性' or hpv6 == '+' or hpv6 == '±') or (
                hpv11 == '阳性' or hpv11 == '弱阳性' or hpv11 == '+' or hpv11 == '±') or (
                hpv81 == '阳性' or hpv81 == '弱阳性' or hpv81 == '+' or hpv81 == '±') and (
                hpv26 == '阴性' or hpv26 == '-') and (hpv53 == '阴性' or hpv53 == '-') and (
                hpv66 == '阴性' or hpv66 == '-') and (hpv73 == '阴性' or hpv73 == '-') and (
                hpv82 == '阴性' or hpv82 == '-') and (hpv16 == '阴性' or hpv16 == '-') and (
                hpv18 == '阴性' or hpv18 == '-') and (hpv31 == '阴性' or hpv31 == '-') and (
                hpv33 == '阴性' or hpv33 == '-') and (hpv52 == '阴性' or hpv52 == '-') and (
                hpv58 == '阴性' or hpv58 == '-') and (hpv35 == '阴性' or hpv35 == '-') and (
                hpv39 == '阴性' or hpv39 == '-') and (hpv45 == '阴性' or hpv45 == '-') and (
                hpv51 == '阴性' or hpv51 == '-') and (hpv56 == '阴性' or hpv56 == '-') and (
                hpv59 == '阴性' or hpv59 == '-') and (hpv68 == '阴性' or hpv68 == '-'):
            return '>>> 1 分'
        elif (hpv26 == '阳性' or hpv26 == '弱阳性' or hpv26 == '+' or hpv26 == '±') or (
                hpv53 == '阳性' or hpv53 == '弱阳性' or hpv53 == '+' or hpv53 == '±') or (
                hpv66 == '阳性' or hpv66 == '弱阳性' or hpv66 == '+' or hpv66 == '±') or (
                hpv73 == '阳性' or hpv73 == '弱阳性' or hpv73 == '+' or hpv73 == '±') or (
                hpv82 == '阳性' or hpv82 == '弱阳性' or hpv82 == '+' or hpv82 == '±') and (
                hpv16 == '阴性' or hpv16 == '-') and (hpv18 == '阴性' or hpv18 == '-') and (
                hpv31 == '阴性' or hpv31 == '-') and (hpv33 == '阴性' or hpv33 == '-') and (
                hpv52 == '阴性' or hpv52 == '-') and (hpv58 == '阴性' or hpv58 == '-') and (
                hpv35 == '阴性' or hpv35 == '-') and (hpv39 == '阴性' or hpv39 == '-') and (
                hpv45 == '阴性' or hpv45 == '-') and (hpv51 == '阴性' or hpv51 == '-') and (
                hpv56 == '阴性' or hpv56 == '-') and (hpv59 == '阴性' or hpv59 == '-') and (
                hpv68 == '阴性' or hpv68 == '-'):
            return '>>> 2 分'
        elif (hpv16 == '阳性' or hpv16 == '弱阳性' or hpv16 == '+' or hpv16 == '±') or (
                hpv18 == '阳性' or hpv18 == '弱阳性' or hpv18 == '+' or hpv18 == '±') or (
                hpv31 == '阳性' or hpv31 == '弱阳性' or hpv31 == '+' or hpv31 == '±') or (
                hpv33 == '阳性' or hpv33 == '弱阳性' or hpv33 == '+' or hpv33 == '±') or (
                hpv52 == '阳性' or hpv52 == '弱阳性' or hpv52 == '+' or hpv52 == '±') or (
                hpv58 == '阳性' or hpv58 == '弱阳性' or hpv58 == '+' or hpv58 == '±') or (
                hpv35 == '阳性' or hpv35 == '弱阳性' or hpv35 == '+' or hpv35 == '±') or (
                hpv39 == '阳性' or hpv39 == '弱阳性' or hpv39 == '+' or hpv39 == '±') or (
                hpv45 == '阳性' or hpv45 == '弱阳性' or hpv45 == '+' or hpv45 == '±') or (
                hpv51 == '阳性' or hpv51 == '弱阳性' or hpv51 == '+' or hpv51 == '±') or (
                hpv56 == '阳性' or hpv56 == '弱阳性' or hpv56 == '+' or hpv56 == '±') or (
                hpv59 == '阳性' or hpv59 == '弱阳性' or hpv59 == '+' or hpv59 == '±') or (
                hpv68 == '阳性' or hpv68 == '弱阳性' or hpv68 == '+' or hpv68 == '±'):
            return '>>> 3 分'
        elif positiveCount >= 2:
            return '>>> 4 分'
        else:
            print('不满足自动打分----切换手动打分')

    @staticmethod
    def interpret_result(surface_antigen, surface_antibody, e_antigen, e_antibody, core_antibody):  # 乙型肝炎组合
        """

        :param surface_antigen: 乙型肝炎病毒表面抗原定量值
        :param surface_antibody: 乙型肝炎病毒表面抗体定量值
        :param e_antigen: 乙型肝炎病毒e抗原定量值
        :param e_antibody: 乙型肝炎病毒e抗体定量值
        :param core_antibody: 乙型肝炎病毒核心抗体定量值
        :return: 返回计算结果
        """

        if (0 <= surface_antigen <= 0.05) and (0 <= surface_antibody <= 10) and (0 <= e_antigen <= 0.1) and (
                0 <= e_antibody <= 0.15) and (0 <= core_antibody <= 0.35):
            return '>>> 0 分'
        elif surface_antigen <= 0.05 and surface_antibody >= 100:
            return '>>> 1 分'
        elif surface_antigen <= 0.05 and (10 < surface_antibody < 100):
            return '>>> 2 分'
        elif surface_antigen <= 0.05 and surface_antibody <= 10:
            return '>>> 3 分'
        elif surface_antigen > 0.05:
            return '>>> 4 分'
        else:
            print('不满足自动打分----切换手动打分')

    @staticmethod
    def thyroid_function(tsh, ft3, ft4):  # 甲状腺游离三项指标组合

        """
        计算和解释甲状腺功能相关指标。

        :param tsh: 促甲状腺激素（TSH）的值。
        :param ft3: 游离三碘甲状腺原氨酸（FT3）的值。
        :param ft4: 游离甲状腺素（FT4）的值。
        :return: 甲状腺功能评估结果。
        """

        if (2.0 <= ft3 <= 4.4) and (0.93 <= ft4 <= 1.7) and (0.27 <= tsh <= 4.2):
            return '>>> 0 分'
        elif ((2.0 <= ft3 <= 4.4) and (0.93 <= ft4 <= 1.7) and tsh < 0.27) or (
                (2.0 <= ft3 <= 4.4) and (0.93 <= ft4 <= 1.7) and tsh >= 4.2):
            return '>>> 1 分'
        elif (tsh <= 0.26 and (ft4 >= 1.7 or 0.93 <= ft4 <= 1.7) and ft3 >= 4.4) or (
                tsh >= 4.2 and 0.93 >= ft4 <= 1.7) and (ft3 <= 2.0 or 2.0 <= ft3 <= 4.4):
            return '>>> 2 分'
        else:
            print('不满足自动打分----切换手动打分')

    @staticmethod
    def calculate_microalbumin(macr):  # 尿微量白蛋白/尿肌酐比值
        """

        :param macr: 接收尿微量白蛋白/尿肌酐比值检测结果值
        :return: 返回计算结果
        """
        if macr < 30 or macr == 3.4:
            return '>>> 0 分'
        elif 30 <= macr < 100:
            return '>>> 1 分'
        elif 100 <= macr < 200:
            return '>>> 2 分'
        elif 200 <= macr < 250:
            return '>>> 3 分'
        elif 250 <= macr < 300:
            return '>>> 4 分'
        elif macr >= 300:
            return '>>> 5 分'


# 实例化对象时传递方法名和参数
# score = EvaluationScore('calculate_ck_value', 209, 1.3)

# score = EvaluationScore('calculate_hpv_risk', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补', '报告后补')
score = EvaluationScore('interpret_result', 0.05, 7.58, 0.05, 0.1, 0.84)
# score = EvaluationScore('thyroid_function', 2.32, 3.73, 1.22)
# score = EvaluationScore('calculate_microalbumin', 3.4)
print(score.result)  # 打印计算结果
