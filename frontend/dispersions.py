from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5 import uic

import numpy as np

class Dispersions(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi("frontend/dispersions.ui", self)

        self.data = np.array([[],[]])

    def exec(self) -> int:
        self.draw_data()
        return self.exec_()

    def set_data(self, data: np.array):
        self.data = data

    def draw_data(self):
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(self.data.shape[0])

        print(self.data)

        for icol, val in enumerate(self.data):
            item = QTableWidgetItem(str(val))
            self.tableWidget.setItem(0, icol, item)
