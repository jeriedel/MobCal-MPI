# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/josh/Downloads/GUI/gui/Mobcal.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(699, 443)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(699, 443))
        Dialog.setMaximumSize(QtCore.QSize(699, 443))
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 700, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.t1le_1 = QtWidgets.QLineEdit(self.tab_1)
        self.t1le_1.setGeometry(QtCore.QRect(160, 20, 521, 32))
        self.t1le_1.setObjectName("t1le_1")
        self.t1le_2 = QtWidgets.QLineEdit(self.tab_1)
        self.t1le_2.setGeometry(QtCore.QRect(160, 70, 521, 32))
        self.t1le_2.setToolTip("")
        self.t1le_2.setStatusTip("")
        self.t1le_2.setObjectName("t1le_2")
        self.t1le_3 = QtWidgets.QLineEdit(self.tab_1)
        self.t1le_3.setGeometry(QtCore.QRect(160, 120, 521, 32))
        self.t1le_3.setObjectName("t1le_3")
        self.t1l1 = QtWidgets.QLabel(self.tab_1)
        self.t1l1.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.t1l1.setObjectName("t1l1")
        self.t1l2 = QtWidgets.QLabel(self.tab_1)
        self.t1l2.setGeometry(QtCore.QRect(20, 70, 91, 31))
        self.t1l2.setObjectName("t1l2")
        self.t1l3 = QtWidgets.QLabel(self.tab_1)
        self.t1l3.setGeometry(QtCore.QRect(20, 120, 131, 31))
        self.t1l3.setObjectName("t1l3")
        self.t1l4 = QtWidgets.QLabel(self.tab_1)
        self.t1l4.setGeometry(QtCore.QRect(20, 170, 131, 31))
        self.t1l4.setObjectName("t1l4")
        self.t1cb1 = QtWidgets.QComboBox(self.tab_1)
        self.t1cb1.setGeometry(QtCore.QRect(160, 170, 87, 32))
        self.t1cb1.setObjectName("t1cb1")
        self.t1cb1.addItem("")
        self.t1cb1.addItem("")
        self.t1cb1.addItem("")
        self.t1l5 = QtWidgets.QLabel(self.tab_1)
        self.t1l5.setGeometry(QtCore.QRect(400, 170, 131, 31))
        self.t1l5.setObjectName("t1l5")
        self.t1sb1 = QtWidgets.QSpinBox(self.tab_1)
        self.t1sb1.setGeometry(QtCore.QRect(590, 170, 91, 32))
        self.t1sb1.setMaximum(10000)
        self.t1sb1.setProperty("value", 10)
        self.t1sb1.setObjectName("t1sb1")
        self.t1l6 = QtWidgets.QLabel(self.tab_1)
        self.t1l6.setGeometry(QtCore.QRect(400, 220, 131, 31))
        self.t1l6.setObjectName("t1l6")
        self.t1l7 = QtWidgets.QLabel(self.tab_1)
        self.t1l7.setGeometry(QtCore.QRect(400, 270, 131, 31))
        self.t1l7.setObjectName("t1l7")
        self.t1sb2 = QtWidgets.QSpinBox(self.tab_1)
        self.t1sb2.setGeometry(QtCore.QRect(590, 220, 87, 32))
        self.t1sb2.setMaximum(1000)
        self.t1sb2.setProperty("value", 48)
        self.t1sb2.setObjectName("t1sb2")
        self.t1sb3 = QtWidgets.QSpinBox(self.tab_1)
        self.t1sb3.setGeometry(QtCore.QRect(590, 270, 91, 32))
        self.t1sb3.setMaximum(10000)
        self.t1sb3.setProperty("value", 512)
        self.t1sb3.setObjectName("t1sb3")
        self.t1l8 = QtWidgets.QLabel(self.tab_1)
        self.t1l8.setGeometry(QtCore.QRect(20, 220, 131, 31))
        self.t1l8.setObjectName("t1l8")
        self.t1cb2 = QtWidgets.QComboBox(self.tab_1)
        self.t1cb2.setGeometry(QtCore.QRect(160, 220, 87, 32))
        self.t1cb2.setObjectName("t1cb2")
        self.t1cb2.addItem("")
        self.t1cb2.addItem("")
        self.t1l9 = QtWidgets.QLabel(self.tab_1)
        self.t1l9.setGeometry(QtCore.QRect(20, 270, 131, 31))
        self.t1l9.setObjectName("t1l9")
        self.t1sb4 = QtWidgets.QSpinBox(self.tab_1)
        self.t1sb4.setGeometry(QtCore.QRect(160, 270, 91, 32))
        self.t1sb4.setMaximum(10000)
        self.t1sb4.setProperty("value", 8)
        self.t1sb4.setObjectName("t1sb4")
        self.t1l10 = QtWidgets.QLabel(self.tab_1)
        self.t1l10.setGeometry(QtCore.QRect(20, 320, 131, 31))
        self.t1l10.setObjectName("t1l10")
        self.t1le_4 = QtWidgets.QLineEdit(self.tab_1)
        self.t1le_4.setGeometry(QtCore.QRect(160, 320, 521, 32))
        self.t1le_4.setObjectName("t1le_4")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.t2le_1 = QtWidgets.QLineEdit(self.tab_2)
        self.t2le_1.setGeometry(QtCore.QRect(160, 20, 411, 32))
        self.t2le_1.setObjectName("t2le_1")
        self.t2l1 = QtWidgets.QLabel(self.tab_2)
        self.t2l1.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.t2l1.setObjectName("t2l1")
        self.t2l2 = QtWidgets.QLabel(self.tab_2)
        self.t2l2.setGeometry(QtCore.QRect(20, 70, 91, 31))
        self.t2l2.setObjectName("t2l2")
        self.t2dsb1 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.t2dsb1.setGeometry(QtCore.QRect(160, 70, 71, 32))
        self.t2dsb1.setMaximum(1000000.0)
        self.t2dsb1.setProperty("value", 298.15)
        self.t2dsb1.setObjectName("t2dsb1")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 20, 88, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.t3le_1 = QtWidgets.QLineEdit(self.tab_3)
        self.t3le_1.setGeometry(QtCore.QRect(160, 20, 521, 32))
        self.t3le_1.setObjectName("t3le_1")
        self.t3l1 = QtWidgets.QLabel(self.tab_3)
        self.t3l1.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.t3l1.setObjectName("t3l1")
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(612, 410, 88, 34))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MobCal-MPI Processing Suite"))
        self.t1le_1.setPlaceholderText(_translate("Dialog", "File path for folder containing .logs to be converted to .mfj"))
        self.t1le_2.setPlaceholderText(_translate("Dialog", "(Optional) File containing a list of logs that should be converted."))
        self.t1le_3.setText(_translate("Dialog", "C:\\open3dtools\\bin\\sdf2tinkerxyz.exe "))
        self.t1le_3.setPlaceholderText(_translate("Dialog", "Directory that sdf2xyz2sdf was installed in if different from default"))
        self.t1l1.setText(_translate("Dialog", "Log Directory"))
        self.t1l2.setText(_translate("Dialog", "Log List (.csv)"))
        self.t1l3.setText(_translate("Dialog", "sdf2xyz2sdf Directory"))
        self.t1l4.setText(_translate("Dialog", "Charge"))
        self.t1cb1.setItemText(0, _translate("Dialog", "calc"))
        self.t1cb1.setItemText(1, _translate("Dialog", "equal"))
        self.t1cb1.setItemText(2, _translate("Dialog", "none"))
        self.t1l5.setText(_translate("Dialog", "Cycles"))
        self.t1l6.setText(_translate("Dialog", "Velocity Integration"))
        self.t1l7.setText(_translate("Dialog", "Impact Integration"))
        self.t1l8.setText(_translate("Dialog", "Buffer Gas"))
        self.t1cb2.setItemText(0, _translate("Dialog", "He"))
        self.t1cb2.setItemText(1, _translate("Dialog", "N2"))
        self.t1l9.setText(_translate("Dialog", "Number of Cores"))
        self.t1l10.setText(_translate("Dialog", "Temperature List"))
        self.t1le_4.setPlaceholderText(_translate("Dialog", "Comma delimited list of integer temperature(s) in Kelvin. eg. 298 or 298,400,500"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Dialog", "mfj Creator"))
        self.t2le_1.setPlaceholderText(_translate("Dialog", ".csv file containing filenames and relative Gibbs energies"))
        self.t2l1.setText(_translate("Dialog", "CSV Directory"))
        self.t2l2.setText(_translate("Dialog", "Temperature"))
        self.pushButton_2.setText(_translate("Dialog", "Select File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Energy Weighter"))
        self.t3le_1.setPlaceholderText(_translate("Dialog", "File path for folder containing .mout files"))
        self.t3l1.setText(_translate("Dialog", "mout Directory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "CCS Extractor"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
