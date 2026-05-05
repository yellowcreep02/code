from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QTextEdit,QPushButton
import sys


def init_widget(w:QWidget):
    layout = QVBoxLayout()

    def btn_clicked():
        print('按下按钮')

    button = QPushButton()
    button.setText('发射')
    #给按钮添加或关联点击事件（函数）
    button.clicked.connect(btn_clicked)
    layout.addWidget(button)

    w.setLayout(layout)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    init_widget(w)
    w.show()
    sys.exit(app.exec_())
