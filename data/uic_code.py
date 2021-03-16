from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialogButtonBox


class Ui_Test_Wind(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(20, 15, 20, 15)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.answer1 = QtWidgets.QPushButton(self.centralwidget)
        self.answer1.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.answer1.setFont(font)
        self.answer1.setObjectName("answer1")
        self.gridLayout_3.addWidget(self.answer1, 1, 0, 1, 1)
        self.answer4 = QtWidgets.QPushButton(self.centralwidget)
        self.answer4.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.answer4.setFont(font)
        self.answer4.setObjectName("answer4")
        self.gridLayout_3.addWidget(self.answer4, 2, 1, 1, 1)
        self.answer2 = QtWidgets.QPushButton(self.centralwidget)
        self.answer2.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.answer2.setFont(font)
        self.answer2.setObjectName("answer2")
        self.gridLayout_3.addWidget(self.answer2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 2)
        self.answer3 = QtWidgets.QPushButton(self.centralwidget)
        self.answer3.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.answer3.setFont(font)
        self.answer3.setObjectName("answer3")
        self.gridLayout_3.addWidget(self.answer3, 2, 0, 1, 1)
        self.give_up = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.give_up.setFont(font)
        self.give_up.setObjectName("give_up")
        self.gridLayout_3.addWidget(self.give_up, 3, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.answer1.setText(_translate("MainWindow", "PushButton"))
        self.answer4.setText(_translate("MainWindow", "PushButton"))
        self.answer2.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow",
                                      "Какой метод позволяет избирательновыделять и изучать органоиды клетки?"))
        self.answer3.setText(_translate("MainWindow", "PushButton"))
        self.give_up.setText(_translate("MainWindow", "Пропустить"))
        self.pushButton.setText(_translate("MainWindow", "Выйти"))



class Ui_Result(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.answerText = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.answerText.setFont(font)
        self.answerText.setObjectName("answerText")
        self.gridLayout.addWidget(self.answerText, 0, 0, 1, 1)
        self.answer = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.answer.setFont(font)
        self.answer.setAlignment(QtCore.Qt.AlignCenter)
        self.answer.setObjectName("answer")
        self.gridLayout.addWidget(self.answer, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.answerText.setWordWrap(True)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.answerText.setText(_translate("Dialog", "Текст"))
        self.answer.setText(_translate("Dialog", "Ответ"))
        self.buttonBox.button(QDialogButtonBox.Ok).setText("Продолжить")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Закончить тест")