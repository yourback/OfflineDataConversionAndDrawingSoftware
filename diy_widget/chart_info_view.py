import numpy as np
from PyQt5.QtWidgets import QWidget, QVBoxLayout

# 自定义控件
# 图像 + 信息栏（同一时刻每条线的数值 和 一条或者多条数据最大最小，插值，周期，微分，积分，平均值）
from diy_widget.chart_view import Chart


class ItemChartView(QWidget):
    def __init__(self, parent=None):
        super(ItemChartView, self).__init__(parent)
        self.main_layout = None
        self.init_ui()

    def init_ui(self):
        # 新建垂直布局
        self.main_layout = QVBoxLayout(self)
        # 新建折线图表对象
        c = Chart([np.random.normal(size=100) * 1e0, ])
        # 新建下方信息栏对象
