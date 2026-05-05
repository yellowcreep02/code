from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
import sys
from UI.Ui_my_widget import Ui_Form

class mywidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.pushButton.clicked.connect(self.btn_click)
        
    def btn_click(self):
        print('ciallo~~~')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = mywidget()
    w.show()

    sys.exit(app.exec_())