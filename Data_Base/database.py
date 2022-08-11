import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 614)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:#22222e;")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Employeedatabasetext = QtWidgets.QLabel(self.centralwidget)
        self.Employeedatabasetext.setGeometry(QtCore.QRect(290, 10, 301, 30))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(24)
        font.setItalic(False)
        self.Employeedatabasetext.setFont(font)
        self.Employeedatabasetext.setStyleSheet("color:#f08080")
        self.Employeedatabasetext.setObjectName("Employeedatabasetext")
        self.NameSurname = QtWidgets.QLineEdit(self.centralwidget)
        self.NameSurname.setGeometry(QtCore.QRect(30, 60, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.NameSurname.setFont(font)
        self.NameSurname.setStyleSheet("background-color: #22222e;\n"
                                        "border:2px solid #f08080;\n"
                                        "border-radius:10;\n"
                                        "color:white")
        self.NameSurname.setText("")
        self.NameSurname.setAlignment(QtCore.Qt.AlignCenter)
        self.NameSurname.setObjectName("NameSurname")
        self.Cplusplus = QtWidgets.QRadioButton(self.centralwidget)
        self.Cplusplus.setGeometry(QtCore.QRect(40, 380, 47, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cplusplus.setFont(font)
        self.Cplusplus.setStyleSheet("color:white")
        self.Cplusplus.setObjectName("Cplusplus")
        self.Delphi = QtWidgets.QRadioButton(self.centralwidget)
        self.Delphi.setGeometry(QtCore.QRect(40, 410, 58, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Delphi.setFont(font)
        self.Delphi.setStyleSheet("color:white")
        self.Delphi.setObjectName("Delphi")
        self.Csharp = QtWidgets.QRadioButton(self.centralwidget)
        self.Csharp.setGeometry(QtCore.QRect(40, 440, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Csharp.setFont(font)
        self.Csharp.setStyleSheet("color:white")
        self.Csharp.setObjectName("Csharp")
        self.Python = QtWidgets.QRadioButton(self.centralwidget)
        self.Python.setGeometry(QtCore.QRect(40, 470, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Python.setFont(font)
        self.Python.setStyleSheet("color:white")
        self.Python.setObjectName("Python")
        self.YesCar = QtWidgets.QCheckBox(self.centralwidget)
        self.YesCar.setGeometry(QtCore.QRect(40, 320, 43, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.YesCar.setFont(font)
        self.YesCar.setStyleSheet("color:white")
        self.YesCar.setObjectName("YesCar")
        self.Addaperson = QtWidgets.QPushButton(self.centralwidget)
        self.Addaperson.setGeometry(QtCore.QRect(40, 510, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Addaperson.setFont(font)
        self.Addaperson.setStyleSheet("QPushButton {\n"
                                        "     border: 2px solid #8f8f91;\n"
                                        "     border-radius: 8px;\n"
                                        "     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                        "     min-width: 80px;\n"
                                        " }\n"
                                        "\n"
                                        " QPushButton:pressed {\n"
                                        "     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                        " }\n"
                                        "\n"
                                        " QPushButton:flat {\n"
                                        "     border: none; /* для плоской кнопки границы нет */\n"
                                        " }\n"
                                        "\n"
                                        " QPushButton:default {\n"
                                        "     border-color: navy; /* делаем кнопку по умолчанию выпуклой */\n"
                                        " }")
        self.Addaperson.setObjectName("Addaperson")
        self.Deleteaperson = QtWidgets.QPushButton(self.centralwidget)
        self.Deleteaperson.setGeometry(QtCore.QRect(290, 510, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self.Deleteaperson.setFont(font)
        self.Deleteaperson.setStyleSheet("QPushButton {\n"
                                            "     border: 2px solid #8f8f91;\n"
                                            "     border-radius: 8px;\n"
                                            "     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                            "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                            "     min-width: 80px;\n"
                                            " }\n"
                                            "\n"
                                            " QPushButton:pressed {\n"
                                            "     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                            "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                            " }\n"
                                            "\n"
                                            " QPushButton:flat {\n"
                                            "     border: none; /* для плоской кнопки границы нет */\n"
                                            " }\n"
                                            "\n"
                                            " QPushButton:default {\n"
                                            "     border-color: navy; /* делаем кнопку по умолчанию выпуклой */\n"
                                            " }")
        self.Deleteaperson.setObjectName("Deleteaperson")
        self.Doyouhaveacartext = QtWidgets.QLabel(self.centralwidget)
        self.Doyouhaveacartext.setGeometry(QtCore.QRect(40, 290, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(10)
        font.setItalic(False)
        self.Doyouhaveacartext.setFont(font)
        self.Doyouhaveacartext.setStyleSheet("color:#f08080")
        self.Doyouhaveacartext.setObjectName("Doyouhaveacartext")
        self.ProgrammingLanguagetext = QtWidgets.QLabel(self.centralwidget)
        self.ProgrammingLanguagetext.setGeometry(QtCore.QRect(40, 350, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(10)
        font.setItalic(False)
        self.ProgrammingLanguagetext.setFont(font)
        self.ProgrammingLanguagetext.setStyleSheet("color:#f08080")
        self.ProgrammingLanguagetext.setObjectName("ProgrammingLanguagetext")
        self.NoCar = QtWidgets.QCheckBox(self.centralwidget)
        self.NoCar.setGeometry(QtCore.QRect(110, 320, 38, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NoCar.setFont(font)
        self.NoCar.setStyleSheet("color:white")
        self.NoCar.setObjectName("NoCar")
        self.Addanewemployeetext = QtWidgets.QLabel(self.centralwidget)
        self.Addanewemployeetext.setGeometry(QtCore.QRect(30, 20, 183, 24))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(14)
        font.setItalic(False)
        self.Addanewemployeetext.setFont(font)
        self.Addanewemployeetext.setStyleSheet("color:#f08080")
        self.Addanewemployeetext.setObjectName("Addanewemployeetext")
        self.Height = QtWidgets.QLineEdit(self.centralwidget)
        self.Height.setGeometry(QtCore.QRect(30, 190, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.Height.setFont(font)
        self.Height.setStyleSheet("background-color: #22222e;\n"
                                    "border:2px solid #f08080;\n"
                                    "border-radius:10;\n"
                                    "color:white")
        self.Height.setText("")
        self.Height.setAlignment(QtCore.Qt.AlignCenter)
        self.Height.setObjectName("Height")
        self.Weight = QtWidgets.QLineEdit(self.centralwidget)
        self.Weight.setGeometry(QtCore.QRect(30, 230, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.Weight.setFont(font)
        self.Weight.setStyleSheet("background-color: #22222e;\n"
                                    "border:2px solid #f08080;\n"
                                    "border-radius:10;\n"
                                    "color:white")
        self.Weight.setText("")
        self.Weight.setAlignment(QtCore.Qt.AlignCenter)
        self.Weight.setObjectName("Weight")
        self.Deleteanemployee = QtWidgets.QLineEdit(self.centralwidget)
        self.Deleteanemployee.setGeometry(QtCore.QRect(290, 470, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.Deleteanemployee.setFont(font)
        self.Deleteanemployee.setStyleSheet("background-color: #22222e;\n"
                                            "border:2px solid #f08080;\n"
                                            "border-radius:10;\n"
                                            "color:white")
        self.Deleteanemployee.setText("")
        self.Deleteanemployee.setAlignment(QtCore.Qt.AlignCenter)
        self.Deleteanemployee.setObjectName("Deleteanemployee")
        self.Deleteanemployeetext = QtWidgets.QLabel(self.centralwidget)
        self.Deleteanemployeetext.setGeometry(QtCore.QRect(290, 430, 178, 24))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(14)
        font.setItalic(False)
        self.Deleteanemployeetext.setFont(font)
        self.Deleteanemployeetext.setStyleSheet("color:#f08080")
        self.Deleteanemployeetext.setObjectName("Deleteanemployeetext")
        self.Search = QtWidgets.QPushButton(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(620, 510, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self.Search.setFont(font)
        self.Search.setStyleSheet("QPushButton {\n"
                                    "     border: 2px solid #8f8f91;\n"
                                    "     border-radius: 8px;\n"
                                    "     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                    "                                       stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                    "     min-width: 80px;\n"
                                    " }\n"
                                    "\n"
                                    " QPushButton:pressed {\n"
                                    "     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                    "                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                    " }\n"
                                    "\n"
                                    " QPushButton:flat {\n"
                                    "     border: none; /* для плоской кнопки границы нет */\n"
                                    " }\n"
                                    "\n"
                                    " QPushButton:default {\n"
                                    "     border-color: navy; /* делаем кнопку по умолчанию выпуклой */\n"
                                    " }")
        self.Search.setObjectName("Search")
        self.Employeesearch = QtWidgets.QLineEdit(self.centralwidget)
        self.Employeesearch.setGeometry(QtCore.QRect(610, 470, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.Employeesearch.setFont(font)
        self.Employeesearch.setStyleSheet("background-color: #22222e;\n"
                                            "border:2px solid #f08080;\n"
                                            "border-radius:10;\n"
                                            "color:white")
        self.Employeesearch.setText("")
        self.Employeesearch.setAlignment(QtCore.Qt.AlignCenter)
        self.Employeesearch.setObjectName("Employeesearch")
        self.Employeesearchtext = QtWidgets.QLabel(self.centralwidget)
        self.Employeesearchtext.setGeometry(QtCore.QRect(620, 430, 152, 24))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Employeesearchtext.setFont(font)
        self.Employeesearchtext.setStyleSheet("color:#f08080")
        self.Employeesearchtext.setObjectName("Employeesearchtext")
        self.Datebirthday = QtWidgets.QDateEdit(self.centralwidget)
        self.Datebirthday.setGeometry(QtCore.QRect(30, 150, 221, 22))
        self.Datebirthday.setStyleSheet("background-color: #22222e;\n"
                                        "border:2px solid #f08080;\n"
                                        "color:white")
        self.Datebirthday.setObjectName("Datebirthday")
        self.Addabirhdaytext = QtWidgets.QLabel(self.centralwidget)
        self.Addabirhdaytext.setGeometry(QtCore.QRect(30, 110, 128, 24))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(14)
        font.setItalic(False)
        self.Addabirhdaytext.setFont(font)
        self.Addabirhdaytext.setStyleSheet("color:#f08080")
        self.Addabirhdaytext.setObjectName("Addabirhdaytext")
        self.Tabledatabase = QtWidgets.QTableView(self.centralwidget)
        self.Tabledatabase.setGeometry(QtCore.QRect(295, 51, 741, 371))
        self.Tabledatabase.setObjectName("Tabledatabase")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DataBase"))
        self.Employeedatabasetext.setText(_translate("MainWindow", "Employee database"))
        self.Cplusplus.setText(_translate("MainWindow", "C++"))
        self.Delphi.setText(_translate("MainWindow", "Delphi"))
        self.Csharp.setText(_translate("MainWindow", "C#"))
        self.Python.setText(_translate("MainWindow", "Python"))
        self.YesCar.setText(_translate("MainWindow", "Yes"))
        self.Addaperson.setText(_translate("MainWindow", "Add a person"))
        self.Deleteaperson.setText(_translate("MainWindow", "Delete a person"))
        self.Doyouhaveacartext.setText(_translate("MainWindow", "Do you have a car ?"))
        self.ProgrammingLanguagetext.setText(_translate("MainWindow", "Programming language?"))
        self.NoCar.setText(_translate("MainWindow", "No"))
        self.Addanewemployeetext.setText(_translate("MainWindow", "Add a new employee"))
        self.Deleteanemployeetext.setText(_translate("MainWindow", "Delete an employee"))
        self.Search.setText(_translate("MainWindow", "Search"))
        self.Employeesearchtext.setText(_translate("MainWindow", "Employee search"))
        self.Addabirhdaytext.setText(_translate("MainWindow", "Add a birthday"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
