from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QVBoxLayout,QTextEdit
import sys


def init_widget(w:QWidget):
    #创建垂直排列的布局Vertical
    layout = QVBoxLayout()

    edit = QLineEdit()
    edit.setPlaceholderText('请输入账号')
    edit.setText('yellowcreep')
    #设置输入框最大字符数
    edit.setMaxLength(10)
    layout.addWidget(edit)

    print(edit.text())    

    edit_pwd = QLineEdit()
    edit_pwd.setPlaceholderText('请输入密码')
    #设置内容的显示模式
    edit_pwd.setEchoMode(QLineEdit.Password)
    layout.addWidget(edit_pwd)

    #多行文本输入------------------------------------
    text_edit = QTextEdit()
    text_edit.setPlaceholderText('请输入个人介绍')

    #设置文本内容
    text_edit.setPlainText('我叫xxx,来自xxx')
    #获取已经输入的内容
    print(text_edit.toPlainText())
    layout.addWidget(text_edit)

    w.setLayout(layout)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    init_widget(w)
    w.show()
    sys.exit(app.exec_())
