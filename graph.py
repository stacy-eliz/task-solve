from PyQt5.QtWidgets import QMainWindow, QApplication
from design import Ui_MainWindow
import matplotlib.pyplot as plt
import numpy as np
from generator import y1, y2

class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI1()
        self.update()

    def initUI1(self):
        self.ui.audit_month.clicked.connect(lambda: self.graf_tadjyk1(y1))
        self.ui.audit_week.clicked.connect(lambda: self.graf_tadjyk2(y2))

    def graf_tadjyk1(self, y1):
        x1 = [i for i in range(1, 27)]
        y1 = np.array(y1)
        x1 = np.array(x1)
        plt.title("Процентные данные загруженности аудиторий на каждые 4 недели")
        plt.plot(x1, y1)
        plt.scatter(x1, y1)
        plt.grid()
        # plt.savefig("tadjyk1.png")
        plt.show()

    def graf_tadjyk2(self, y2):
        x2 = [i for i in range(1, 54)]
        y2 = np.array(y2)
        x2 = np.array(x2)
        plt.title("Процентные данные загруженности аудиторий на каждую неделю")
        plt.plot(x2, y2)
        plt.scatter(x2, y2)
        plt.grid()
        # plt.savefig("tadjyk2.png")
        plt.show()


app = QApplication([y1, y2])
application = MyWindow()
application.setWindowTitle('Графики')
# application.setWindowIcon(QIcon('.\images\icon.ico'))
application.show()

exit(app.exec())
