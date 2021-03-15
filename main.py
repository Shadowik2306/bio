import sys
import sqlite3
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from random import shuffle


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class WelcomWind(QMainWindow):
    def __init__(self):
        super(WelcomWind, self).__init__()
        uic.loadUi('data/Qt/WelcomeWind.ui', self)
        self.randomQuest.clicked.connect(self.random_quests)

    def random_quests(self):
        self.wind = TectWind()
        self.wind.show()
        self.close()


class TectWind(QMainWindow):
    def __init__(self, test=None):
        super(TectWind, self).__init__()
        uic.loadUi('data/Qt/TestWind.ui', self)
        self.test = test
        self.real_test = self.load_test(self.test)
        self.answer1.clicked.connect(self.check)
        self.process()

    def load_test(self, test):
        con = sqlite3.connect('data/sql/test.db')
        cur = con.cursor()
        lst = cur.execute('SELECT * FROM info').fetchall()
        shuffle(lst)
        return lst

    def process(self):
        if not self.real_test:
            self.real_test = self.load_test(self.test)
        self.now = self.real_test.pop(0)
        self.question = eval('"' + str(self.now[2] + '"'))
        self.label.setText(self.question)
        self.answers = self.now[3:7]
        print(self.answers)
        self.answer1.setText(self.answers[0])
        self.answer2.setText(self.answers[1])
        self.answer3.setText(self.answers[2])
        self.answer4.setText(self.answers[3])
        if self.now[7] == 1:
            text = self.answers[0]
        elif self.now[7] == 2:
            text = self.answers[1]
        elif self.now[7] == 3:
            text = self.answers[2]
        elif self.now[7] == 4:
            text = self.answers[3]
        self.right_answer = (self.now[7], text)
        print(self.right_answer)

    def check(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WelcomWind()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())