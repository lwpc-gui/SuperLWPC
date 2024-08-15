# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainApp(object):
    def setupUi(self, MainApp):
        MainApp.setObjectName("MainApp")
        MainApp.setWindowModality(QtCore.Qt.WindowModal)
        MainApp.resize(933, 743)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainApp.sizePolicy().hasHeightForWidth())
        MainApp.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainApp.setWindowIcon(icon)
        MainApp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralWidget = QtWidgets.QWidget(MainApp)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spinBox_BetaAmb = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.spinBox_BetaAmb.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_BetaAmb.setPrefix("")
        self.spinBox_BetaAmb.setDecimals(3)
        self.spinBox_BetaAmb.setMinimum(0.2)
        self.spinBox_BetaAmb.setMaximum(0.6)
        self.spinBox_BetaAmb.setSingleStep(0.01)
        self.spinBox_BetaAmb.setProperty("value", 0.3)
        self.spinBox_BetaAmb.setObjectName("spinBox_BetaAmb")
        self.horizontalLayout_2.addWidget(self.spinBox_BetaAmb)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.spinBox_HpAmb = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.spinBox_HpAmb.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_HpAmb.setPrefix("")
        self.spinBox_HpAmb.setDecimals(3)
        self.spinBox_HpAmb.setMinimum(60.0)
        self.spinBox_HpAmb.setProperty("value", 74.0)
        self.spinBox_HpAmb.setObjectName("spinBox_HpAmb")
        self.horizontalLayout_3.addWidget(self.spinBox_HpAmb)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textDist = QtWidgets.QLabel(self.centralWidget)
        self.textDist.setObjectName("textDist")
        self.horizontalLayout_4.addWidget(self.textDist)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.spinBox_Step = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.spinBox_Step.setPrefix("")
        self.spinBox_Step.setSuffix("")
        self.spinBox_Step.setDecimals(0)
        self.spinBox_Step.setMinimum(1.0)
        self.spinBox_Step.setMaximum(500.0)
        self.spinBox_Step.setProperty("value", 20.0)
        self.spinBox_Step.setObjectName("spinBox_Step")
        self.horizontalLayout_4.addWidget(self.spinBox_Step)
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.spinBox_NLines = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_NLines.setMinimum(5)
        self.spinBox_NLines.setMaximum(50)
        self.spinBox_NLines.setProperty("value", 10)
        self.spinBox_NLines.setObjectName("spinBox_NLines")
        self.horizontalLayout.addWidget(self.spinBox_NLines)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.dBeta = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.dBeta.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dBeta.setDecimals(3)
        self.dBeta.setMinimum(-0.6)
        self.dBeta.setMaximum(0.6)
        self.dBeta.setSingleStep(0.05)
        self.dBeta.setProperty("value", -0.1)
        self.dBeta.setObjectName("dBeta")
        self.horizontalLayout_6.addWidget(self.dBeta)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.dHp = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.dHp.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dHp.setDecimals(3)
        self.dHp.setMinimum(-30.0)
        self.dHp.setMaximum(30.0)
        self.dHp.setSingleStep(1.0)
        self.dHp.setProperty("value", -5.0)
        self.dHp.setObjectName("dHp")
        self.horizontalLayout_5.addWidget(self.dHp)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.btn_updateMaillor = QtWidgets.QPushButton(self.centralWidget)
        self.btn_updateMaillor.setObjectName("btn_updateMaillor")
        self.verticalLayout.addWidget(self.btn_updateMaillor)
        self.label_14 = QtWidgets.QLabel(self.centralWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.centralWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.doubleSpinBox_dA = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox_dA.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_dA.setDecimals(3)
        self.doubleSpinBox_dA.setMinimum(-50.0)
        self.doubleSpinBox_dA.setMaximum(50.0)
        self.doubleSpinBox_dA.setSingleStep(0.001)
        self.doubleSpinBox_dA.setProperty("value", 1.4)
        self.doubleSpinBox_dA.setObjectName("doubleSpinBox_dA")
        self.horizontalLayout_7.addWidget(self.doubleSpinBox_dA)
        self.label_16 = QtWidgets.QLabel(self.centralWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_7.addWidget(self.label_16)
        self.doubleSpinBox_dPhi = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox_dPhi.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_dPhi.setDecimals(3)
        self.doubleSpinBox_dPhi.setMinimum(-180.0)
        self.doubleSpinBox_dPhi.setMaximum(180.0)
        self.doubleSpinBox_dPhi.setSingleStep(1.0)
        self.doubleSpinBox_dPhi.setProperty("value", -97.7)
        self.doubleSpinBox_dPhi.setObjectName("doubleSpinBox_dPhi")
        self.horizontalLayout_7.addWidget(self.doubleSpinBox_dPhi)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_27 = QtWidgets.QLabel(self.centralWidget)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_15.addWidget(self.label_27)
        self.lineEdit_errdA = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_errdA.setObjectName("lineEdit_errdA")
        self.horizontalLayout_15.addWidget(self.lineEdit_errdA)
        self.label_28 = QtWidgets.QLabel(self.centralWidget)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_15.addWidget(self.label_28)
        self.lineEdit_errdPhi = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_errdPhi.setObjectName("lineEdit_errdPhi")
        self.horizontalLayout_15.addWidget(self.lineEdit_errdPhi)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.pushButton_profile = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_profile.setStatusTip("")
        self.pushButton_profile.setObjectName("pushButton_profile")
        self.verticalLayout.addWidget(self.pushButton_profile)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_21 = QtWidgets.QLabel(self.centralWidget)
        self.label_21.setMouseTracking(True)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_12.addWidget(self.label_21)
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_12.addWidget(self.progressBar_2)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_22 = QtWidgets.QLabel(self.centralWidget)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_13.addWidget(self.label_22)
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_13.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.label_19 = QtWidgets.QLabel(self.centralWidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout.addWidget(self.label_19)
        self.labelDAlwpc = QtWidgets.QLabel(self.centralWidget)
        self.labelDAlwpc.setObjectName("labelDAlwpc")
        self.verticalLayout.addWidget(self.labelDAlwpc)
        self.DAmpLWPC = QtWidgets.QLabel(self.centralWidget)
        self.DAmpLWPC.setObjectName("DAmpLWPC")
        self.verticalLayout.addWidget(self.DAmpLWPC)
        self.labelDPlwpc = QtWidgets.QLabel(self.centralWidget)
        self.labelDPlwpc.setObjectName("labelDPlwpc")
        self.verticalLayout.addWidget(self.labelDPlwpc)
        self.DPhiLWPC = QtWidgets.QLabel(self.centralWidget)
        self.DPhiLWPC.setObjectName("DPhiLWPC")
        self.verticalLayout.addWidget(self.DPhiLWPC)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.lineEdit_BetaRes = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_BetaRes.setReadOnly(True)
        self.lineEdit_BetaRes.setObjectName("lineEdit_BetaRes")
        self.horizontalLayout_9.addWidget(self.lineEdit_BetaRes)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.lineEdit_HpRes = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_HpRes.setReadOnly(True)
        self.lineEdit_HpRes.setObjectName("lineEdit_HpRes")
        self.horizontalLayout_10.addWidget(self.lineEdit_HpRes)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_17 = QtWidgets.QLabel(self.centralWidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.label_17)
        self.lineEdit_errdARres = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_errdARres.setReadOnly(True)
        self.lineEdit_errdARres.setObjectName("lineEdit_errdARres")
        self.horizontalLayout_8.addWidget(self.lineEdit_errdARres)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.label_18 = QtWidgets.QLabel(self.centralWidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_8.addWidget(self.label_18)
        self.lineEdit_errdPhiRes = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_errdPhiRes.setReadOnly(True)
        self.lineEdit_errdPhiRes.setObjectName("lineEdit_errdPhiRes")
        self.horizontalLayout_8.addWidget(self.lineEdit_errdPhiRes)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.pushButton_simulation = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_simulation.setObjectName("pushButton_simulation")
        self.verticalLayout.addWidget(self.pushButton_simulation)
        self.horizontalLayout_11.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mpl1 = MPL_WIDGET(self.centralWidget)
        self.mpl1.setObjectName("mpl1")
        self.verticalLayout_2.addWidget(self.mpl1)
        self.mpl2 = MPL_WIDGET(self.centralWidget)
        self.mpl2.setObjectName("mpl2")
        self.verticalLayout_2.addWidget(self.mpl2)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        MainApp.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainApp)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 933, 20))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuConfiguration = QtWidgets.QMenu(self.menuBar)
        self.menuConfiguration.setObjectName("menuConfiguration")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        MainApp.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainApp)
        self.statusBar.setObjectName("statusBar")
        MainApp.setStatusBar(self.statusBar)
        self.actionAbout = QtWidgets.QAction(MainApp)
        self.actionAbout.setObjectName("actionAbout")
        self.actionTuturial = QtWidgets.QAction(MainApp)
        self.actionTuturial.setObjectName("actionTuturial")
        self.actionExit = QtWidgets.QAction(MainApp)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_Qt = QtWidgets.QAction(MainApp)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.LWPC_input = QtWidgets.QAction(MainApp)
        self.LWPC_input.setObjectName("LWPC_input")
        self.actionReset = QtWidgets.QAction(MainApp)
        self.actionReset.setObjectName("actionReset")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionTuturial)
        self.menuConfiguration.addAction(self.LWPC_input)
        self.menuTools.addAction(self.actionReset)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuConfiguration.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainApp)
        QtCore.QMetaObject.connectSlotsByName(MainApp)

    def retranslateUi(self, MainApp):
        _translate = QtCore.QCoreApplication.translate
        MainApp.setWindowTitle(_translate("MainApp", "SuperLWPC"))
        self.label.setText(_translate("MainApp", "β Anbient "))
        self.label_2.setText(_translate("MainApp", "H\' Anbient "))
        self.textDist.setText(_translate("MainApp", "--/--- Distance = -- Mm"))
        self.label_7.setText(_translate("MainApp", "step"))
        self.label_8.setText(_translate("MainApp", "km"))
        self.label_5.setText(_translate("MainApp", "<html><head/><body><p align=\"center\">Meshing</p></body></html>"))
        self.label_11.setText(_translate("MainApp", "<html><head/><body><p align=\"center\">Δ β</p></body></html>"))
        self.label_12.setText(_translate("MainApp", "<html><head/><body><p align=\"center\">Δ H\'</p></body></html>"))
        self.btn_updateMaillor.setText(_translate("MainApp", "Update profile"))
        self.label_14.setText(_translate("MainApp", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Parameters from VLF signal</span></p></body></html>"))
        self.label_15.setText(_translate("MainApp", "<html><head/><body><p align=\"center\">Δ A (dB)</p></body></html>"))
        self.label_16.setText(_translate("MainApp", "<html><head/><body><p align=\"center\">Δ φ (°)</p></body></html>"))
        self.label_27.setText(_translate("MainApp", "<html><head/><body><p align=\"center\">err Δ A (dB)</p></body></html>"))
        self.lineEdit_errdA.setText(_translate("MainApp", "0.2"))
        self.label_28.setText(_translate("MainApp", "<html><head/><body><p align=\"center\">err Δ φ (°)</p></body></html>"))
        self.lineEdit_errdPhi.setText(_translate("MainApp", "2"))
        self.pushButton_profile.setText(_translate("MainApp", "Generate results"))
        self.label_21.setText(_translate("MainApp", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">β</span></p></body></html>"))
        self.label_22.setText(_translate("MainApp", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">H\'</span></p></body></html>"))
        self.label_19.setText(_translate("MainApp", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Output results</span></p></body></html>"))
        self.labelDAlwpc.setText(_translate("MainApp", "<html><head/><body><p><span style=\" font-weight:600;\">Δ A</span><span style=\" font-weight:600; vertical-align:sub;\">LWPC</span><span style=\" font-weight:600;\"> (dB)</span></p></body></html>"))
        self.DAmpLWPC.setText(_translate("MainApp", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">----</span></p></body></html>"))
        self.labelDPlwpc.setText(_translate("MainApp", "<html><head/><body><p><span style=\" font-weight:600;\">Δ φ</span><span style=\" font-weight:600; vertical-align:sub;\">LWPC</span><span style=\" font-weight:600;\"> (°)</span></p></body></html>"))
        self.DPhiLWPC.setText(_translate("MainApp", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">----</span></p></body></html>"))
        self.label_3.setText(_translate("MainApp", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">β  disturbance</span></p></body></html>"))
        self.label_4.setText(_translate("MainApp", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">H\'  disturbance</span></p></body></html>"))
        self.label_17.setText(_translate("MainApp", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">err Δ A (dB)</span></p></body></html>"))
        self.label_18.setText(_translate("MainApp", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">err Δ φ (°)</span></p></body></html>"))
        self.pushButton_simulation.setText(_translate("MainApp", "Show simulation"))
        self.menuFile.setTitle(_translate("MainApp", "File"))
        self.menuHelp.setTitle(_translate("MainApp", "Help"))
        self.menuConfiguration.setTitle(_translate("MainApp", "Configuration"))
        self.menuTools.setTitle(_translate("MainApp", "Tools"))
        self.actionAbout.setText(_translate("MainApp", "About"))
        self.actionAbout.setStatusTip(_translate("MainApp", "About SuperLWPC application"))
        self.actionAbout.setShortcut(_translate("MainApp", "Ctrl+A"))
        self.actionTuturial.setText(_translate("MainApp", "Tutorial"))
        self.actionTuturial.setStatusTip(_translate("MainApp", "This small tutorial may help you!"))
        self.actionTuturial.setShortcut(_translate("MainApp", "Ctrl+T"))
        self.actionExit.setText(_translate("MainApp", "Exit"))
        self.actionExit.setStatusTip(_translate("MainApp", "Exit SuperLWPC"))
        self.actionExit.setShortcut(_translate("MainApp", "Ctrl+Q"))
        self.actionAbout_Qt.setText(_translate("MainApp", "About Qt"))
        self.actionAbout_Qt.setStatusTip(_translate("MainApp", "Technology behind this beautiful GUI"))
        self.actionAbout_Qt.setShortcut(_translate("MainApp", "Ctrl+D"))
        self.LWPC_input.setText(_translate("MainApp", "LWPC input"))
        self.LWPC_input.setShortcut(_translate("MainApp", "Ctrl+I"))
        self.actionReset.setText(_translate("MainApp", "Reset"))
        self.actionReset.setStatusTip(_translate("MainApp", "Liberate lwpm.exe"))

from gui.mplwidget import MPL_WIDGET

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainApp = QtWidgets.QMainWindow()
    ui = Ui_MainApp()
    ui.setupUi(MainApp)
    MainApp.show()
    sys.exit(app.exec_())

