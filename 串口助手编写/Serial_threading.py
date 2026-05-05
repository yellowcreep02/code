import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import QThread, pyqtSignal,QObject
from time import sleep
import threading
from PyQt5.QtSerialPort import QSerialPort


class Serial_Qthread_function(QObject):

    signal_Serialstart_function      = pyqtSignal()
    signal_pushButton_Open           = pyqtSignal(object)
    signal_pushButton_Open_flag      = pyqtSignal(object)
    signal_ReadData                  = pyqtSignal(object)
    signal_DTR                       = pyqtSignal(object)
    signal_TRS                       = pyqtSignal(object)
    signal_TimeView                  = pyqtSignal(object)


    def __init__(self,parent=None):
        super().__init__()
        print('初始化线程',threading.current_thread().ident)
        self.state = 0  #0未打开，1串口已打开，2串口已关闭

    def slot_pushButton_Open(self,parameter):

        if self.state == 0:
            print('按下打开串口按钮',parameter)
            self.Serial.setPortName(parameter['comboBox_Com'])
            self.Serial.setBaudRate(int(parameter['comboBox_Baud']))

            if parameter['comboBox_Stop'] == '1.5':
                self.Serial.setStopBits(3)
            else:
                self.Serial.setStopBits(int(parameter['comboBox_Stop']))

            self.Serial.setDataBits(int(parameter['comboBox_Data']))
            
            setParity = 0
            if parameter['comboBox_Check'] == 'None':
                setParity = 0
            elif parameter['comboBox_Check'] == 'Odd':
                setParity = 3
            else:
                setParity = 2

            self.Serial.setParity(setParity)

            if self.Serial.open(QSerialPort.ReadWrite)==True:
                print('打开串口成功')
                self.state = 1
                self.signal_pushButton_Open_flag.emit(self.state)

            else:
                self.signal_pushButton_Open_flag.emit(self.state)
                print('串口打开失败')

        else:
            print('关闭串口')
            self.state = 0
            self.Serial.close()
            self.signal_pushButton_Open_flag.emit(2)

    def slot_DTR(self,state):
        print('DTR',state)
        if state == 2:
            self.Serial.setDataTerminalReady(True)
        else:
            self.Serial.setDataTerminalReady(False)

    def slot_TRS(self,state):
        print('TRS',state)
        if state == 2:
            self.Serial.setRequestToSend(True)
        else:
            self.Serial.setRequestToSend(False)
        
    def slot_TimeView(self,state):
        print('TimeView',state)

    def Serial_receive_data(self):
        print("接受数据线程id:",threading.current_thread().ident)
        self.signal_ReadData.emit(self.Serial.readAll())
 
    def SerialInit_function(self):
        print("串口线程id:",threading.current_thread().ident)
        self.Serial = QSerialPort()
        self.Serial.readyRead.connect(self.Serial_receive_data)



