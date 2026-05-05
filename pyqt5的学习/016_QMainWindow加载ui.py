from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMainWindow
import sys
from UI.Ui_my_main_window import Ui_MyMainWindow

class MyMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MyMainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.actionExit.triggered.connect(QApplication.quit)
        self.ui.actionRefresh.triggered.connect(self.on_refresh)

    def on_refresh(self):
        print('刷新')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyMainWindow()
    w.show()

    sys.exit(app.exec_())