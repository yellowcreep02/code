import PyQt5.QtWidgets as qw
import test 
import sys

class Instruments(qw.QWidget):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w = test.MyWindow()
    w.show()
    sys.exit(app.exec_())

