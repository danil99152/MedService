import sys
from PyQt5 import QtWidgets
import MedService
import requests as requests
import json

class MainService(QtWidgets.QMainWindow, MedService.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(lambda: self.getSymptoms(self.GettingSymptoms.toPlainText()))

    def getSymptoms(self, symptoms): #Здесь вся обработка
        data = {'user_id': 'med-1-doctor-1',
                'symptoms': symptoms
                }
        headers = {'Authorization': 'ae8e8b3e727ab44b014f9e5285348c59b67d27c56fa3d32d04d1709d9e37703a',
                   'Content-Type': 'application/json'
                   }
        url = 'https://top3.sbermed.ai/api/calls'
        response = requests.post(url,
                                 data=json.dumps(data),
                                 headers=headers
                                 )
        for diag in response.json()['diag']:
            self.Result.addItem(diag[1])

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainService()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':
    main()