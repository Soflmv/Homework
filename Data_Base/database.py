# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'database.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 592)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:#22222e;")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(
            QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Employeedatabasetext = QtWidgets.QLabel(self.centralwidget)
        self.Employeedatabasetext.setGeometry(QtCore.QRect(470, 0, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(24)
        font.setItalic(False)
        self.Employeedatabasetext.setFont(font)
        self.Employeedatabasetext.setStyleSheet("color:#f08080")
        self.Employeedatabasetext.setObjectName("Employeedatabasetext")
        self.NameSurname = QtWidgets.QLineEdit(self.centralwidget)
        self.NameSurname.setGeometry(QtCore.QRect(10, 70, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.NameSurname.setFont(font)
        self.NameSurname.setStyleSheet(
            "background-color: #22222e;\n"
            "border:2px solid #f08080;\n"
            "border-radius:10;\n"
            "color:white"
        )
        self.NameSurname.setText("")
        self.NameSurname.setAlignment(QtCore.Qt.AlignCenter)
        self.NameSurname.setObjectName("NameSurname")
        self.Addaperson = QtWidgets.QPushButton(self.centralwidget)
        self.Addaperson.setGeometry(QtCore.QRect(50, 460, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Addaperson.setFont(font)
        self.Addaperson.setStyleSheet(
            "QPushButton {\n"
            "     border: 2px solid #8f8f91;\n"
            "     border-radius: 10px;\n"
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
            " }"
        )
        self.Addaperson.setObjectName("Addaperson")
        self.Deleteaperson = QtWidgets.QPushButton(self.centralwidget)
        self.Deleteaperson.setGeometry(QtCore.QRect(50, 510, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self.Deleteaperson.setFont(font)
        self.Deleteaperson.setStyleSheet(
            "QPushButton {\n"
            "     border: 2px solid #8f8f91;\n"
            "     border-radius: 10px;\n"
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
            " }"
        )
        self.Deleteaperson.setObjectName("Deleteaperson")
        self.Addanewemployeetext = QtWidgets.QLabel(self.centralwidget)
        self.Addanewemployeetext.setGeometry(QtCore.QRect(40, 40, 161, 24))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        font.setItalic(False)
        self.Addanewemployeetext.setFont(font)
        self.Addanewemployeetext.setStyleSheet("color:#f08080")
        self.Addanewemployeetext.setObjectName("Addanewemployeetext")
        self.Height = QtWidgets.QLineEdit(self.centralwidget)
        self.Height.setGeometry(QtCore.QRect(10, 160, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.Height.setFont(font)
        self.Height.setStyleSheet(
            "background-color: #22222e;\n"
            "border:2px solid #f08080;\n"
            "border-radius:10;\n"
            "color:white"
        )
        self.Height.setText("")
        self.Height.setAlignment(QtCore.Qt.AlignCenter)
        self.Height.setObjectName("Height")
        self.Weight = QtWidgets.QLineEdit(self.centralwidget)
        self.Weight.setGeometry(QtCore.QRect(10, 210, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.Weight.setFont(font)
        self.Weight.setStyleSheet(
            "background-color: #22222e;\n"
            "border:2px solid #f08080;\n"
            "border-radius:10;\n"
            "color:white"
        )
        self.Weight.setText("")
        self.Weight.setAlignment(QtCore.Qt.AlignCenter)
        self.Weight.setObjectName("Weight")
        self.Search = QtWidgets.QPushButton(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(480, 510, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self.Search.setFont(font)
        self.Search.setStyleSheet(
            "QPushButton {\n"
            "     border: 2px solid #8f8f91;\n"
            "     border-radius: 10px;\n"
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
            " }"
        )
        self.Search.setObjectName("Search")
        self.Employeesearch = QtWidgets.QLineEdit(self.centralwidget)
        self.Employeesearch.setGeometry(QtCore.QRect(250, 510, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.Employeesearch.setFont(font)
        self.Employeesearch.setStyleSheet(
            "background-color: #22222e;\n"
            "border:2px solid #f08080;\n"
            "border-radius:10;\n"
            "color:white"
        )
        self.Employeesearch.setText("")
        self.Employeesearch.setAlignment(QtCore.Qt.AlignCenter)
        self.Employeesearch.setObjectName("Employeesearch")
        self.Datebirthday = QtWidgets.QDateEdit(self.centralwidget)
        self.Datebirthday.setGeometry(QtCore.QRect(10, 120, 221, 22))
        self.Datebirthday.setStyleSheet(
            "background-color: #22222e;\n" "border:2px solid #f08080;\n" "color:white"
        )
        self.Datebirthday.setCalendarPopup(True)
        self.Datebirthday.setDate(QtCore.QDate(2009, 1, 2))
        self.Datebirthday.setObjectName("Datebirthday")
        self.table_data = QtWidgets.QTableWidget(self.centralwidget)
        self.table_data.setEnabled(True)
        self.table_data.setGeometry(QtCore.QRect(250, 40, 711, 451))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.table_data.setFont(font)
        self.table_data.setStyleSheet(
            "background-color:rgb(240, 242, 255);\n"
            "selection-background-color: rgb(82, 206, 225);\n"
            "selection-color: rgb(0, 0, 0);"
        )
        self.table_data.setRowCount(1)
        self.table_data.setColumnCount(7)
        self.table_data.setObjectName("table_data")
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.table_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.table_data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(6, item)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 360, 191, 81))
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.Csharp = QtWidgets.QRadioButton(self.groupBox)
        self.Csharp.setGeometry(QtCore.QRect(10, 10, 69, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Csharp.setFont(font)
        self.Csharp.setStyleSheet("color:white")
        self.Csharp.setObjectName("Csharp")
        self.Delphi = QtWidgets.QRadioButton(self.groupBox)
        self.Delphi.setGeometry(QtCore.QRect(10, 30, 69, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Delphi.setFont(font)
        self.Delphi.setStyleSheet("color:white")
        self.Delphi.setObjectName("Delphi")
        self.Cplusplus = QtWidgets.QRadioButton(self.groupBox)
        self.Cplusplus.setGeometry(QtCore.QRect(10, 50, 69, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cplusplus.setFont(font)
        self.Cplusplus.setStyleSheet("color:white")
        self.Cplusplus.setObjectName("Cplusplus")
        self.Python = QtWidgets.QRadioButton(self.groupBox)
        self.Python.setGeometry(QtCore.QRect(90, 10, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Python.setFont(font)
        self.Python.setStyleSheet("color:white")
        self.Python.setObjectName("Python")
        self.JavaScript = QtWidgets.QRadioButton(self.groupBox)
        self.JavaScript.setGeometry(QtCore.QRect(90, 30, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.JavaScript.setFont(font)
        self.JavaScript.setStyleSheet("color:white")
        self.JavaScript.setObjectName("JavaScript")
        self.PHP = QtWidgets.QRadioButton(self.groupBox)
        self.PHP.setGeometry(QtCore.QRect(90, 50, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PHP.setFont(font)
        self.PHP.setStyleSheet("color:white")
        self.PHP.setObjectName("PHP")
        self.Car = QtWidgets.QLineEdit(self.centralwidget)
        self.Car.setGeometry(QtCore.QRect(10, 260, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.Car.setFont(font)
        self.Car.setStyleSheet(
            "background-color: #22222e;\n"
            "border:2px solid #f08080;\n"
            "border-radius:10;\n"
            "color:white"
        )
        self.Car.setText("")
        self.Car.setAlignment(QtCore.Qt.AlignCenter)
        self.Car.setObjectName("Car")
        self.Addfile = QtWidgets.QPushButton(self.centralwidget)
        self.Addfile.setGeometry(QtCore.QRect(710, 510, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self.Addfile.setFont(font)
        self.Addfile.setStyleSheet(
            "QPushButton {\n"
            "     border: 2px solid #8f8f91;\n"
            "     border-radius: 10px;\n"
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
            " }"
        )
        self.Addfile.setObjectName("Addfile")
        self.City = QtWidgets.QLineEdit(self.centralwidget)
        self.City.setGeometry(QtCore.QRect(10, 310, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        self.City.setFont(font)
        self.City.setStyleSheet(
            "background-color: #22222e;\n"
            "border:2px solid #f08080;\n"
            "border-radius:10;\n"
            "color:white"
        )
        self.City.setText("")
        self.City.setAlignment(QtCore.Qt.AlignCenter)
        self.City.setObjectName("City")
        self.Savefile = QtWidgets.QPushButton(self.centralwidget)
        self.Savefile.setGeometry(QtCore.QRect(840, 510, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self.Savefile.setFont(font)
        self.Savefile.setStyleSheet(
            "QPushButton {\n"
            "     border: 2px solid #8f8f91;\n"
            "     border-radius: 10px;\n"
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
            " }"
        )
        self.Savefile.setObjectName("Savefile")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DataBase"))
        self.Employeedatabasetext.setText(_translate("MainWindow", "Database"))
        self.Addaperson.setText(_translate("MainWindow", "Add a person"))
        self.Deleteaperson.setText(_translate("MainWindow", "Delete a person"))
        self.Addanewemployeetext.setText(_translate("MainWindow", "Add a new employee"))
        self.Search.setText(_translate("MainWindow", "Search"))
        item = self.table_data.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table_data.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Birhtday"))
        item = self.table_data.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Height"))
        item = self.table_data.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Weihgt"))
        item = self.table_data.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Car"))
        item = self.table_data.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Сity"))
        item = self.table_data.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "languages"))
        self.Csharp.setText(_translate("MainWindow", "C#"))
        self.Delphi.setText(_translate("MainWindow", "Delphi"))
        self.Cplusplus.setText(_translate("MainWindow", "C++"))
        self.Python.setText(_translate("MainWindow", "Python"))
        self.JavaScript.setText(_translate("MainWindow", "JavaScript"))
        self.PHP.setText(_translate("MainWindow", "PHP"))
        self.Addfile.setText(_translate("MainWindow", "Add file"))
        self.Savefile.setText(_translate("MainWindow", "Save file"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
