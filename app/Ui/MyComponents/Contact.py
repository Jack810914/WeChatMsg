from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Contact(QtWidgets.QPushButton):
    """
    联系人类，继承自pyqt的按钮，里面封装了联系人头像等标签
    """
    usernameSingal = pyqtSignal(str)

    def __init__(self, Ui, id=None, contact=None):
        super(Contact, self).__init__(Ui)
        self.layoutWidget = QtWidgets.QWidget(Ui)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout1 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout1.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout1.setContentsMargins(10, 10, 10, 10)
        self.gridLayout1.setSpacing(10)
        self.gridLayout1.setObjectName("gridLayout1")
        self.label_time = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_time.setFont(font)
        self.label_time.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_time.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_time.setObjectName("label_time")
        self.gridLayout1.addWidget(self.label_time, 0, 2, 1, 1)
        self.label_remark = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.label_remark.setFont(font)
        self.label_remark.setObjectName("label_remark")
        self.gridLayout1.addWidget(self.label_remark, 0, 1, 1, 1)
        self.label_msg = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_msg.setFont(font)
        self.label_msg.setObjectName("label_msg")
        self.gridLayout1.addWidget(self.label_msg, 1, 1, 1, 2)
        self.label_avatar = QtWidgets.QLabel(self.layoutWidget)
        self.label_avatar.setMinimumSize(QtCore.QSize(60, 60))
        self.label_avatar.setMaximumSize(QtCore.QSize(60, 60))
        self.label_avatar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_avatar.setAutoFillBackground(False)
        self.label_avatar.setStyleSheet("background-color: #ffffff;")
        self.label_avatar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_avatar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_avatar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_avatar.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_avatar.setObjectName("label_avatar")
        self.gridLayout1.addWidget(self.label_avatar, 0, 0, 2, 1)
        self.gridLayout1.setColumnStretch(0, 1)
        self.gridLayout1.setColumnStretch(1, 6)
        self.gridLayout1.setRowStretch(0, 5)
        self.gridLayout1.setRowStretch(1, 3)
        self.setLayout(self.gridLayout1)
        self.setStyleSheet(
            "QPushButton {background-color: rgb(220,220,220);}"
            "QPushButton:hover{background-color: rgb(208,208,208);}\n"
        )
        self.msgCount = contact[0]
        self.username = contact[1]
        self.conversationTime = contact[6]
        self.msgType = contact[7]
        self.digest = contact[8]
        hasTrunc = contact[10]
        attrflag = contact[11]
        if hasTrunc == 0:
            if attrflag == 0:
                self.digest = '[动画表情]'
            elif attrflag == 67108864:
                try:
                    remark = data.get_conRemark(contact[9])
                    msg = self.digest.split(':')[1].strip('\n').strip()
                    self.digest = f'{remark}:{msg}'
                except Exception as e:
                    pass
            else:
                pass
        self.show_info(id)

    def show_info(self, id):
        self.avatar = data.get_avator(self.username)
        # print(avatar)
        self.conRemark = data.get_conRemark(self.username)
        self.nickname, self.alias = data.get_nickname(self.username)
        time = datetime.now().strftime("%m-%d %H:%M")
        msg = '还没说话'
        pixmap = QPixmap(self.avatar).scaled(60, 60)  # 按指定路径找到图片
        self.label_avatar.setPixmap(pixmap)  # 在label上显示图片
        self.label_remark.setText(self.conRemark)
        self.label_msg.setText(self.digest)
        self.label_time.setText(data.timestamp2str(self.conversationTime)[2:])

    def show_msg(self):
        self.usernameSingal.emit(self.username)
