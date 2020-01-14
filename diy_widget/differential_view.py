from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget

from diy_widget.chart_view import Chart


class DifferentialView(QWidget):
    line_port_move = pyqtSignal(tuple)

    def __init__(self, range_info, data):
        super(DifferentialView, self).__init__()
        self.setWindowTitle(range_info)
        # 新建布局
        self.layout_v = QtWidgets.QVBoxLayout()
        self.diff_chart = None
        self.diff_info = QtWidgets.QLabel('微分数据')
        self.setWindowModality(Qt.WindowModal)
        self.init_ui(range_info, data)
        # 信号与槽的连接
        self.line_port_move.connect(self.line_move)

    def init_ui(self, range_info, data):
        # data = {'a':[1,2,3,5],'b':[2,3,4,5,6]}
        # 新建斜率图像数据
        diff = {}
        # 利用数据生成微分 （导数|斜率）
        for key in data:
            # 'a':[1,2,3,5] 求导数线
            key_diff = []
            key_data = data[key]
            for i, v in enumerate(key_data):
                if i == 0:
                    key_diff.append(0)
                    continue
                else:
                    key_diff.append(round(v - key_data[i - 1], 2))

            diff['%s微分' % key] = key_diff
            # print('%s的微分为曲线：%s' % (key, key_diff))

        # 将diff 中的数据合并到data中
        data.update(diff)

        # 生成图表，和布局
        # 图表设置
        c = Chart(range_info, data, self.line_port_move, None)
        # 布局设置
        self.layout_v.addWidget(c, 1)
        self.layout_v.addWidget(self.diff_info, 0)
        # 设置总布局
        self.setLayout(self.layout_v)

    def line_move(self, info):
        status_str = '横坐标：%s   ' % info[1]
        for k in info[2]:
            status_str += "%s : %s  " % (k, info[2][k])

        self.diff_info.setText(status_str)
