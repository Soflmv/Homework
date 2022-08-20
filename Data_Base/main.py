import sys
from database import Ui_MainWindow
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets

data_list = []


class Data_Base(QtWidgets.QMainWindow):
    def __init__(self):
        super(Data_Base, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Name window
        self.setWindowTitle("Data Base")
        # Fixing the window and table
        self.setFixedSize(990, 580)
        self.setWindowIcon(QIcon("blue-icon.png"))
        # Hints to the user
        self.ui.Employeesearch.setPlaceholderText("Name and Surname")
        self.ui.NameSurname.setPlaceholderText("Name and Surname")
        self.ui.Height.setPlaceholderText("Height")
        self.ui.Weight.setPlaceholderText("Weight")
        self.ui.Car.setPlaceholderText("Car and model?")
        self.ui.City.setPlaceholderText("Your city?")
        # Buttons
        self.ui.Addaperson.clicked.connect(self.save_person)
        self.ui.Deleteaperson.clicked.connect(self.delete_person)
        self.ui.Search.clicked.connect(self.search_person)
        self.ui.NameSurname.text()
        self.ui.Datebirthday.date().toString("dd.MM.yyyy")
        self.ui.Height.text()
        self.ui.Weight.text()
        self.ui.Car.text()
        self.ui.Csharp.text()
        self.ui.Delphi.text()
        self.ui.Cplusplus.text()
        self.ui.Python.text()
        self.ui.JavaScript.text()
        self.ui.PHP.text()


    def save_person(self):

        row_index = 0
        for person in data_list:

            self.ui.table_data.setRowCount(len(data_list))
            self.ui.table_data.setItem(row_index, 0, QTableWidgetItem(str(person["name"])))
            self.ui.table_data.setItem(row_index, 1, QTableWidgetItem(str(person["birthday"])))
            self.ui.table_data.setItem(row_index, 2, QTableWidgetItem(str(person["height"])))
            self.ui.table_data.setItem(row_index, 3, QTableWidgetItem(str(person["weight"])))
            self.ui.table_data.setItem(row_index, 4, QTableWidgetItem(str(person["car"])))
            self.ui.table_data.setItem(row_index, 5, QTableWidgetItem(str(person["city"])))
            self.ui.table_data.setItem(row_index, 6, QTableWidgetItem(str(person["languages"])))

            row_index += 1

        rowCount = self.ui.table_data.rowCount()
        self.ui.table_data.insertRow(rowCount)
        self.ui.table_data.setItem(rowCount, 0, QTableWidgetItem(self.ui.NameSurname.text()))
        self.ui.table_data.setItem(rowCount, 1, QTableWidgetItem(self.ui.Datebirthday.date().toString("dd.MM.yyyy")))
        self.ui.table_data.setItem(rowCount, 2, QTableWidgetItem(self.ui.Height.text()))
        self.ui.table_data.setItem(rowCount, 3, QTableWidgetItem(self.ui.Weight.text()))
        self.ui.table_data.setItem(rowCount, 4, QTableWidgetItem(self.ui.Car.text()))
        self.ui.table_data.setItem(rowCount, 5, QTableWidgetItem(self.ui.City.text()))

        if self.ui.Csharp.isChecked():
            self.ui.table_data.setItem(rowCount, 6, QTableWidgetItem(self.ui.Csharp.text()))
        if self.ui.Delphi.isChecked():
            self.ui.table_data.setItem(rowCount, 6, QTableWidgetItem(self.ui.Delphi.text()))
        if self.ui.Cplusplus.isChecked():
            self.ui.table_data.setItem(rowCount, 6, QTableWidgetItem(self.ui.Cplusplus.text()))
        if self.ui.Python.isChecked():
            self.ui.table_data.setItem(rowCount, 6, QTableWidgetItem(self.ui.Python.text()))
        if self.ui.JavaScript.isChecked():
            self.ui.table_data.setItem(rowCount, 6, QTableWidgetItem(self.ui.JavaScript.text()))
        if self.ui.PHP.isChecked():
            self.ui.table_data.setItem(rowCount, 6, QTableWidgetItem(self.ui.PHP.text()))

        QMessageBox.information(self, "Data added", "You have successfully added the data to the database !")

    def delete_person(self):

        for del_name in self.ui.table_data.selectionModel().selectedRows():
            index = QtCore.QPersistentModelIndex(del_name)
            self.ui.table_data.removeRow(index.row())

        QMessageBox.information(self, "Delete data", "You have successfully deleted the data !")

    def search_person(self, key):
        name_search = self.ui.Employeesearch.text()

        for row in range(self.ui.table_data.rowCount()):
            matching_items = self.ui.table_data.findItems(name_search, Qt.MatchExactly)
            if matching_items:
                item = matching_items[0]
                item.setSelected(True)
                item.setForeground(QBrush(QColor(255, 0, 0)))
                self.ui.table_data.verticalScrollBar().setSliderPosition(row)

        QMessageBox.information(self, "Completed !", "Data search completed !")


app = QtWidgets.QApplication(sys.argv)
application = Data_Base()
application.show()
application.setWindowOpacity(0.95)
sys.exit(app.exec_())
