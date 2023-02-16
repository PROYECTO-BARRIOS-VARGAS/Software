###################
#######IMPORTS#####
###################
#Import GUI file
import sys
import os
from ui_interface import *
from Custom_Widgets.Widgets import *



from PyQt5.QtCore import QObject, QThread, pyqtSignal

import BoardManagers as BD
import SerialScripts.mainSerial as Serial
from time import sleep
###################
####MAIN WINDOW####
###################



class InterfaceUpdater():

    def __init__(self,ui : Ui_MainWindow, bd : BD.BoardManager):
        self.UI = ui
        self.boardManager = bd

    def change_IPG_color_RED(self, board_num, ipg_num):
        red_stylesheet = '''QPushButton{
            color: #ffffff;
            width: 70%;	
            height: 100%;
            background-color: rgb(200, 0, 0 / 85%);
            font-style: normal;
            font-weight: 800;
            height: 200%;
            width: 250%;
            border: 1px solid rgb(255, 0, 0 / 20%);
            border-radius: 5px;
            }

            QPushButton:hover {
                background-color: rgb(220, 0, 0);
                border: 1px solid rgb(255, 50, 50);
                border-width: 1px;
                border-radius: 5px;
            }'''
        eval(f"self.UI.p{board_num}h1_ipg{ipg_num}_Btn.setStyleSheet('''{red_stylesheet}''')")

    def change_IPG_color_GREEN(self, board_num, ipg_num):
        green_stylesheet = '''QPushButton{
            color: #ffffff;
            width: 70%;	
            background-color: rgb(0, 197, 95 / 85%);
            height: 100%;
            font-style: normal;
            font-weight: 800;
            height: 200%;
            width: 250%;
            border: 1px solid rgb(85, 255, 127 / 20%);
            border-radius: 5px;
            }

            QPushButton:hover {
                background-color: rgb(0, 197, 95);
                border: 1px solid rgb(85, 255, 127);
                border-width: 1px;
                border-radius: 5px;
            }'''

        eval(f"self.UI.p{board_num}h1_ipg{ipg_num}_Btn.setStyleSheet('''{green_stylesheet}''')")

    def change_IPG_color_GRAY(self, board_num, ipg_num):
        gray_stylesheet = '''QPushButton{
            color: #ffffff;
            width: 70%;	
            background-color: rgb(0, 197, 95 / 85%);
            height: 100%;
            font-style: normal;
            font-weight: 800;
            height: 200%;
            width: 250%;
            border: 1px solid rgb(85, 255, 127 / 20%);
            border-radius: 5px;
            }

            QPushButton:hover {
                background-color: rgb(0, 197, 95);
                border: 1px solid rgb(85, 255, 127);
                border-width: 1px;
                border-radius: 5px;
            }'''
        eval(f"self.UI.p{board_num}h1_ipg{ipg_num}_Btn.setStyleSheet('''{gray_stylesheet}''')")
        
    def change_IPG_color_YELLOW(self, board_num, ipg_num):
        yellow_stylesheet = '''QPushButton{
            color: #ffffff;
            width: 70%;	
            background-color: rgb(190, 197, 60 / 85%);
            height: 100%;
            font-style: normal;
            font-weight: 800;
            height: 200%;
            width: 250%;
            border: 1px solid rgb(200, 255, 127 / 20%);
            border-radius: 5px;
            }

            QPushButton:hover {
                background-color: rgb(190, 197, 60);
                border: 1px solid rgb(200, 255, 127);
                border-width: 1px;
                border-radius: 5px;
            }'''
        eval(f"self.UI.p{board_num}h1_ipg{ipg_num}_Btn.setStyleSheet('''{yellow_stylesheet}''')")
        
    def update_board (self, board_num):
        for ipg in self.boardManager.Borards[board_num-1].IPGs:
            if ipg.is_stimulating() and ipg.is_communicating():
                self.change_IPG_color_GREEN(board_num, ipg.idNum+1)
            elif not ipg.is_stimulating() and ipg.is_communicating():
                self.change_IPG_color_RED(board_num, ipg.idNum+1)
            else:
                self.change_IPG_color_GRAY(board_num, ipg.idNum+1)


class StatusCheckThread(QObject):
    update_board_status = pyqtSignal(int)
    update_ui = pyqtSignal()


    def run(self):
        """Long-running task."""
        while True:
            for i in range(1):
                sleep(1)
                self.update_board_status.emit(i+1)
                self.update_ui.emit()
            sleep(20)
            # sleep(2)
            # self.update_board_status.emit(1)
            # self.update_ui.emit()
            
class MainWindow(QMainWindow):

    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.boardManager = BD.BoardManager()
        self.ui_updater = InterfaceUpdater(self.ui, self.boardManager)
        try:
            self.ser =  Serial.Serial()
        except:
            print("An exception occurred")
        loadJsonStyle(self, self.ui)
        self.show()
        
        ###Expand center menu
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        ###Close center menu
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        ###Expand right menu
        self.ui.logsBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())

        ###Close right menu
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())
        
        ###Close notification menu
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())
        
        self.ui.p1h1_ipg1_Btn.clicked.connect(lambda: self.refresh())
        self.ui.p1h1_ipg2_Btn.clicked.connect(lambda: self.ser.command_stop_burn_in())
        self.ui.initMad_plancha1_horno1Btn.clicked.connect(lambda: self.ser.command_start_burn_in())

        # self.thread = QThread()
        # self.statusThread = StatusCheckThread()
        # self.statusThread.moveToThread(self.thread)
        # self.thread.started.connect(self.statusThread.run)
        # self.statusThread.update_board_status.connect(self.serial_steps)
        # self.statusThread.update_ui.connect(self.ui_updater.update_board)
        # self.thread.start()

    def serial_steps(self, board_num):
        self.ser.command_get_status(board_num)
        result = self.ser.read_n_bytes(2)
        self.boardManager.update_board_status(1,result)

    def refresh(self):
        self.ser.command_get_status(1)
        result = self.ser.read_n_bytes(2)
        self.boardManager.update_board_status(0,result)
        self.ui_updater.update_board(1)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

