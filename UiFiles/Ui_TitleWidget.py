# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\QtSkin\UiFiles\TitleWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TitleWidget(object):
    def setupUi(self, TitleWidget):
        TitleWidget.setObjectName("TitleWidget")
        TitleWidget.resize(798, 28)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TitleWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelTitle = QtWidgets.QLabel(TitleWidget)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.horizontalLayout.addWidget(self.labelTitle)
        spacerItem1 = QtWidgets.QSpacerItem(92, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonLogin = QtWidgets.QPushButton(TitleWidget)
        self.buttonLogin.setObjectName("buttonLogin")
        self.horizontalLayout.addWidget(self.buttonLogin)
        self.lineLogin = QtWidgets.QFrame(TitleWidget)
        self.lineLogin.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lineLogin.setLineWidth(2)
        self.lineLogin.setFrameShape(QtWidgets.QFrame.VLine)
        self.lineLogin.setObjectName("lineLogin")
        self.horizontalLayout.addWidget(self.lineLogin)
        spacerItem2 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.buttonMin = QtWidgets.QPushButton(TitleWidget)
        self.buttonMin.setObjectName("buttonMin")
        self.horizontalLayout.addWidget(self.buttonMin)
        self.buttonNorMax = QtWidgets.QPushButton(TitleWidget)
        self.buttonNorMax.setObjectName("buttonNorMax")
        self.horizontalLayout.addWidget(self.buttonNorMax)
        self.buttonClose = QtWidgets.QPushButton(TitleWidget)
        self.buttonClose.setObjectName("buttonClose")
        self.horizontalLayout.addWidget(self.buttonClose)

        self.retranslateUi(TitleWidget)
        QtCore.QMetaObject.connectSlotsByName(TitleWidget)

    def retranslateUi(self, TitleWidget):
        _translate = QtCore.QCoreApplication.translate
        TitleWidget.setWindowTitle(_translate("TitleWidget", "TitleWidget"))
        self.labelTitle.setText(_translate("TitleWidget", "Qt Skin Designer"))
        self.buttonLogin.setText(_translate("TitleWidget", "Login"))
        self.buttonMin.setText(_translate("TitleWidget", "0"))
        self.buttonNorMax.setText(_translate("TitleWidget", "1"))
        self.buttonClose.setText(_translate("TitleWidget", "r"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TitleWidget = QtWidgets.QWidget()
    ui = Ui_TitleWidget()
    ui.setupUi(TitleWidget)
    TitleWidget.show()
    sys.exit(app.exec_())

