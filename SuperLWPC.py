
"""
Module implementing SuperLWPC.
### GFORTRAN should be installed on linux (depandency)
(sudo apt-get install libgfortran3:amd64)
"""
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from gui.main import Ui_MainApp
from gui.InputGen import InputGenerator
from gui.Ui_InputGen import Ui_InputGen
import os, sys, subprocess, platform
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import Data_Loader as dl
import json
class SuperLWPC(QMainWindow, Ui_MainApp):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SuperLWPC, self).__init__(parent)
        self.setupUi(self)
        self.init_directory=os.getcwd() # get initial directory
        #self.Maillor()
        # Input gen window
        self.input_gen= InputGenerator(self)
        self.__version__ = "1.0.4"
        print('''
              *********************************************************
              VLF modelling and simulation software
              SuperLWPC v{}
              please report bugs to ahmed.ammar@fst.utm.tn
              *********************************************************'''.format(self.__version__))
        
    def Maillor(self):
        '''
        Create Hp and Beta mesh grid
        '''
        global TxID, RxID, pathname
        NLines=self.spinBox_NLines.value()
        
        dHp=self.dHp.value()
        dBeta=self.dBeta.value()
        # load database
        path = self.init_directory
        with open(path+'/config/dbconfig.json', 'r') as f:
            datastore=json.load(f)
        pathname = datastore["pathname"]
        TxID = datastore["TxID"]
        RxID = datastore["RxID"]
        Range_max = datastore["range_max"]

        self.newrho = np.arange(0, float(Range_max), self.spinBox_Step.value()) 
        self.newhprime = np.ones(len(self.newrho))*self.spinBox_HpAmb.value()
        self.newbeta = np.ones(len(self.newrho))*self.spinBox_BetaAmb.value()
        # save ambient config
        np.save(path+"/config/init_grid_data.npy", np.array([self.newrho, self.newhprime, self.newbeta]))
        #distance to receiver
        self.textDist.setText("{}/{} Distance = {} Mm".format(TxID, RxID,float(Range_max)/1000))
        plt1 = self.mpl1.canvas
        plt2 = self.mpl2.canvas
        plt1.ax.clear(); plt2.ax.clear() #clear on plot()
        #plt1.ax.plot(rho/1000, hprime, "bo")
        plt1.ax.plot(self.newrho/1000, self.newhprime, "-b")
        #plt2.ax.plot(rho/1000, beta, "bo")
        plt2.ax.plot(self.newrho/1000, self.newbeta, "-b")
#         perturbation grid
        self.HPmatrix = np.zeros((len(self.newhprime), NLines+1))
        try:
            j=0
            for k in np.linspace(1E-8,dHp,NLines, endpoint = True):
                for i in range(len(self.newhprime)):
                    self.HPmatrix[i,j]= self.newhprime[i] + k
    
                plt1.ax.plot(self.newrho/1000, self.HPmatrix[:,j], "r--", ms=1, alpha = 1)
                j+=1
        except OSError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(e))
            msg.setWindowTitle("Error")
            msg.exec_()        
#        plt1.ax.plot(self.newrho/1000,  self.HPmatrix[:,2], "y-", ms=1, alpha = 1)

            
        plt1.ax.set_title("H' stratified profile: %s-%s"%(TxID, RxID))
        plt1.ax.set_xlabel("rho [Mm]")
        plt1.ax.set_ylabel("h' [km]")    
        plt1.ax.get_figure().tight_layout(pad=0.7, h_pad=None, rect=(None,0.11, None, 0.895)) # fill space
        plt1.draw() # required to update the window
            
        self.BETAmatrix = np.zeros((len(self.newbeta), NLines+1))
        try:
            j = 0
            for k in np.linspace(1E-8, dBeta,NLines, endpoint = True):
                for i in range(len(self.newbeta)):
                    self.BETAmatrix[i,j]= self.newbeta[i] + k
                plt2.ax.plot(self.newrho/1000, self.BETAmatrix[:,j], "r--", ms=1, alpha = 1)
                j+=1
        except OSError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(e))
            msg.setWindowTitle("Error")
            msg.exec_()
        
