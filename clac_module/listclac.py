from data_module.get_source_file import *
import numpy as np


class DataCleaner(object):

    def __init__(self):
        # 图1数据源
        self.data_LD = []
        self.data_I = []
        self.data_LU = []
        self.data_T = []

        # 图2数据源
        self.data_RD = []
        self.data_RU = []

        # 图3数据源
        self.data_K_R = []
        self.data_K_L = []
        self.data_J = []

        # 图4数据源
        self.data_LU_LD = []
        self.data_RD_RU = []
        self.data_Q = []

        # 图5数据源
        self.data_K = []
        self.data_P = []
        self.data_R = []
        self.data_S = []

    def single_line_cleaning(self, one_line):
        end = one_line.index(" 0D 0A")
        start = 1
        line_result = one_line[start:end]
        item_data_list = line_result.split(" ")
        # print(item_data_list)
        return self.__get_datas(item_data_list)

    def get_item_data(self, data, i):
        """
        需要计算的单数据生成
        :param data:
        :param i:
        :return:
        """
        return (int(data[i], 16) << 8 + int(data[i + 1], 16)) / 100

    def get_item_single_data(self, data, i):
        """
        简单的单数据生成
        :param i:
        :return:
        """
        return int(data[i], 16)

    def __get_datas(self, data):
        """
        多种单数据生成
        :param data:
        :return:
        """
        LD = self.get_item_data(data, 0)
        LU = self.get_item_data(data, 2)
        RD = self.get_item_data(data, 4)
        RU = self.get_item_data(data, 6)
        K_R = self.get_item_data(data, 10)
        K_L = self.get_item_data(data, 12)

        I = self.get_item_single_data(data, 8)
        T = self.get_item_single_data(data, 19)
        J = self.get_item_single_data(data, 9)
        Q = self.get_item_single_data(data, 16) / 50
        K = self.get_item_single_data(data, 16)
        P = self.get_item_single_data(data, 16) / 10
        R = self.get_item_single_data(data, 17)
        S = self.get_item_single_data(data, 18)

        return LD, LU, RD, RU, K_R, K_L, I, T, J, Q, K, P, R, S

    def read_data(self):
        source_data = file_read_lines()
        for line_str in source_data:
            cleaned_data = self.single_line_cleaning(line_str)
            # print(cleaned_data)
            # LD, LU, RD, RU, K_R, K_L, I, T, J, Q, K, P, R, S
            self.data_LD.append(cleaned_data[0])
            self.data_LU.append(cleaned_data[1])
            self.data_RD.append(cleaned_data[2])
            self.data_RU.append(cleaned_data[3])
            self.data_K_R.append(cleaned_data[4])
            self.data_K_L.append(cleaned_data[5])
            self.data_I.append(cleaned_data[6])
            self.data_T.append(cleaned_data[7])
            self.data_J.append(cleaned_data[8])
            self.data_Q.append(cleaned_data[9])
            self.data_K.append(cleaned_data[10])
            self.data_P.append(cleaned_data[11])
            self.data_R.append(cleaned_data[12])
            self.data_S.append(cleaned_data[13])

            self.data_LU_LD.append(cleaned_data[1] - cleaned_data[0])
            self.data_RD_RU.append(cleaned_data[2] - cleaned_data[3])

    def get_chart_data(self, chart_num):
        # 读文件
        self.read_data()

        # print("data_LD:%s" % self.data_LD)
        # print("data_LU:%s" % self.data_LU)
        # print("data_RD:%s" % self.data_RD)
        # print("data_K_R:%s" % self.data_K_R)
        # print("data_K_L:%s" % self.data_K_L)
        # print("data_I:%s" % self.data_I)
        # print("data_T:%s" % self.data_T)
        # print("data_J:%s" % self.data_J)
        # print("data_Q:%s" % self.data_Q)
        # print("data_K:%s" % self.data_K)
        # print("data_P:%s" % self.data_P)
        # print("data_R:%s" % self.data_R)
        # print("data_S:%s" % self.data_S)

        if chart_num == '1':
            # 返回图1 所有需要的数据
            return {'data_LD': self.data_LD,
                    'data_I': self.data_I,
                    'data_LU': self.data_LU,
                    'data_T': self.data_T, }
        elif chart_num == '2':
            # 返回图2 所有需要的数据
            return {'data_RD': self.data_RD,
                    'data_I': self.data_I,
                    'data_RU': self.data_RU,
                    'data_T': self.data_T, }
        elif chart_num == '3':
            return {'data_RD': self.data_K_R,
                    'data_K_L': self.data_K_L,
                    'data_I': self.data_I,
                    'data_T': self.data_T,
                    'data_J': self.data_J, }
        elif chart_num == '4':
            return {'data_LU_LD': self.data_LU_LD,
                    'data_RD_RU': self.data_RD_RU,
                    'data_K_R': self.data_K_R,
                    'data_K_L': self.data_K_L,
                    'data_I': self.data_I,
                    'data_T': self.data_T,
                    'data_J': self.data_J,
                    'data_Q': self.data_Q, }
        elif chart_num == '5':
            return {'data_K': self.data_K,
                    'data_P': self.data_P,
                    'data_R': self.data_R,
                    'data_S': self.data_S, }


if __name__ == '__main__':
    dc = DataCleaner()
    m = dc.get_chart_data("1")
    for key in m:
        print(key + ':' + m[key].__str__())
