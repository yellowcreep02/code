import pyvisa
import serial.tools.list_ports 
from binascii import a2b_hex,b2a_hex

def get_serial_port_list():
    port_list_temp = list(serial.tools.list_ports.comports())
    if len(port_list_temp) == 0:
        print("No available serial port!")
        return False
    else:
        print("Available serial ports exist:")
        for my_port in port_list_temp:
            print(my_port)
        return True

get_serial_port_list()

class Device_name:
    def __init__(self):
        self.device_name = "Device_name"
        print(self.device_name)
 
    def list_ports(self):
        self.port_list = get_serial_port_list()
        return True
 
    def open_port(self,portx):
 
        port_temp = portx.split()
        port = port_temp[0]
 
        self.successful = False
        bps = 9600
        timeout = 1
        stopbits = 1
        bytesize = 8
        parity = 'N'
 
        try:
 
            self.ser = serial.Serial(port, bps, timeout=timeout, stopbits=stopbits, bytesize=bytesize, parity=my_parity)
 
            if (self.ser.is_open):
                self.successful = True
                th = threading.Thread(target=read_from_serial_port, args=(self.ser,)) 
                 # 创建一个子线程去等待读数据
                th.start()
        except Exception:
            print("open_serial_port error!")
 
        return self.successful
 
 
    def write_code(self,text):
        if self.successful == True:
            byte_num_sent = self.ser.write(a2b_hex(text))
 
    def read_code(self,text):
         if self.ser.in_waiting:
            data = b2a_hex(self.ser.read(self.ser.in_waiting)).decode('utf-8')
 
    def close_port(self):
        self.ser.close()




# class VisaInstrument:
#     def __init__(self, address: str):
#         self.address = address
#         self.rm = pyvisa.ResourceManager()
#         self.inst = None

#     def __enter__(self):
#         self.open()
#         return self

#     def __exit__(self, *args):
#         self.close()

#     def open(self):
#         self.inst = self.rm.open_resource(self.address)
#         self.inst.timeout = 3000
#         self.inst.read_termination = "\n"
#         self.inst.write_termination = "\n"

#     def write(self, cmd: str):
#         self.inst.write(cmd)

#     def query(self, cmd: str) -> str:
#         return self.inst.query(cmd).strip()

#     def close(self):
#         if self.inst:
#             self.inst.close()

# with VisaInstrument('ASRL1::INSTR') as inst:
#     print('666')



'''
class 串口通信:
    def __init__(self, 资源字符串: str, 波特率: int = 9600):
        self.资源字符串 = 资源字符串
        self.波特率 = 波特率
        self.资源管理器 = None
        self.仪器 = None
    def 连接(self):
        try:
            self.资源管理器 = pyvisa.ResourceManager()
            self.仪器 = self.资源管理器.open_resource(self.资源字符串)
            self.仪器.baud_rate = self.波特率
            return True
        except Exception as e:
            raise ConnectionError(f"串口连接失败: {e}")
    def 断开(self):
        if self.仪器:
            self.仪器.close()
        if self.资源管理器:
            self.资源管理器.close()
    def 发送(self, 命令: str):
        if not self.仪器:
            raise ConnectionError("未连接到仪器")
        self.仪器.write(命令)
    def 查询(self, 命令: str) -> str:
        if not self.仪器:
            raise ConnectionError("未连接到仪器")
        return self.仪器.query(命令).strip()
'''
