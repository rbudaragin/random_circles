import sys

import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class DrawWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Разноцветные окружности')
        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(180, 60)
        self.btn.move(560, 260)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        rand = random.choice([int(i) for i in range(500)])
        qp.setBrush(QColor(random.choice([int(i) for i in range(256)]), random.choice([int(i) for i in range(256)]),
                           random.choice([int(i) for i in range(256)])))
        qp.drawEllipse(10, 10, rand, rand)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawWindow()
    ex.show()
    sys.exit(app.exec())
