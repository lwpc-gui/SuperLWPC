from PyQt5.QtCore import pyqtSlot, QDateTime, QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
import os, sys, subprocess, platform
from gui.Ui_InputGen import Ui_InputGen
import Data_Loader as dl
from datetime import datetime
import locale
import json
class InputGenerator(QMainWindow, Ui_InputGen):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.init_directory=os.getcwd() # get initial directory
        try:
            path = self.init_directory # SuperLWPC path
            with open(path+'/config/dbconfig.json', 'r') as f:
                datastore=json.load(f)
            
            self.path=datastore["pathname"] # Path to LWPCv21
            self.lineEdit_path.setText(self.path)
            self.directory = os.chdir(self.path)
        except Exception:
            QMessageBox.critical(self, "LWPC path",
                                 "Directory '{}' not found!".format(self.path))
        self.Update_Interface()
    def Update_Interface(self):
        # Fill tx list from data
        try:
            df_xmtr = dl.xmtrLoader(pathname= self.path)
            self.cb_tx.addItems(df_xmtr['xmtr_id'])
        except Exception:
            QMessageBox.critical(self, "LWPC path",
                                 "Directory '{}' not found!".format(self.path))
        # Fill rx list from data
        try:
            df_rx = dl.rxLoader(pathname= self.path)
            self.cb_rx.addItems(df_rx["rx_id"])
        except Exception:
            QMessageBox.critical(self, "LWPC path",
                                 "Directory '{}' not found!".format(self.path))
        # Fill area list from data
        try:
            df_area = dl.areaLoader(pathname= self.path)
            self.cb_gcp_area.addItems(df_area['area_id'])
            self.cb_bearings_area.addItems(df_area['area_id'])
        except Exception:
            QMessageBox.critical(self, "LWPC path",
                                 "Directory '{}' not found!".format(self.path))
        # SET datetimeEdit widget to today
        today= datetime.now()
        self.dt_gcp_DateTime.setDateTime(today)
        self.dt_bearings_DateTime.setDateTime(today)
        # SET bearing tab from gcpath tab data
        # Load gcpath dataframe
        # df_gcpath, df_gcpathAmb = dl.gcpathLoader(pathname= self.path)
        # self.bearing, self.range_max = df_gcpath["bearing"], df_gcpath["rrho"]
        self.range_max_bearings.setValue(10000.)
        self.label_bearings.setText('68.7') # valeur initialisée du template

        
    def MakeGcpInputfile(self):
        '''
        Create gcp.inp with configured parameters
        '''
        # Load rx/tx info
        df_rx = dl.rxLoader(pathname= self.path)
        self.tx=self.cb_tx.currentText()
        self.rx=self.cb_rx.currentText()
        for i in range(len(df_rx)):
            if self.rx == df_rx["rx_id"][i]:
                self.lat_rx = df_rx["lat"][i]
                self.lon_rx= df_rx ["lon"][i]
                
        # Date Time Setting (Radio button state condition)
        if self.rb_gcp_DayNight.isChecked():
            self.dt_gcp = self.cb_gcp_DayNight.currentText()
        elif self.rb_gcp_DateTime.isChecked():
            dt= self.dt_gcp_DateTime.dateTime()
            dt= dt.toPyDateTime()
            # Date Time Format: https://www.dataquest.io/blog/python-datetime-tutorial/
            locale.setlocale(locale.LC_TIME,'en_US.utf8') # impose l'anglais si le système utilise autre langue
            self.dt_gcp = dt.strftime("%b/%d/%y %H:%M") 
        
        with open("gcpath.inp", 'w+') as f:
            f.write('case-id     %s coverage of the %s\n'%(self.tx,self.cb_gcp_area.currentText()))
            f.write('tx          gcpath\n')
            f.write('tx-data    %s\n'%self.tx)
            f.write('ionosphere  %s %s\n'%(self.cb_gcpath_ionosphere.currentText(), self.dt_gcp))
            f.write('range-max %s\n'%str(self.range_max_gcpath.value()))
            f.write('receivers    %s %s\n'% (self.lat_rx, self.lon_rx))
            f.write('gcpath\n')
            f.write('start\n')
            f.write('quit')
        #f.close()
        myOS = platform.system()
        if myOS == 'Windows':
            ##execute 'lwpm.exe' and create 'gcpath.log'
            subprocess.call(["lwpm.exe","gcpath"],  shell=True)
        else:
            os.system('./LWPC gcpath')
        
        df_gcpath, df_gcpathAmb = dl.gcpathLoader(pathname= self.path)
        self.bearing, self.range_max = df_gcpath["bearing"], df_gcpath["rrho"]
        
    def MakeBearingsInputfile(self):
        """
        Create bearing.log
        """
        df_gcpath, df_gcpathAmb = dl.gcpathLoader(pathname= self.path)
        self.bearing, self.range_max = df_gcpath["bearing"], df_gcpath["rrho"]
        df_rx = dl.rxLoader(pathname= self.path)
        self.tx=self.cb_tx.currentText()
        self.rx=self.cb_rx.currentText()
        for i in range(len(df_rx)):
            if self.rx == df_rx["rx_id"][i]:
                self.lat_rx = df_rx["lat"][i]
                self.lon_rx= df_rx ["lon"][i]

        # Date Time Setting (Radio button state condition)
        if self.rb_bearings_DayNight.isChecked():
            self.dt_bearings = self.cb_bearings_DayNight.currentText()
        elif self.rb_bearings_DateTime.isChecked():
            dt= self.dt_bearings_DateTime.dateTime()
            dt= dt.toPyDateTime()
            self.dt_bearings = dt.strftime("%b/%d/%y %H:%M") 
        
        with open("bearings.inp", 'w+') as f:
            f.write('file-mds    Output/\n')
            f.write('file-lwf    Output/\n')
            f.write('case-id     %s coverage of the %s\n'%(self.tx,self.cb_bearings_area.currentText()))
            f.write('tx          bearings\n')
            f.write('tx-data    %s\n'%self.tx)
            f.write('ionosphere  %s %s\n'%(self.cb_bearings_ionosphere.currentText(), self.dt_bearings))
            f.write('range-max %s\n'%str(self.range_max_bearings.value()))
            f.write('bearings %s\n'% str(float(self.bearing)))
            f.write('print-swg 2\n')
            f.write('lwf-vs-dist %s\n'%str(self.range_max_bearings.value()))
            f.write('print-lwf 2\n')
            f.write('start\n')
            f.write('quit')
        #f.close()
        myOS = platform.system()
        if myOS == 'Windows':
            subprocess.call(["lwpm.exe","bearings"],  shell=True)
            os.remove("Output/bearings.mds")
        else:
            try:
                os.remove("Output/bearings.mds")
            except:
                pass
            os.system('./LWPC bearings')
            os.remove("Output/bearings.mds")
            
        
    def configDataBase(self):
        """
        Create data base to store latest configuration
        #TODO! fix path for linux
        """
        
        #path = self.init_directory # /home/ahmed/Documents/SuperLWPC/source/gui/
        path = self.init_directory
        with open(path+'/config/dbconfig.json', 'w') as outfile:
            json.dump({
                "pathname": self.lineEdit_path.text(),
                "TxID": self.cb_tx.currentText(),
                "RxID": self.cb_rx.currentText(),
                "area" : self.cb_gcp_area.currentText(),
                "bearing" : self.label_bearings.text(),
                "ionosphere" : "range exponential"
                
                }, outfile)
        
    @pyqtSlot()
    def on_lineEdit_path_returnPressed(self):
            """
            set input in LWPC directory
            """
            try:
                self.path=self.lineEdit_path.text()
                self.directory = os.chdir(self.path)
                f = open('/'.join(self.path.split('/')[:-1])+"/" +"lwpcDAT.loc", "w")
                f.write(self.path+"/Data/")
                f.close()
                self.configDataBase()
                self.Update_Interface()
                QMessageBox.information(self, "LWPC path", "Working directory has been successfully set to '{}' ".format(self.path))
                
            except Exception:
                QMessageBox.critical(self, "LWPC path", "Directory '{}' not found!".format(self.path))
    @pyqtSlot()
    def on_btn_path_clicked(self):
        try:
            startingDir = '.'
            destDir = QFileDialog.getExistingDirectory(None, 
                                                             'Open working directory (LWPC path)', 
                                                             startingDir, 
                                                             QFileDialog.ShowDirsOnly)
            self.lineEdit_path.setText(destDir)
            self.path = destDir
            self.directory = os.chdir(self.path)
            f = open('/'.join(self.path.split('/')[:-1])+"/" +"lwpcDAT.loc", "w")
            f.write(self.path+"/Data/")
            f.close()
            self.configDataBase()
            self.Update_Interface()
            QMessageBox.information(self, "LWPC path", "Working directory has been successfully set to '{}' ".format(self.path))

        except:
            print("No changes in working directory path!")
    @pyqtSlot(str)
    def on_cb_tx_currentTextChanged(self):
        self.label_tx_gcp.setText(self.cb_tx.currentText())
        self.label_tx_bearings.setText(self.cb_tx.currentText())
        self.configDataBase()
        
    @pyqtSlot(str)
    def on_cb_rx_currentTextChanged(self):
        self.configDataBase()
        

    
    @pyqtSlot(bool)
    def on_rb_gcp_DayNight_toggled(self):
        '''
        Activate DayNight radio button (gcpath)
        '''
        self.cb_gcp_DayNight.setDisabled(False)
        self.dt_gcp_DateTime.setDisabled(True)
        
    @pyqtSlot(bool)
    def on_rb_bearings_DayNight_toggled(self):
        '''
        Activate DayNight radio button (bearings)
        '''
        self.cb_bearings_DayNight.setDisabled(False)
        self.dt_bearings_DateTime.setDisabled(True)
        
        
    @pyqtSlot(bool)
    def on_rb_gcp_DateTime_toggled(self):
        '''
        Activate DateTime radio button (gcpath)
        '''
        self.cb_gcp_DayNight.setDisabled(True)
        self.dt_gcp_DateTime.setDisabled(False)
        
    @pyqtSlot(bool)
    def on_rb_bearings_DateTime_toggled(self):
        '''
        Activate DateTime radio button (bearings)
        '''
        self.cb_bearings_DayNight.setDisabled(True)
        self.dt_bearings_DateTime.setDisabled(False)
        
        
    @pyqtSlot(QDate)
    def on_dt_gcp_DateTime_dateTimeChanged(self):
        '''
        Change datetime (gcpath)
        '''
        dt= self.dt_gcp_DateTime.dateTime()
        dt= dt.toPyDateTime()
        self.dt_gcp = dt.strftime("%b/%d/%y %H:%M")
        
    @pyqtSlot(QDate)
    def on_dt_bearings_DateTime_dateTimeChanged(self):
        '''
        Change datetime (bearings)
        '''
        dt= self.dt_bearings_DateTime.dateTime()
        dt= dt.toPyDateTime()
        self.dt_bearings = dt.strftime("%b/%d/%y %H:%M")
        
     
    @pyqtSlot(str)
    def on_cb_gcp_area_currentTextChanged(self):
        '''
        Synchronyse AREA (gcpath)
        '''
        index = self.cb_gcp_area.currentIndex()
        self.cb_bearings_area.setCurrentIndex(index)
        self.configDataBase()
    
    @pyqtSlot(str)
    def on_cb_bearings_area_currentTextChanged(self):
        '''
        Synchronyse AREA (bearings)
        '''
        index = self.cb_bearings_area.currentIndex()
        self.cb_gcp_area.setCurrentIndex(index)
        self.configDataBase()
        
    @pyqtSlot()
    def on_btnGcp_clicked(self):
        try:
            self.MakeGcpInputfile()
            self.range_max_bearings.setValue(self.range_max)
            self.range_max_gcpath.setValue(self.range_max)
            self.label_bearings.setText(str(float(self.bearing)))
            self.configDataBase()
            self.MakeGcpInputfile()
            QMessageBox.information(self, "log file", "Your gcpath.log file have been successfully created ")
            
        except OSError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(e))
            msg.setWindowTitle("Error")
            msg.exec_()
            #os.system("taskkill /f /im  lwpm.exe")
    @pyqtSlot()
    def on_btnBearings_clicked(self):
        try:
            self.MakeBearingsInputfile()
            QMessageBox.information(self, "log file", "Your bearings.log file have been successfully created")
        except OSError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(e))
            msg.setWindowTitle("Error")
            msg.exec_()
            #os.system("taskkill /f /im  lwpm.exe")
    
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Conf_Input = InputGenerator()
    Conf_Input.show()
    sys.exit(app.exec_())