import sys

import serial.tools.list_ports
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMessageBox

from show_module.chart_view_manager import ChartView
from show_module.main_view import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 显示图像按钮
    show_chart_signal = pyqtSignal(str)
    # 清空已经选择的cb按钮
    clear_cb_signal = pyqtSignal()
    # 发送信息
    send_signal = pyqtSignal(str)

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()

        self.ser = serial.Serial()

    def init_ui(self):
        self.bind_slot2signal()
        self.click_listener()
        self.cbb_port_init()
        # 发送不可用
        self.set_send_layout_status(False)

    def click_listener(self):
        """
        按钮点击后触发信号
        :return:
        """
        self.btn_show_chart.clicked.connect(self.emit_btn_show_chart_click)
        self.btn_clear_cb.clicked.connect(self.emit_btn_clear_cb_click)
        self.btn_send.clicked.connect(self.emit_btn_send_click)

    def bind_slot2signal(self):
        """
        # 信号与槽子绑定
        :return:
        """
        # 显示折线图
        self.show_chart_signal.connect(self.show_chart)
        # 清空选择cb
        self.clear_cb_signal.connect(self.clear_cb)
        # 发送
        self.send_signal.connect(self.send_msg)

    def show_chart(self, str):
        self.cv = ChartView(str)
        self.cv.show()

    def send_msg(self, msg):
        print('发送信息：%s' % msg)

    def clear_cb(self):
        self.cb_1.setCheckState(False)
        self.cb_2.setCheckState(False)
        self.cb_3.setCheckState(False)
        self.cb_4.setCheckState(False)
        self.cb_5.setCheckState(False)

    def emit_btn_clear_cb_click(self):
        """
        清空按钮触发
        :return:
        """
        self.clear_cb_signal.emit()

    def emit_btn_show_chart_click(self):
        """
        点击按钮触发
        :return:
        """
        # 查看5个cb选中了那几个
        str = ''
        if self.cb_1.isChecked():
            str += "1"

        if self.cb_2.isChecked():
            str += "2"

        if self.cb_3.isChecked():
            str += "3"

        if self.cb_4.isChecked():
            str += "4"

        if self.cb_5.isChecked():
            str += "5"

        if not str:
            QMessageBox.warning(self, '警告', '请选择', QMessageBox.Yes, QMessageBox.Yes)
            return
        self.show_chart_signal.emit(str)

    def emit_btn_send_click(self):
        """
        发送按钮触发
        :return:
        """
        msg = self.et_send_msg.text()
        if not msg:
            QMessageBox.warning(self, '警告', '请输入发送的消息')
            return
        self.send_signal.emit(msg)

    @pyqtSlot()
    def on_btn_refresh_com_clicked(self):
        self.cbb_port_init()

    @pyqtSlot()
    def on_btn_open_port_clicked(self):
        if self.btn_open_port.text() == '打开串口':
            # print('打开串口')
            # 打开串口逻辑
            self.ser.port = self.ccb_port.currentText()
            self.ser.baudrate = self.ccb_baudrate.currentText()
            try:
                self.ser.open()
                self.set_port_settings_layout_status(False)
                self.set_send_layout_status(True)
                # 更改打开串口按钮文本
                self.btn_open_port.setText("关闭串口")
            except:
                QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
                return None
        else:
            # 关闭串口逻辑
            # print('关闭串口')
            try:
                self.ser.close()
            except:
                pass
            # 更改关闭串口按钮文本
            self.btn_open_port.setText("打开串口")
            self.set_port_settings_layout_status(True)
            self.set_send_layout_status(False)

    def set_port_settings_layout_status(self, status):
        """
        设置串口区域状态
        :param status:
        :return:
        """
        # 刷新串口不能使用救
        self.btn_refresh_com.setEnabled(status)
        # 波特率选择不能使用
        self.ccb_port.setEnabled(status)
        # 串口选择不能使用
        self.ccb_baudrate.setEnabled(status)

    def set_send_layout_status(self, status):
        """
        发送区域状态
        :param status:
        :return:
        """
        self.et_send_msg.setEnabled(status)
        self.btn_send.setEnabled(status)

    def cbb_port_init(self):
        '''
        init of combobox (select  port)
        :return:
        '''
        # data
        self.ccb_port.clear()
        # for i in range(self.cbb_port.count() + 1):
        #     print(i)
        #     print(self.cbb_port.removeItem(i))

        self.port_list = list(serial.tools.list_ports.comports())
        # print('串口列表：%s' % self.port_list)
        if len(self.port_list) != 0:
            for port in self.port_list:
                self.ccb_port.addItem(port.device)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
