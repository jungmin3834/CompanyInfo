import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QDialog
from PyQt5.QtGui import QIcon


class Ui_Dialog(object):
    def __init__(self , Dialog):
        super().__init__()
        self.Dialog = Dialog
        self.setupUi(Dialog)
        self.btn_accept.clicked.connect(self.click_accept)
        self.btn_reject.clicked.connect(Dialog.close)
        #self.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 152)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 351, 111))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(80, 40, 251, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lb_delete = QtWidgets.QLabel(self.groupBox)
        self.lb_delete.setGeometry(QtCore.QRect(10, 40, 61, 21))
        self.lb_delete.setObjectName("lb_delete")
        self.btn_accept = QtWidgets.QPushButton(self.groupBox)
        self.btn_accept.setGeometry(QtCore.QRect(180, 80, 75, 23))
        self.btn_accept.setObjectName("btn_accept")
        self.btn_reject = QtWidgets.QPushButton(self.groupBox)
        self.btn_reject.setGeometry(QtCore.QRect(260, 80, 75, 23))
        self.btn_reject.setObjectName("btn_reject")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "삭제 코드 입력"))
        self.lb_delete.setText(_translate("Dialog", "삭제 코드 :"))
        self.btn_accept.setText(_translate("Dialog", "확인"))
        self.btn_reject.setText(_translate("Dialog", "취소"))

    def click_accept(self):
        self.code = self.lineEdit.text()
        self.Dialog.accept()

    def getCode(self):
        return self.code



def Ui_DeleteCode():
    dialog = QDialog()
    dialog.ui = Ui_Dialog(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    if(dialog.exec() == QDialog.Accepted):
        return dialog.ui.getCode()
    return "NULL"
