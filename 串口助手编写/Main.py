import sys
import PyQt5.QtWidgets as qw
import Serial_ui
import threading
from Serial_threading import Serial_Qthread_function
from PyQt5.QtCore import QThread,QTimer
from PyQt5.QtSerialPort import QSerialPortInfo
from PyQt5.QtGui import QTextCursor,QColor
import time

class SerialForm(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Serial_ui.Ui_Serial()#对于窗口w创建ui实例
        self.ui.setupUi(self)#将Ui实例应用在窗口w
        self.Interface_Init()
        self.Ui_Init()

        print('主线程ID',threading.current_thread().ident)#打印主线程的标识
        self.Serial_QThread = QThread()#为窗口w创建一个子线程
        self.Serial_QThread_Function = Serial_Qthread_function()#为窗口w创建串口函数实例
        self.Serial_QThread_Function.moveToThread(self.Serial_QThread)#将创建的线程实例移到子线程中
        self.Serial_QThread.start()#启动线程

        self.Serial_QThread_Function.signal_Serialstart_function.connect(self.Serial_QThread_Function.SerialInit_function)#将实例中的signal_Serialstart_function信号指向实例中的SerialInit_function函数
        self.Serial_QThread_Function.signal_Serialstart_function.emit()#触发signal_Serialstart_function信号
        
        self.Serial_QThread_Function.signal_pushButton_Open.connect(self.Serial_QThread_Function.slot_pushButton_Open)

        self.Serial_QThread_Function.signal_pushButton_Open_flag.connect(self.slot_pushButton_Open_flag)

        self.Serial_QThread_Function.signal_ReadData.connect(self.slot_ReadData)

        self.Serial_QThread_Function.signal_DTR.connect(self.Serial_QThread_Function.slot_DTR)
        self.Serial_QThread_Function.signal_TRS.connect(self.Serial_QThread_Function.slot_TRS)
        self.Serial_QThread_Function.signal_TimeView.connect(self.Serial_QThread_Function.slot_TimeView)

        self.port_name = []

        self.time_scan = QTimer()#创建一个定时器
        self.time_scan.timeout.connect(self.TimeOut_Scan)#触发的中断函数
        self.time_scan.start(1000)#启动定时器，并定时1s


    def TimeOut_Scan(self):
        '''
        中断函数
        '''
        availablePort = QSerialPortInfo.availablePorts()
        new_port = []
        for port in availablePort:
            new_port.append(port.portName())
        
        if len(self.port_name) != len(new_port):
            self.port_name = new_port
            self.ui.comboBox_Com.clear()
            self.ui.comboBox_Com.addItems(self.port_name)

    def Interface_Init(self):
        self.ui.comboBox_Baud.addItems(['4800','9600','57600','115200'])
        self.ui.comboBox_Stop.addItems(['1','1.5','2'])
        self.ui.comboBox_Data.addItems(['8','7','6','5'])
        self.ui.comboBox_Check.addItems(['None','Odd','Oven'])
        self.ui.checkBox_TRS.stateChanged.connect(self.checkBox_TRS)
        self.ui.checkBox_DTR.stateChanged.connect(self.checkBox_DTR)

    def Ui_Init(self):
        self.ui.pushButton_Open.clicked.connect(self.pushButton_Open)

    def pushButton_Open(self):
        self.set_parameter = {}
        self.set_parameter['comboBox_Com'] = self.ui.comboBox_Com.currentText()
        self.set_parameter['comboBox_Baud'] = self.ui.comboBox_Baud.currentText()
        self.set_parameter['comboBox_Data'] = self.ui.comboBox_Data.currentText()
        self.set_parameter['comboBox_Stop'] = self.ui.comboBox_Stop.currentText()
        self.set_parameter['comboBox_Check'] = self.ui.comboBox_Check.currentText()
        self.Serial_QThread_Function.signal_pushButton_Open.emit(self.set_parameter)

    def slot_pushButton_Open_flag(self,state):
        print('串口打开状态',state)
        if state == 2:
            self.ui.pushButton_Open.setText('打开串口')
            self.ui.pushButton_Open.setStyleSheet('color:black')
            self.time_scan.start(1000)

        if state == 1:
            self.ui.pushButton_Open.setStyleSheet('color:red')
            self.ui.pushButton_Open.setText('关闭串口')
            self.time_scan.stop()

        if state == 0:
            qw.QMessageBox.warning(self,'错误信息','串口已被占用，打开失败')

    def slot_ReadData(self,data):
        # print(data)

        if self.ui.checkBox_TimeView.isChecked():
            time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\r\n'
            self.ui.textEdit_receive.setTextColor(QColor('red'))
            self.ui.textEdit_receive.insertPlainText(time_str)
            self.ui.textEdit_receive.setTextColor(QColor('black'))

        Byte_data = bytes(data)
        print(Byte_data)
        if self.ui.checkBox_HexView.checkState():
            print('十六进制显示')
            View_data = ''
            for i in range(len(Byte_data)):
                View_data += '{:2x}'.format(Byte_data[i])+' '
            self.ui.textEdit_receive.insertPlainText(View_data)
        else:
            print('字符串显示')
            self.ui.textEdit_receive.insertPlainText(Byte_data.decode('utf-8','ignore'))
        self.ui.textEdit_receive.moveCursor(QTextCursor.End)

    def checkBox_TRS(self,state):
        self.Serial_QThread_Function.signal_TRS.emit(state)

    def checkBox_DTR(self,state):
        self.Serial_QThread_Function.signal_DTR.emit(state)

if __name__=='__main__':
    app = qw.QApplication(sys.argv)
    w = SerialForm()
    w.show()
    sys.exit(app.exec_())