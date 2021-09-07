import ctypes
from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    _translate = QtCore.QCoreApplication.translate
    expanded = False
    def setupUi(self, MainWindow):
        user32 = ctypes.windll.user32
        x_increase = user32.GetSystemMetrics(0)/1366
        y_increase = user32.GetSystemMetrics(1)/768
        width = int(user32.GetSystemMetrics(0)*0.015)
        height = int(user32.GetSystemMetrics(1)*0.64)
        MainWindow.move(int(user32.GetSystemMetrics(0) - width), 0)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(width, height)
        self.moveButton = QtWidgets.QPushButton(MainWindow)
        self.moveButton.setGeometry(QtCore.QRect(0, 0, 21*x_increase, 491*y_increase))
        self.moveButton.setObjectName("expand")
        self.GettingSymptoms = QtWidgets.QTextEdit(MainWindow)
        self.GettingSymptoms.setGeometry(QtCore.QRect(20*x_increase, 0, 291*x_increase, 231*y_increase))
        self.GettingSymptoms.setObjectName("textEdit")
        self.Result = QtWidgets.QListWidget(MainWindow)
        self.Result.setGeometry(QtCore.QRect(20*x_increase, 260*y_increase, 291*x_increase, 231*y_increase))
        self.Result.setObjectName("listWidget")
        self.Result.setWordWrap(True)
        self.getResult = QtWidgets.QPushButton(MainWindow)
        self.getResult.setGeometry(QtCore.QRect(20*x_increase, 230*y_increase, 146*x_increase, 31*y_increase))
        self.getResult.setObjectName("getResult")
        self.clearSymptoms = QtWidgets.QPushButton(MainWindow)
        self.clearSymptoms.setGeometry(QtCore.QRect(165*x_increase, 230*y_increase, 146*x_increase, 31*y_increase))
        self.clearSymptoms.setObjectName("clearSymptoms")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(self._translate("MainWindow", "Топ-3 диагнозов"))
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        MainWindow.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.moveButton.setText("<")
        self.getResult.setText(self._translate("MainWindow", "Не менее 6 симптомов"))
        self.clearSymptoms.setText(self._translate("MainWindow", "Очистить поле ввода"))
        self.GettingSymptoms.hide()
        self.Result.hide()
        self.getResult.hide()
        self.clearSymptoms.hide()