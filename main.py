import sys
import sqlite3
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt
from random import shuffle
from data.uic_code import *


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class WelcomWind(QMainWindow):
    def __init__(self):
        super(WelcomWind, self).__init__()
        uic.loadUi('data/Qt/WelcomeWind.ui', self)
        self.randomQuest.clicked.connect(self.random_quests)
        self.choseTest.clicked.connect(self.chose)

    def random_quests(self):
        self.wind = TectWind()
        self.wind.show()
        self.close()

    def chose(self):
        self.wind = Select_Group()
        self.wind.show()
        self.close()


class TectWind(QMainWindow, Ui_Test_Wind):
    def __init__(self, test=None):
        super(TectWind, self).__init__()
        self.setupUi(self)
        self.test = test
        self.real_test = self.load_test(self.test)
        self.answer1.clicked.connect(self.check)
        self.answer2.clicked.connect(self.check)
        self.answer3.clicked.connect(self.check)
        self.answer4.clicked.connect(self.check)
        self.pushButton.clicked.connect(self.exit_to_main)
        self.give_up.clicked.connect(self.pas)
        self.process()

    def load_test(self, test):
        con = sqlite3.connect('data/sql/test.db')
        cur = con.cursor()
        if self.test is None:
            lst = cur.execute('SELECT * FROM info').fetchall()
        else:
            lst = cur.execute('SELECT * FROM info WHERE team = ?', (test,)).fetchall()
        shuffle(lst)
        return lst

    def process(self):
        if not self.real_test:
            self.real_test = self.load_test(self.test)
        self.now = self.real_test.pop(0)
        print(str(self.now))
        self.question = str(self.now[2]).capitalize()
        self.label.setText(self.question)
        self.answers = self.now[3:7]
        print(self.answers)
        self.answer1.setText(self.answers[0].capitalize())
        self.answer2.setText(self.answers[1].capitalize())
        self.answer3.setText(self.answers[2].capitalize())
        self.answer4.setText(self.answers[3].capitalize())
        text = ''
        if self.now[7] == 1:
            text = self.answers[0]
        elif self.now[7] == 2:
            text = self.answers[1]
        elif self.now[7] == 3:
            text = self.answers[2]
        elif self.now[7] == 4:
            text = self.answers[3]
        self.right_answer = (self.now[7], text)
        self.answer = eval('"' + str(self.now[8]) + '"'.replace(',', ',\n'))

    def pas(self):
        self.check(g=True)

    def check(self, g=False):
        k = None
        if g:
            k = False
        elif self.sender().objectName() == 'answer1' and self.right_answer[0] == 1:
            k = True
        elif self.sender().objectName() == 'answer2' and self.right_answer[0] == 2:
            k = True
        elif self.sender().objectName() == 'answer3' and self.right_answer[0] == 3:
            k = True
        elif self.sender().objectName() == 'answer4' and self.right_answer[0] == 4:
            k = True
        else:
            k = False
        self.wind = Right_answer(self.answer, self.right_answer, k)
        self.wind.show()
        k = self.wind.exec_()
        if k:
            self.process()
        else:
            self.exit_to_main()

    def exit_to_main(self):
        self.wind = WelcomWind()
        self.wind.show()
        self.close()


class Right_answer(QDialog, Ui_Result):
    def __init__(self, answer, right_answer, right):
        super(Right_answer, self).__init__()
        self.setupUi(self)
        self.answerText.setText(answer)
        if right:
            self.answer.setStyleSheet("color: green")
        else:
            self.answer.setStyleSheet("color: red")
        self.answer.setText(f'{right_answer[0]}: {right_answer[1]}')


class Select_Group(QMainWindow, Ui_Select_Group):
    def __init__(self):
        super(Select_Group, self).__init__()
        self.setupUi(self)
        self.selectGroup.buttonClicked.connect(self.connect)

    def connect(self, name):
        self.wind = TectWind(test=name.text())
        self.wind.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WelcomWind()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())