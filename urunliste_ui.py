# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urunliste.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(313, 299)
        self.sepettablo = QtWidgets.QTableWidget(Form)
        self.sepettablo.setGeometry(QtCore.QRect(0, 0, 311, 291))
        self.sepettablo.setObjectName("sepettablo")
        self.sepettablo.setColumnCount(3)
        self.sepettablo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sepettablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sepettablo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sepettablo.setHorizontalHeaderItem(2, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ürün Listesi"))
        item = self.sepettablo.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ürün"))
        item = self.sepettablo.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Stok"))
        item = self.sepettablo.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Fiyat"))