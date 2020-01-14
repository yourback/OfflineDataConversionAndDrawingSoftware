from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout

from clac_module.listcalc import DataCleaner
from diy_widget.chart_info_view import ItemChartView


class ChartView(QtWidgets.QWidget):
    def __init__(self, title, parent=None):
        super(ChartView, self).__init__(parent)
        # self.setupUi(self)
        self.chart_array = title
        self.setWindowTitle(title)
        # 子窗口在最上面
        self.setWindowModality(Qt.ApplicationModal)
        # 新建竖向布局
        self.main_layout = QVBoxLayout(self)
        # 设置布局
        self.init_ui()

    def init_ui(self):
        # 从文档拿到数据
        dc = DataCleaner()
        for chart_num in self.chart_array:
            # 拿到对应图形数据
            data = dc.get_chart_data(chart_num)
            # print("%s的数据为：%s" % (chart_num, data))
            ipv = ItemChartView(chart_num, data)
            self.main_layout.addWidget(ipv)
        self.setLayout(self.main_layout)
        self.showMaximized()
