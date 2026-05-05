from PyQt5.QtWidgets import *
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 创建界面（相当于你在 Designer 里画的）
        self.setWindowTitle("设备管理")
        self.resize(500, 300)
        
        # 中央部件
        central = QWidget()
        self.setCentralWidget(central)
        
        # 垂直布局
        layout = QVBoxLayout(central)
        
        # 1. 添加按钮（在 Designer 里拖的）
        self.btn_add = QPushButton("➕ 添加设备")
        self.btn_add.clicked.connect(self.add_row)
        
        # 2. 表格（在 Designer 里拖的）
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["设备名", "连接方式", "操作"])
        self.table.horizontalHeader().setStretchLastSection(True)
        
        layout.addWidget(self.btn_add)
        layout.addWidget(self.table)
    
    def add_row(self):
        """每次点击，添加一行并嵌入控件"""
        row = self.table.rowCount()
        self.table.insertRow(row)
        
        # 🔥 关键：在这里把控件“塞进”表格单元格
        # 第0列：设备名输入框
        self.table.setCellWidget(row, 0, QLineEdit())
        
        # 第1列：连接方式下拉框
        combo = QComboBox()
        combo.addItems(["串口", "TCP/IP", "USB"])
        self.table.setCellWidget(row, 1, combo)
        
        # 第2列：连接按钮（这就是你要的“对应仪器按钮”）
        btn = QPushButton("连接")
        btn.clicked.connect(lambda _, r=row: self.on_connect_clicked(r))
        self.table.setCellWidget(row, 2, btn)
    
    def on_connect_clicked(self, row):
        print(f"点击了第 {row} 行的连接按钮")
        # 获取这一行的设备名
        device_name = self.table.cellWidget(row, 0).text()
        print(f"设备名: {device_name}")

# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# sys.exit(app.exec_())