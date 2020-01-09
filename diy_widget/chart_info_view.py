import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from diy_widget.chart_view import Chart


# 自定义控件
# 图像 + 信息栏（同一时刻每条线的数值 和 一条或者多条数据最大最小，插值，周期，微分，积分，平均值）
class ItemChartView(QWidget):
    lines_point_info_signal = pyqtSignal(tuple)
    lines_range_info_signal = pyqtSignal(tuple)

    def __init__(self, chart_num, data, parent=None):
        # print('初始化：ItemChartView')
        super(ItemChartView, self).__init__(parent)
        # 新建下方信息栏对象
        self.label_line_range = QtWidgets.QLabel()
        self.label_line_point = QtWidgets.QLabel()
        self.main_layout = None
        self.init_ui(chart_num, data)
        # 信号与槽连接
        self.lines_point_info_signal.connect(self.lines_point_info)
        self.lines_range_info_signal.connect(self.lines_range_info)

    def lines_range_info(self, info):
        # print('最小:%s' % info[0])
        # print('最大:%s' % info[1])
        # print('lines_range_info:%s' % info[2])
        # self.label_line_range.setText('你不好')
        range_str = '区间：%s-%s' % (info[0], info[1])
        for k in info[2]:
            range_str += "\n%s" % k
            range_str += '  最大值：%s' % info[2][k]["max"]
            range_str += '  最小值：%s' % info[2][k]["min"]
            range_str += '  差值：%s' % info[2][k]["diff"]
            range_str += '  平均值：%s' % info[2][k]["average"]
        self.label_line_range.setText(range_str)

    def lines_point_info(self, info):
        # print('lines_point_info')
        # print('收到发来数据为：图%s  横坐标：%s  纵坐标分别为：%s' % (info[0], info[1], info[2]))
        status_str = '横坐标：%s   ' % info[1]
        for k in info[2]:
            status_str += "%s : %s  " % (k, info[2][k])
        self.label_line_point.setText(status_str)

    def init_ui(self, chart_num, data):
        # print('ItemChartView的数据为：%s' % data)
        # 新建垂直布局
        self.main_layout = QVBoxLayout(self)
        # 新建折线图表对象
        c = Chart(chart_num, data, self.lines_point_info_signal, self.lines_range_info_signal)

        # 添加控件
        self.main_layout.addWidget(c, 1)
        self.main_layout.addWidget(self.label_line_point, 0)
        self.main_layout.addWidget(self.label_line_range, 0)

        # 设置总布局
        self.setLayout(self.main_layout)
