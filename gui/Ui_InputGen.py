# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\Ui_InputGen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InputGen(object):
    def setupUi(self, InputGen):
        InputGen.setObjectName("InputGen")
        InputGen.resize(432, 263)
        self.centralwidget = QtWidgets.QWidget(InputGen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout.addWidget(self.label_20)
        self.lineEdit_path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.horizontalLayout.addWidget(self.lineEdit_path)
        self.btn_path = QtWidgets.QToolButton(self.centralwidget)
        self.btn_path.setObjectName("btn_path")
        self.horizontalLayout.addWidget(self.btn_path)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_rx = QtWidgets.QLabel(self.centralwidget)
        self.label_rx.setObjectName("label_rx")
        self.gridLayout.addWidget(self.label_rx, 0, 3, 1, 1)
        self.cb_rx = QtWidgets.QComboBox(self.centralwidget)
        self.cb_rx.setObjectName("cb_rx")
        self.gridLayout.addWidget(self.cb_rx, 0, 4, 1, 1)
        self.cb_tx = QtWidgets.QComboBox(self.centralwidget)
        self.cb_tx.setObjectName("cb_tx")
        self.gridLayout.addWidget(self.cb_tx, 0, 1, 1, 1)
        self.label_tx = QtWidgets.QLabel(self.centralwidget)
        self.label_tx.setObjectName("label_tx")
        self.gridLayout.addWidget(self.label_tx, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_coverage1 = QtWidgets.QLabel(self.tab)
        self.label_coverage1.setObjectName("label_coverage1")
        self.gridLayout_2.addWidget(self.label_coverage1, 0, 2, 1, 1)
        self.label_tx_gcp = QtWidgets.QLabel(self.tab)
        self.label_tx_gcp.setText("")
        self.label_tx_gcp.setObjectName("label_tx_gcp")
        self.gridLayout_2.addWidget(self.label_tx_gcp, 0, 1, 1, 1)
        self.label_case_id1 = QtWidgets.QLabel(self.tab)
        self.label_case_id1.setObjectName("label_case_id1")
        self.gridLayout_2.addWidget(self.label_case_id1, 0, 0, 1, 1)
        self.cb_gcp_area = QtWidgets.QComboBox(self.tab)
        self.cb_gcp_area.setObjectName("cb_gcp_area")
        self.gridLayout_2.addWidget(self.cb_gcp_area, 0, 4, 1, 1)
        self.dt_gcp_DateTime = QtWidgets.QDateTimeEdit(self.tab)
        self.dt_gcp_DateTime.setEnabled(False)
        self.dt_gcp_DateTime.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dt_gcp_DateTime.setCalendarPopup(True)
        self.dt_gcp_DateTime.setTimeSpec(QtCore.Qt.LocalTime)
        self.dt_gcp_DateTime.setObjectName("dt_gcp_DateTime")
        self.gridLayout_2.addWidget(self.dt_gcp_DateTime, 2, 2, 1, 1)
        self.rb_gcp_DateTime = QtWidgets.QRadioButton(self.tab)
        self.rb_gcp_DateTime.setText("")
        self.rb_gcp_DateTime.setObjectName("rb_gcp_DateTime")
        self.gridLayout_2.addWidget(self.rb_gcp_DateTime, 2, 4, 1, 1)
        self.rb_gcp_DayNight = QtWidgets.QRadioButton(self.tab)
        self.rb_gcp_DayNight.setEnabled(True)
        self.rb_gcp_DayNight.setText("")
        self.rb_gcp_DayNight.setChecked(True)
        self.rb_gcp_DayNight.setObjectName("rb_gcp_DayNight")
        self.gridLayout_2.addWidget(self.rb_gcp_DayNight, 1, 4, 1, 1)
        self.range_max_gcpath = QtWidgets.QDoubleSpinBox(self.tab)
        self.range_max_gcpath.setMinimum(20.0)
        self.range_max_gcpath.setMaximum(10000.0)
        self.range_max_gcpath.setSingleStep(100.0)
        self.range_max_gcpath.setProperty("value", 7000.0)
        self.range_max_gcpath.setObjectName("range_max_gcpath")
        self.gridLayout_2.addWidget(self.range_max_gcpath, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)
        self.cb_gcp_DayNight = QtWidgets.QComboBox(self.tab)
        self.cb_gcp_DayNight.setObjectName("cb_gcp_DayNight")
        self.cb_gcp_DayNight.addItem("")
        self.cb_gcp_DayNight.addItem("")
        self.gridLayout_2.addWidget(self.cb_gcp_DayNight, 1, 2, 1, 1)
        self.cb_gcpath_ionosphere = QtWidgets.QComboBox(self.tab)
        self.cb_gcpath_ionosphere.setObjectName("cb_gcpath_ionosphere")
        self.cb_gcpath_ionosphere.addItem("")
        self.gridLayout_2.addWidget(self.cb_gcpath_ionosphere, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.btnGcp = QtWidgets.QPushButton(self.tab)
        self.btnGcp.setObjectName("btnGcp")
        self.gridLayout_2.addWidget(self.btnGcp, 4, 4, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rb_bearings_DayNight = QtWidgets.QRadioButton(self.tab_2)
        self.rb_bearings_DayNight.setText("")
        self.rb_bearings_DayNight.setChecked(True)
        self.rb_bearings_DayNight.setObjectName("rb_bearings_DayNight")
        self.gridLayout_3.addWidget(self.rb_bearings_DayNight, 1, 4, 1, 1)
        self.dt_bearings_DateTime = QtWidgets.QDateTimeEdit(self.tab_2)
        self.dt_bearings_DateTime.setEnabled(False)
        self.dt_bearings_DateTime.setCalendarPopup(True)
        self.dt_bearings_DateTime.setObjectName("dt_bearings_DateTime")
        self.gridLayout_3.addWidget(self.dt_bearings_DateTime, 2, 2, 1, 1)
        self.rb_bearings_DateTime = QtWidgets.QRadioButton(self.tab_2)
        self.rb_bearings_DateTime.setText("")
        self.rb_bearings_DateTime.setObjectName("rb_bearings_DateTime")
        self.gridLayout_3.addWidget(self.rb_bearings_DateTime, 2, 4, 1, 1)
        self.label_tx_bearings = QtWidgets.QLabel(self.tab_2)
        self.label_tx_bearings.setText("")
        self.label_tx_bearings.setObjectName("label_tx_bearings")
        self.gridLayout_3.addWidget(self.label_tx_bearings, 0, 1, 1, 1)
        self.cb_bearings_DayNight = QtWidgets.QComboBox(self.tab_2)
        self.cb_bearings_DayNight.setObjectName("cb_bearings_DayNight")
        self.cb_bearings_DayNight.addItem("")
        self.cb_bearings_DayNight.addItem("")
        self.gridLayout_3.addWidget(self.cb_bearings_DayNight, 1, 2, 1, 1)
        self.range_max_bearings = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.range_max_bearings.setMinimum(20.0)
        self.range_max_bearings.setMaximum(10000.0)
        self.range_max_bearings.setSingleStep(100.0)
        self.range_max_bearings.setProperty("value", 7000.0)
        self.range_max_bearings.setObjectName("range_max_bearings")
        self.gridLayout_3.addWidget(self.range_max_bearings, 4, 1, 1, 1)
        self.cb_bearings_ionosphere = QtWidgets.QComboBox(self.tab_2)
        self.cb_bearings_ionosphere.setObjectName("cb_bearings_ionosphere")
        self.cb_bearings_ionosphere.addItem("")
        self.gridLayout_3.addWidget(self.cb_bearings_ionosphere, 1, 1, 1, 1)
        self.label_case_id1_2 = QtWidgets.QLabel(self.tab_2)
        self.label_case_id1_2.setObjectName("label_case_id1_2")
        self.gridLayout_3.addWidget(self.label_case_id1_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_coverage1_2 = QtWidgets.QLabel(self.tab_2)
        self.label_coverage1_2.setObjectName("label_coverage1_2")
        self.gridLayout_3.addWidget(self.label_coverage1_2, 0, 2, 1, 1)
        self.cb_bearings_area = QtWidgets.QComboBox(self.tab_2)
        self.cb_bearings_area.setObjectName("cb_bearings_area")
        self.gridLayout_3.addWidget(self.cb_bearings_area, 0, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)
        self.btnBearings = QtWidgets.QPushButton(self.tab_2)
        self.btnBearings.setObjectName("btnBearings")
        self.gridLayout_3.addWidget(self.btnBearings, 4, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_bearings = QtWidgets.QLabel(self.tab_2)
        self.label_bearings.setText("")
        self.label_bearings.setObjectName("label_bearings")
        self.gridLayout_3.addWidget(self.label_bearings, 2, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        InputGen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(InputGen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 21))
        self.menubar.setObjectName("menubar")
        InputGen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(InputGen)
        self.statusbar.setObjectName("statusbar")
        InputGen.setStatusBar(self.statusbar)

        self.retranslateUi(InputGen)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(InputGen)
        InputGen.setTabOrder(self.lineEdit_path, self.btn_path)
        InputGen.setTabOrder(self.btn_path, self.cb_tx)
        InputGen.setTabOrder(self.cb_tx, self.cb_rx)
        InputGen.setTabOrder(self.cb_rx, self.cb_gcp_area)
        InputGen.setTabOrder(self.cb_gcp_area, self.cb_gcpath_ionosphere)
        InputGen.setTabOrder(self.cb_gcpath_ionosphere, self.cb_gcp_DayNight)
        InputGen.setTabOrder(self.cb_gcp_DayNight, self.rb_gcp_DayNight)
        InputGen.setTabOrder(self.rb_gcp_DayNight, self.rb_gcp_DateTime)
        InputGen.setTabOrder(self.rb_gcp_DateTime, self.dt_gcp_DateTime)
        InputGen.setTabOrder(self.dt_gcp_DateTime, self.cb_bearings_area)
        InputGen.setTabOrder(self.cb_bearings_area, self.cb_bearings_ionosphere)
        InputGen.setTabOrder(self.cb_bearings_ionosphere, self.rb_bearings_DayNight)
        InputGen.setTabOrder(self.rb_bearings_DayNight, self.cb_bearings_DayNight)
        InputGen.setTabOrder(self.cb_bearings_DayNight, self.rb_bearings_DateTime)
        InputGen.setTabOrder(self.rb_bearings_DateTime, self.dt_bearings_DateTime)

    def retranslateUi(self, InputGen):
        _translate = QtCore.QCoreApplication.translate
        InputGen.setWindowTitle(_translate("InputGen", "LWPC Input Generator"))
        self.label_20.setText(_translate("InputGen", "<html><head/><body><p align=\"center\">LWPC path</p></body></html>"))
        self.lineEdit_path.setToolTip(_translate("InputGen", "Write here the path of your LWPC\'s directory and press <Enter>"))
        self.lineEdit_path.setText(_translate("InputGen", "C:/lwpcv21"))
        self.btn_path.setText(_translate("InputGen", "..."))
        self.label_rx.setText(_translate("InputGen", "<html><head/><body><p align=\"center\">Receiver ID</p></body></html>"))
        self.label_tx.setText(_translate("InputGen", "<html><head/><body><p align=\"center\">Transmitter ID</p></body></html>"))
        self.label_coverage1.setText(_translate("InputGen", "coverage of the"))
        self.label_case_id1.setText(_translate("InputGen", "area"))
        self.label_2.setText(_translate("InputGen", "range max"))
        self.cb_gcp_DayNight.setItemText(0, _translate("InputGen", "day"))
        self.cb_gcp_DayNight.setItemText(1, _translate("InputGen", "night"))
        self.cb_gcpath_ionosphere.setItemText(0, _translate("InputGen", "lwpm"))
        self.label.setText(_translate("InputGen", "ionosphere"))
        self.btnGcp.setText(_translate("InputGen", "generate gcp model"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("InputGen", "gcpath"))
        self.cb_bearings_DayNight.setItemText(0, _translate("InputGen", "day"))
        self.cb_bearings_DayNight.setItemText(1, _translate("InputGen", "night"))
        self.cb_bearings_ionosphere.setItemText(0, _translate("InputGen", "lwpm"))
        self.label_case_id1_2.setText(_translate("InputGen", "area"))
        self.label_3.setText(_translate("InputGen", "ionosphere"))
        self.label_coverage1_2.setText(_translate("InputGen", "coverage of the"))
        self.label_4.setText(_translate("InputGen", "range max"))
        self.btnBearings.setText(_translate("InputGen", "generate bearings model"))
        self.label_5.setText(_translate("InputGen", "bearing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("InputGen", "bearings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InputGen = QtWidgets.QMainWindow()
    ui = Ui_InputGen()
    ui.setupUi(InputGen)
    InputGen.show()
    sys.exit(app.exec_())

