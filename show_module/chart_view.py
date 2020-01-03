# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chart_view.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 130, 72, 15))
        self.label.setObjectName("label")
        self.widget = ItemChartView(Form)
        self.widget.setGeometry(QtCore.QRect(50, 30, 120, 80))
        self.widget.setObjectName("widget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "图像"))


from diy_widget.chart_info_view import ItemChartView
