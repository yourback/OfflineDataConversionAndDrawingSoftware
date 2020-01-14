import math

import pyqtgraph as pg
from pyqtgraph import PlotWidget

from clac_module.rangecalc import get_range_values

colors_list = ['r', 'y', 'b', 'g', 'ro', 'yo', 'bo', 'go']

# 范围线需要具体取值的 LD,  RD, RU ,LU, k_R ,K_L ,LU-LD, RD-RU
need_range_data_list = ['data_LD', 'data_RD', 'data_RU', 'data_LU', 'data_K_R', 'data_K_L', 'data_LU_LD', 'data_RD_RU']


class Chart(PlotWidget):
    def __init__(self, chart_num, data, lines_point_info_signal, lines_range_info_signal):
        super(Chart, self).__init__()
        # 获得信号
        self.lines_point_info_signal = lines_point_info_signal
        self.lines_range_info_signal = lines_range_info_signal
        # 图几
        self.chart_type = chart_num
        # 数据
        self.chart_data = data
        # print("数据格式：%s" % data)
        self.single_line = pg.InfiniteLine(angle=90, movable=True)
        # 如果是微分图像 则不显示区间线
        self.range_line = pg.LinearRegionItem([10, 30], movable=True)
        self.setTitle("图%s" % chart_num)
        self.init_ui()
        self.start_move()

    def start_move(self):
        # 发送两个信号
        # self.single_line_moved()
        # self.range_line_moved()
        self.single_line.setValue(1)
        self.range_line.setRegion((10, 20))

    def init_ui(self):
        # 坐标轴信息设置
        self.setLabel(axis='left', text='数值')
        self.setLabel(axis='bottom', text='时间')
        # 标题
        self.addLegend(size=(130, 50))
        # 加竖线
        self.addItem(self.single_line)
        # 竖线移动监听
        self.single_line.sigPositionChangeFinished.connect(self.single_line_moved)
        if '-' not in self.chart_type:
            # 加区间
            self.addItem(self.range_line)
            # 区间的监听
            self.range_line.sigRegionChangeFinished.connect(self.range_line_moved)

        # 循环画线
        for index, data_item in enumerate(self.chart_data):
            # 颜色
            current_color = colors_list[index]
            if 'o' in current_color:
                curve = self.plot(self.chart_data[data_item], clickable=True, pen=current_color[0], name=data_item,
                                  symbolBrush=current_color[0])
            else:
                curve = self.plot(self.chart_data[data_item], clickable=True, pen=current_color[0], name=data_item)

    # 单根线移动完成
    def single_line_moved(self):
        print('单根移动')
        index = int(self.single_line.value())
        self.single_line.setValue(index)
        line_key_value = {}
        for key in self.chart_data:
            if index > len(self.chart_data[key]):
                index = len(self.chart_data[key]) - 1
            line_key_value[key] = self.chart_data[key][index]

        emit_data = self.chart_type, index, line_key_value
        self.lines_point_info_signal.emit(emit_data)

    # 区间改变完成
    def range_line_moved(self):
        print('区间重新移动')
        region = self.range_line.getRegion()
        # print('最小:%s   %s' % (region[0], round(region[0])))
        # print('最大:%s   %s' % (region[1], round(region[1])))
        # 区间——max
        max_index = math.floor(region[1])
        # 区间——min
        min_index = math.ceil(region[0])
        # print('最小值：%s' % min_index)
        # print('最大值：%s' % max_index)
        # 处理完的数据集合
        cleaned_chart_data = {}
        # 区间内数据
        data_in_range = {}
        for key in self.chart_data:
            if key in need_range_data_list:
                # print('key:%s  value:%s' % (key, self.chart_data))
                # 数据基础
                base_data = self.chart_data[key][min_index:max_index + 1]
                # 区间内数据
                data_in_range[key] = base_data
                if not base_data:
                    # print('为空')
                    return
                # 获得区间内所有数据
                range_values = get_range_values(base_data)
                # 添加到最终显示结果
                cleaned_chart_data[key] = range_values
        # 发送信号
        # print(cleaned_chart_data)
        self.lines_range_info_signal.emit((min_index, max_index, cleaned_chart_data, data_in_range))
