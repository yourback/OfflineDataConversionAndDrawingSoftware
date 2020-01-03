from pyqtgraph import PlotWidget, np


class Chart(PlotWidget):
    def __init__(self, data):
        super(Chart, self).__init__()
        print(data)

        self.init_ui(data)

    def init_ui(self, data):
        # 循环画线
        for data_item in data:
            curve = self.plot(data_item, clickable=True)