#        plt2.ax.plot(self.newrho/1000,  self.BETAmatrix[:,2], "y-", ms=1, alpha = 1)
            
        plt2.ax.set_title("Beta stratified profile: %s-%s"%(TxID, RxID))
        plt2.ax.set_xlabel("rho [Mm]")
        plt2.ax.set_ylabel(r"$\beta \ [km^{-1}]$")    
        plt2.ax.get_figure().tight_layout(pad=0.7, h_pad=None, rect=(None,0.11, None, 0.895)) # fill space
        plt2.draw() # required to update the window
 
            
    def profile(self):
        '''
        Simulation 
        '''
        # load database
        path = self.init_directory # SuperLWPC path
        with open(path+'/config/dbconfig.json', 'r') as f:
            datastore=json.load(f)
        pathname = datastore["pathname"]
        directory = os.chdir(pathname) # change path to lwpcv21
        tx = datastore["TxID"]
        area = datastore["area"]
        bearing = datastore["bearing"]
        ionosphere = datastore["ionosphere"]
        range_max = float(datastore["range_max"])
        # # load ambient profile from bearing
        # df_bearings_path_info , df_ambient = dl.bearingsLoader(pathname= pathname)
        # ampQ, phiQ = df_ambient[:,1][-1], df_ambient[:,2][-1]
        ## load ambient from rexp
        Hpamb,Betaamb = self.newhprime, self.newbeta
        np.savetxt("Profile/rexp.ndx", np.c_[self.newrho, Betaamb, Hpamb],
                   header=" rho  beta  hprime",comments='; ', fmt='%.4f', delimiter='  ')
        with open("rexp.inp", 'w+') as f:
            f.write('file-mds    Output/ \n')
            f.write('file-lwf    Output/ \n')
            f.write('file-prf    Profile/ \n')
            f.write('file-ndx    Profile/ \n')
            f.write('case-id     %s coverage of the %s\n'%(tx,area))
            f.write('tx          rexp\n')
            f.write('tx-data    %s\n'%tx)
            f.write('ionosphere  %s rexp\n'% ionosphere)
            f.write('range-max %s\n'%str(range_max))
            f.write('bearing %s\n'% str(bearing))
            f.write('print-swg   2\n')
            f.write('lwf-vs-dist %s\n'%str(range_max))
            f.write('print-lwf   2\n')
            f.write('start\n')
            f.write('quit')
        #f.close()
        #execute LWPC
        myOS = platform.system()
        if myOS == 'Windows':
            subprocess.call(["lwpm.exe","rexp"],  shell=True)
            os.remove("Output/rexp.mds")
        else:
            try:
                os.remove("Output/rexp.mds")
            except:
                pass
            os.system('./LWPC rexp')
            os.remove("Output/rexp.mds")
            
        df_rexp_path_info,df_disturb = dl.rexpLoader(pathname= pathname)
        self.distAmbient = df_disturb[:-1,0]
        self.ampAmbient = df_disturb[:-1,1]
        self.phiAmbient = df_disturb[:-1,2]
        ampQ= df_disturb[:-1,1][-1]
        phiQ = df_disturb[:-1,2][-1]
        #-------------------
        DeltaA=self.doubleSpinBox_dA.value() #Perturbed Amplitude from the recorded signal
        DeltaPhi=self.doubleSpinBox_dPhi.value() #Perturbed Phase from the recorded signal
        Err_amp_min=float(self.lineEdit_errdA.text())
        Err_phi_min=float(self.lineEdit_errdPhi.text())
        Beta_min_index =0
        Hp_min_index=0
        Sol_Beta = 0
        Sol_Hp = 0
        Sol_DAmp_rexp = 0
        Sol_DPhi_rexp = 0
        N = self.spinBox_NLines.value()
        Err_Amp = np.zeros((N, N))
        Err_Phi = np.zeros((N, N))
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(N-1)
        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(N-1)
        for i in range(N):
            for j in range(N):
                np.savetxt("Profile/rexp.ndx", np.c_[self.newrho, self.BETAmatrix[:, i], self.HPmatrix[:, j]],
                           header=" rho  beta  hprime",comments='; ', fmt='%.4f', delimiter='  ')
                
                with open("rexp.inp", 'w+') as f:
                    f.write('file-mds    Output/ \n')
                    f.write('file-lwf    Output/ \n')
                    f.write('file-prf    Profile/ \n')
                    f.write('file-ndx    Profile/ \n')
                    f.write('case-id     %s coverage of the %s\n'%(tx,area))
                    f.write('tx          rexp\n')
                    f.write('tx-data    %s\n'%tx)
                    f.write('ionosphere  %s rexp\n'% ionosphere)
                    f.write('range-max %s\n'%str(range_max))
                    f.write('bearing %s\n'% str(bearing))
                    f.write('print-swg   2\n')
                    f.write('lwf-vs-dist %s\n'%str(range_max))
                    f.write('print-lwf   2\n')
                    f.write('start\n')
                    f.write('quit')
                #f.close()
                #execute LWPC
                myOS = platform.system()
                if myOS == 'Windows':
                    subprocess.call(["lwpm.exe","rexp"],  shell=True)
                    os.remove("Output/rexp.mds")
                else:
                    try:
                        os.remove("Output/rexp.mds")
                    except:
                        pass
                    os.system('./LWPC rexp')
                    os.remove("Output/rexp.mds")
                    
                df_rexp_path_info,df_disturb = dl.rexpLoader(pathname= pathname)
                amplitude_rexp = df_disturb[:-1,1][-1]
                phase_rexp = df_disturb[:-1,2][-1]
                DAmp_rexp = amplitude_rexp - ampQ
                DPhi_rexp = phase_rexp - phiQ
                err_amplitude = abs(DAmp_rexp - DeltaA)
                err_phase= abs(DPhi_rexp - DeltaPhi)
                Err_Amp[i, j] = err_amplitude
                Err_Phi[i, j] = err_phase
                
                if err_amplitude <= Err_amp_min and err_phase <= Err_phi_min:
                    Err_amp_min = err_amplitude
                    Err_phi_min = err_phase
                    Beta_min_index = i
                    Sol_Beta = self.BETAmatrix[:, Beta_min_index][-1]
                    Hp_min_index = j
                    Sol_Hp = self.HPmatrix[:, Hp_min_index][-1]
                    Sol_DAmp_rexp = DAmp_rexp
                    Sol_DPhi_rexp = DPhi_rexp
                #print("%d  %d  DArexp: %.3f errDArexp: %.3f  DPhirexp: %.3f errDPhirexp: %.3f\n"%(i, j, DAmp_rexp, err_amplitude,DPhi_rexp, err_phase))
                self.progressBar_2.setValue(j)
                self.progressBar.setValue(i)
                self.DAmpLWPC.setText(str("%3.3f" %DAmp_rexp))
                self.DPhiLWPC.setText(str("%3.3f" %DPhi_rexp))
                QtCore.QCoreApplication.processEvents() #Create loop that doesn't lock up the window Pyqt4
        
        self.DAmpLWPC.setText(str("%3.3f" %Sol_DAmp_rexp))
        self.DPhiLWPC.setText(str("%3.3f" %Sol_DPhi_rexp))
        self.lineEdit_BetaRes.setText(str("%.3f" %Sol_Beta))
        self.lineEdit_HpRes.setText(str("%.3f" %Sol_Hp))
        self.lineEdit_errdARres.setText(str("%.3f" %Err_amp_min))
        self.lineEdit_errdPhiRes.setText(str("%.3f" %Err_phi_min))
