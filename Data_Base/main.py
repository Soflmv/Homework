import sys
import json
from database import Ui_MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets


class Data_Base(QtWidgets.QMainWindow):
    def __init__(self):
        super(Data_Base, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Name window
        self.setWindowTitle("Data Base")
        # Fixing the window and table
        self.setFixedSize(960, 560)
        self.ui.table_data.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setWindowIcon(QIcon("blue-icon.png"))
        # Hints to the user
        self.ui.Employeesearch.setPlaceholderText("Name and Surname")
        self.ui.NameSurname.setPlaceholderText("Name and Surname")
        self.ui.Height.setPlaceholderText("Height")
        self.ui.Weight.setPlaceholderText("Weight")
        # Buttons
        self.ui.Addaperson.clicked.connect(self.save_person)
        self.ui.Deleteaperson.clicked.connect(self.delete_person)
        self.ui.Search.clicked.connect(self.search_person)

    def save_person(self):
        data_list = []
        row_index = 0
        for person in data_list:

            self.ui.table_data.setRowCount(len(data_list))
            self.ui.table_data.setItem(row_index, 0, QTableWidgetItem(str(person["name"])))
            self.ui.table_data.setItem(row_index, 1, QTableWidgetItem(str(person["birthday"])))
            self.ui.table_data.setItem(row_index, 2, QTableWidgetItem(str(person["height"])))
            self.ui.table_data.setItem(row_index, 3, QTableWidgetItem(str(person["weight"])))
            self.ui.table_data.setItem(row_index, 4, QTableWidgetItem(str(person["car"])))
            self.ui.table_data.setItem(row_index, 5, QTableWidgetItem(str(person["languages"])))

            row_index += 1

        name = self.ui.NameSurname.text()
        birhtday = self.ui.Datebirthday.date().toString("dd.MM.yyyy")
        height = self.ui.Height.text()
        weight = self.ui.Weight.text()
        yes_car = self.ui.YesCar.text()
        no_car = self.ui.NoCar.text()
        c_plus = self.ui.Cplusplus.text()
        csharp = self.ui.Csharp.text()
        delphi = self.ui.Delphi.text()
        python = self.ui.Python.text()

        if (name, birhtday, height, weight) is not None:
            rowCount = self.ui.table_data.rowCount()
            self.ui.table_data.insertRow(rowCount)
            self.ui.table_data.setItem(rowCount, 0, QTableWidgetItem(name))
            self.ui.table_data.setItem(rowCount, 1, QTableWidgetItem(birhtday))
            self.ui.table_data.setItem(rowCount, 2, QTableWidgetItem(height))
            self.ui.table_data.setItem(rowCount, 3, QTableWidgetItem(weight))
        if self.ui.YesCar.isChecked():
            self.ui.table_data.setItem(rowCount, 4, QTableWidgetItem(yes_car))
        if self.ui.NoCar.isChecked():
            self.ui.table_data.setItem(rowCount, 4, QTableWidgetItem(no_car))
        if self.ui.Cplusplus.isChecked():
            self.ui.table_data.setItem(rowCount, 5, QTableWidgetItem(c_plus))
        if self.ui.Csharp.isChecked():
            self.ui.table_data.setItem(rowCount, 5, QTableWidgetItem(csharp))
        if self.ui.Delphi.isChecked():
            self.ui.table_data.setItem(rowCount, 5, QTableWidgetItem(delphi))
        if self.ui.Python.isChecked():
            self.ui.table_data.setItem(rowCount, 5, QTableWidgetItem(python))

        QMessageBox.information(self, "Data added", "You have successfully added the data to the database !")

    def delete_person(self):

        for del_name in self.ui.table_data.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(del_name)
            self.ui.table_data.removeRow(index.row())

        QMessageBox.information(self, "Delete data", "You have successfully deleted the data !")

    def search_person(self):

        text = self.ui.Employeesearch.text()
        items = self.ui.table_data.findItems(text, Qt.MatchExactly)
        item = items[0]
        item.setSelected(True)
        item.setForeground(QBrush(QColor(255, 0, 0)))
        row = item.row()
        self.ui.table_data.verticalScrollBar().setSliderPosition(row)

        QMessageBox.information(self, "Completed !", "Data search completed !")


app = QtWidgets.QApplication(sys.argv)
application = Data_Base()
application.show()
application.setWindowOpacity(0.96)
sys.exit(app.exec_())
