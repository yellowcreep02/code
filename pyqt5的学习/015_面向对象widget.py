from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
import sys

class mywidget(QWidget):

    def __init__(self,title):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(640,480)

        self.init_ui()

    def init_ui(self):
        btn = QPushButton("ciallo~",self)
        btn.clicked.connect(self.btn_click)

    def btn_click(self):
        print('ciallo~~~~')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = mywidget("你好世界")
    w.show()

    sys.exit(app.exec_())