#        # PLOT FIGURS OF ERRORS ON PHASE AND AMPLITUDE
        dHp=self.dHp.value()
        dBeta=self.dBeta.value()
        x=np.linspace(Hpamb[0], Hpamb[0]+dHp, N)
        y=np.linspace(Betaamb[0], Betaamb[0] + dBeta, N)
        xi, yi = np.meshgrid(x, y) #Order is very important
        plt.figure(figsize=(8,6))
        plt.subplot(2,1,1)
        levels=np.linspace(0.,1.,4)
        cs1=plt.contour(xi,yi,Err_Amp,levels,cmap="Greys")
        # plt.colorbar(cs1, extend='both')
        # plt.clabel(cs1, levels[1::2],  # label every second level
        #            inline=1,
        #            fmt='%1.1f', fontsize=14)
        im1=plt.contourf(xi,yi,Err_Amp,levels=np.linspace(0, 10, 21),
                         cmap="gnuplot", origin='lower')
        CBI1 = plt.colorbar(im1, shrink=0.8)
        CBI1.set_label(r'$err \Delta A$ [dB]')
        CBI1.add_lines(cs1)
        ## SHOW X, Y, Z VALUES ON TOP RIGHT CORNER
        ## REF : https://stackoverflow.com/questions/10081100/matplotlib-contourf-get-z-value-under-cursor
        Xflata, Yflata, Zflata = xi.flatten(), yi.flatten(), Err_Amp.flatten()
        def fmt1(x, y):
            # get closest point with known data
            dist = np.linalg.norm(np.vstack([Xflata - x, Yflata - y]), axis=0)
            idx = np.argmin(dist)
            z = Zflata[idx]
            return 'x={x:.5f}  y={y:.5f}  z={z:.5f}'.format(x=x, y=y, z=z)
        plt.gca().format_coord = fmt1
        
        if Sol_Beta and Sol_Hp !=0:
            plt.scatter(Sol_Hp,Sol_Beta, s=20, c ="r", marker="X",
            label=r"$H' = %.3f , \ \beta = %.3f$" %(Sol_Hp, Sol_Beta))
            plt.axvline(x = Sol_Hp,color ="k", linewidth=1, ls="--")
            plt.legend()
        # plt.title('Error on Amplitude')
        # plt.grid()
        plt.xlabel("h' [km]")
        plt.ylabel(r"$\beta \ [km^{-1}]$")
        
        
        plt.subplot(2,1,2)
        levels=np.linspace(0.,8.,4)
        cs2=plt.contour(xi,yi,Err_Phi,levels,cmap="Greys")
        # plt.colorbar(cs2, extend='both')
        # plt.clabel(cs2, levels[1::2],  # label every second level
        #            inline=1,
        #            fmt='%1.f', fontsize=14)
        im2=plt.contourf(xi,yi,Err_Phi,levels=np.linspace(0, 90, 21),
                         cmap="gnuplot", origin='lower')
        CBI2 = plt.colorbar(im2, shrink=0.8)
        CBI2.set_label(r'$err \Delta \phi$ [°]')
        CBI2.add_lines(cs2)
        Xflatp, Yflatp, Zflatp = xi.flatten(), yi.flatten(), Err_Phi.flatten()
        def fmt2(x, y):
            # get closest point with known data
            dist = np.linalg.norm(np.vstack([Xflatp - x, Yflatp - y]), axis=0)
            idx = np.argmin(dist)
            z = Zflatp[idx]
            return 'x={x:.5f}  y={y:.5f}  z={z:.5f}'.format(x=x, y=y, z=z)
        plt.gca().format_coord = fmt2
        
        if Sol_Beta and Sol_Hp !=0:
            plt.scatter(Sol_Hp, Sol_Beta, s=20, c ="r", marker="X",
            label=r"$H' = %.3f , \ \beta = %.3f$" %(Sol_Hp, Sol_Beta))
            plt.axvline(x = Sol_Hp,color ="k", linewidth=1, ls="--")
            plt.legend()
        
        plt.xlabel("h' [km]") 
        plt.ylabel(r"$\beta \ [km^{-1}]$")
        # plt.grid()
        #plt.savefig('..\\program\\tmp.pdf');  plt.savefig('..\\program\\tmp.png')
        plt.tight_layout()
        plt.show()
    @pyqtSlot(int)
    def on_spinBox_BetaAmb_valueChanged(self, p0):
        """
        Change beta ambient
        """
        self.Maillor()
    @pyqtSlot(int)
    def on_spinBox_HpAmb_valueChanged(self, p0):
        """
        Change hp ambient
        """
        self.Maillor()
    @pyqtSlot(int)
    def on_spinBox_Step_valueChanged(self, p0):
        """
        Change step of discret gcp path
        """
        self.Maillor()
    
    @pyqtSlot(int)
    def on_spinBox_NLines_valueChanged(self, p0):
        """
        Change number of lines h' and beta
        """
        self.Maillor()
    
    @pyqtSlot(float)
    def on_dHp_valueChanged(self, value):
        """
        Change dHP value
        """
        self.Maillor()
    
    
    @pyqtSlot(float)
    def on_dBeta_valueChanged(self, value):
        """
        Change dBeta value
        """
        self.Maillor()
        
    @pyqtSlot()
    def on_btn_updateMaillor_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            self.Maillor()
            QMessageBox.information(self, "update profile", "Profile successfully updated")
        except OSError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(e))
            msg.setWindowTitle("Error")
            msg.exec_()
            
    
    @pyqtSlot()
    def on_pushButton_profile_clicked(self):
        """
        Slot documentation goes here.
        """
        self.profile()
    @pyqtSlot()
    def on_pushButton_simulation_clicked(self):
        """
        Slot documentation goes here.
        """
        try:
            #df_bearings_path_info , df_ambient = dl.bearingsLoader(pathname = pathname)
            df_rexp_path_info,df_disturb = dl.rexpLoader(pathname = pathname)
            
            fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True,figsize=(8,5))
            plt.suptitle(f"Variation of signal amplitude and phase along the {TxID}-{RxID} propagation path",
                         fontweight = "bold")
            ax1.plot(self.distAmbient,self.ampAmbient, "b-", lw = 2, label = "Ambient amplitude")
            ax1.plot(df_disturb[:-1,0], df_disturb[:-1,1], "r-", lw = 2, label = "Perturbed amplitude")
            ax1.set_ylabel("Amplitude")
            ax1.legend()
            ax2.plot(self.distAmbient,self.phiAmbient, "b-", lw = 2, label = "Ambient phase")
            ax2.plot(df_disturb[:-1,0], df_disturb[:-1,2], "r-", lw = 2, label = "perturbed phase")
            ax2.set_xlabel("rho [km]")
            ax2.set_ylabel("Phase")
            ax2.legend()
            plt.show()
           
        except:
            print("Error! Please try another simulation.")
            pass
    
    @pyqtSlot()
    def on_actionAbout_triggered(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.about(self,"SuperLWPC v{}".format(self.__version__),
        """
        
        This application is an interface for LWPC program. It is a tool for finding Wait' parameters.
        
        Author: Ahmed AMMAR, Hassen Ghalila and Samir Naitamor \n
        Email: ahmed.ammar@fst.utm.tn, hassen.ghalila@gmail.com, snaitamor@yahoo.com \n
        
        """)
     # CONFIG - MB   
    @pyqtSlot()
    def on_LWPC_input_triggered(self):
        try:
            self.input_gen.show()
            self.input_gen.activateWindow()
            
        except:
            pass
    @pyqtSlot()
    def on_actionAbout_Qt_triggered(self):
        QMessageBox.aboutQt(self)
    
    @pyqtSlot()
    def on_actionTuturial_triggered(self):
        """
        Tutorial
        """
        filename = self.init_directory + '/manual.pdf'
       # os.chdir(self.init_directory)
        myOS = platform.system()
        if myOS == 'Windows':
            os.startfile(filename)
        elif myOS == 'Linux':
            subprocess.call(['xdg-open', filename])
        else:
            subprocess.call(['open', filename])
       # os.chdir(self.path)
        
    @pyqtSlot()
    def on_actionExit_triggered(self):
        """
        Slot documentation goes here.
        """
        self.close()
    #TOOLS - MB
    @pyqtSlot()
    def on_actionReset_triggered(self):
        """
        liberate lwpm.exe
        """
        myOS = platform.system()
        if myOS == 'Windows':
            os.system("taskkill /f /im  lwpm.exe")
        else:
            pass
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = SuperLWPC()
   
    MainWindow.show()
    sys.exit(app.exec_())
