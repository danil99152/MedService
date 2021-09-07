import ctypes
import os
import sys
from datetime import datetime

from PyQt5 import QtWidgets
import MedService
import requests as requests
import json

class MainService(QtWidgets.QMainWindow, MedService.Ui_MainWindow):
    user32 = ctypes.windll.user32
    width = int(user32.GetSystemMetrics(0) * 0.22)
    height = int(user32.GetSystemMetrics(1) * 0.64)
    y_start = 0
    med_id = ""

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.getResult.clicked.connect(lambda: self.getSymptoms(self.GettingSymptoms.toPlainText()))
        self.moveButton.clicked.connect(self.get_forward)
        self.GettingSymptoms.textChanged.connect(self.validate_input)
        self.clearSymptoms.clicked.connect(self.GettingSymptoms.clear)

    def get_forward(self):
        new_width = int(self.user32.GetSystemMetrics(0)*0.015)
        if self.expanded:
            width = int(self.user32.GetSystemMetrics(0) - self.width * 0.065)
            self.GettingSymptoms.hide()
            self.Result.hide()
            self.getResult.hide()
            self.clearSymptoms.hide()
            self.setFixedSize(new_width, self.height)
            self.move(width, self.y_start)
            self.moveButton.setText("<")
            self.expanded = False
        else:
            width = int(self.user32.GetSystemMetrics(0) - self.width)
            self.setFixedSize(self.width, self.height)
            self.GettingSymptoms.show()
            self.Result.show()
            self.getResult.show()
            self.clearSymptoms.show()
            self.move(width, self.y_start)
            self.moveButton.setText(">")
            self.expanded = True

    def validate_input(self):
        text = self.GettingSymptoms.toPlainText()
        if len(text.split(',')) >= 5:
            self.getResult.setText(self._translate("MainWindow", "Получить результат"))
        else: self.getResult.setText(self._translate("MainWindow", "Не менее 5 симптомов"))

    def logging(self, response):
        f = open("logs/log.txt", "a")
        if os.path.getsize('logs/log.txt') >= 10000000:
            os.remove('logs/log.txt')
        f.write(str(datetime.now().isoformat()) + ":\n")
        f.write("Status code: " + str(response.status_code) + "\n")
        f.write("Request processed: " + str(response.ok) + "\n")
        f.write("Content: " + response.text + "\n")
        f.close()

    def getSymptoms(self, symptoms): #Здесь вся обработка
        try:
            f = open("configs/config.json", "r")
            params = json.loads(f.read())
            f.close()
            data = {'user_id': self.med_id,
                    'symptoms': symptoms
                    }
            headers = {'Authorization': params['token'],
                       'Content-Type': 'application/json'
                       }
            url = 'https://top3.sbermed.ai/api/calls'
            try:
                response = requests.post(url,
                                         data=json.dumps(data),
                                         headers=headers
                                         )
                self.Result.clear()
                if params['write_log'] == "True":
                    try:
                        self.logging(response)
                    except:
                        os.mkdir("logs")
                        self.logging(response)
                if len(response.json()['diag']) == 0:
                    self.Result.addItem("Нет ответа из-за недостаточного количества данных или некорректного ввода")
                else:
                    for diag in response.json()['diag']:
                        self.Result.addItem(diag[0] + " " + diag[1])
            except Exception as e:
                f = open("logs/log.txt", "a")
                f.write(str(datetime.now().isoformat()) + ":\n")
                f.write("Exception: " + str(e) + ":\n")
                f.close()
        except Exception as e:
            self.Result.addItem(str(e))
            f = open("logs/log.txt", "a")
            f.write(str(datetime.now().isoformat()) + ":\n")
            f.write("Exception: " + str(e) + ":\n")
            f.close()

def main(med_id):
    MainService.med_id = med_id
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainService()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':
    try:
        med_id = sys.argv[1]
    except:
        med_id = "med-1-doctor-1"
    main(med_id)