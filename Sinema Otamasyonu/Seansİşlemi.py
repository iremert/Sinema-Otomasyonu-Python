# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Seansİşlemi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Seansİşlemi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 432)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#centralwidget{border-image: url(:/arkaplan/arkaplan11.jpg);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 381, 361))
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 361, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit_2)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(40, 270, 301, 41))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 140, 261, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 50, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 70, 81, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 90, 81, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setGeometry(QtCore.QRect(100, 30, 81, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_6.setGeometry(QtCore.QRect(100, 50, 81, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_20 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_20.setGeometry(QtCore.QRect(100, 70, 81, 20))
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_19 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_19.setGeometry(QtCore.QRect(100, 90, 81, 20))
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_21 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_21.setGeometry(QtCore.QRect(190, 30, 81, 20))
        self.checkBox_21.setObjectName("checkBox_21")
        self.checkBox_22 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_22.setGeometry(QtCore.QRect(190, 50, 81, 20))
        self.checkBox_22.setObjectName("checkBox_22")
        self.checkBox_23 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_23.setGeometry(QtCore.QRect(190, 70, 81, 20))
        self.checkBox_23.setObjectName("checkBox_23")
        self.checkBox_24 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_24.setGeometry(QtCore.QRect(190, 90, 81, 20))
        self.checkBox_24.setObjectName("checkBox_24")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 320, 93, 31))
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Seans Ekle"))
        self.groupBox.setTitle(_translate("MainWindow", "Seans Ekle"))
        self.label_3.setText(_translate("MainWindow", "Film Adı:"))
        self.label_8.setText(_translate("MainWindow", "Tarih:"))
        self.label.setText(_translate("MainWindow", "Salon:"))
        self.pushButton.setText(_translate("MainWindow", "Seansları Ekle"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Seanslar"))
        self.checkBox.setText(_translate("MainWindow", "10.00"))
        self.checkBox_2.setText(_translate("MainWindow", "13.00"))
        self.checkBox_3.setText(_translate("MainWindow", "16.00"))
        self.checkBox_4.setText(_translate("MainWindow", "19.00"))
        self.checkBox_5.setText(_translate("MainWindow", "11.00"))
        self.checkBox_6.setText(_translate("MainWindow", "14.00"))
        self.checkBox_20.setText(_translate("MainWindow", "17.00"))
        self.checkBox_19.setText(_translate("MainWindow", "20.00"))
        self.checkBox_21.setText(_translate("MainWindow", "12.00"))
        self.checkBox_22.setText(_translate("MainWindow", "15.00"))
        self.checkBox_23.setText(_translate("MainWindow", "18.00"))
        self.checkBox_24.setText(_translate("MainWindow", "21.00"))
        self.pushButton_2.setText(_translate("MainWindow", "Geri Dön"))
import anasayfa_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Seansİşlemi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
