import pyvisa
import serial.tools.list_ports
from binascii import a2b_hex,b2a_hex
import threading

#获取串口号
com_list = []
for port in serial.tools.list_ports.comports():
    com_list.append(port)
    print(port)

class connect_com:
    def __init__(self):
        pass

    def com_open(self,com_info):
        try:
            self.ser = serial.Seiral(**com_info)

            if self.ser.is_open:
                th = threading.Thread()
                print('打开成功')
        except Exception as e:
            print('com连接失败')


      