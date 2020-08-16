from PyQt5.QtWidgets import QMainWindow, QApplication
from design import Ui_MainWindow
import matplotlib.pyplot as plt
import numpy as np
from generator import y1, y2, teacher_time
from random import choice


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
        self.ui.teach_week.clicked.connect(lambda: self.graf_tadjyk3())
        self.ui.teach_month.clicked.connect(lambda: self.graf_tadjyk4())

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

    def graf_tadjyk3(self):
        lines = []
        labels = []
        number_of_colors = len(teacher_time)

        color = ["#" + ''.join([choice('0123456789ABCDEF') for j in range(6)])
                 for i in range(number_of_colors)]
        plt.title("Количество преподавателей в каждую неделю")
        for j, i in enumerate(teacher_time):
            x3 = teacher_time[i].keys()
            y3 = teacher_time[i].values()
            labels.append(i)
            a, = plt.plot(x3, y3, color=color[j])
            lines.append(a)
        plt.legend(lines, labels)

        plt.grid()
        # plt.savefig("tadjyk3.png")
        plt.show()

    def graf_tadjyk4(self):
        x4 = [l for l in range(1, 14)]
        y4 = []
        k = 0
        for i in range(1, 54):
            if i % 4 != 0:
                for j in teacher_time:
                    if i in teacher_time[j]:
                        k += teacher_time[j][i]
            else:
                y4.append(k)
                k = 0
        y4 = np.array(y4)
        x4 = np.array(x4)
        plt.title("Количество пар у преподавателей в месяц")
        plt.plot(x4, y4)
        plt.grid()
        plt.scatter(x4, y4)
        plt.show()


app = QApplication([y1, y2, teacher_time])
application = MyWindow()
application.setWindowTitle('Графики')
# application.setWindowIcon(QIcon('.\images\icon.ico'))
application.show()

exit(app.exec())
