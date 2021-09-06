import ctypes
from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    _translate = QtCore.QCoreApplication.translate
    expanded = False
    def setupUi(self, MainWindow):
        width = 21
        height = 493
        user32 = ctypes.windll.user32
        MainWindow.move(int(user32.GetSystemMetrics(0) - width), 0)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(width, height)
        self.moveButton = QtWidgets.QPushButton(MainWindow)
        self.moveButton.setGeometry(QtCore.QRect(0, 0, 21, 491))
        self.moveButton.setObjectName("expand")
        self.GettingSymptoms = QtWidgets.QTextEdit(MainWindow)
        self.GettingSymptoms.setGeometry(QtCore.QRect(20, 0, 291, 231))
        self.GettingSymptoms.setObjectName("textEdit")
        self.Result = QtWidgets.QListWidget(MainWindow)
        self.Result.setGeometry(QtCore.QRect(20, 260, 291, 231))
        self.Result.setObjectName("listWidget")
        self.Result.setWordWrap(True)
        self.getResult = QtWidgets.QPushButton(MainWindow)
        self.getResult.setGeometry(QtCore.QRect(20, 230, 146, 31))
        self.getResult.setObjectName("getResult")
        self.clearSymptoms = QtWidgets.QPushButton(MainWindow)
        self.clearSymptoms.setGeometry(QtCore.QRect(165, 230, 146, 31))
        self.clearSymptoms.setObjectName("clearSymptoms")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(self._translate("MainWindow", "MedService"))
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        MainWindow.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.moveButton.setText("<")
        self.getResult.setText(self._translate("MainWindow", "Не менее 6 симптомов"))
        self.clearSymptoms.setText(self._translate("MainWindow", "Очистить поле ввода"))
        self.GettingSymptoms.hide()
        self.Result.hide()
        self.getResult.hide()
        self.clearSymptoms.hide()