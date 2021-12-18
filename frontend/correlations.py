from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5 import uic

import numpy as np


class Correls(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi("frontend/correlations.ui", self)

        self.data = np.array([[], []])

    def exec(self, hlabel='x', vlabel='x') -> int:
        self.draw_data(hlabel=hlabel, vlabel=vlabel)
        return self.exec_()

    def set_data(self, data: np.array):
        self.data = data

    def draw_data(self, hlabel='x', vlabel='x'):
        self.tableWidget.setRowCount(self.data.shape[0])
        self.tableWidget.setColumnCount(self.data.shape[1])

        self.tableWidget.setHorizontalHeaderLabels([f'{hlabel}{i}' for i in range(self.data.shape[1])])
        self.tableWidget.setVerticalHeaderLabels([f'{vlabel}{i}' for i in range(self.data.shape[0])])

        for irow, row in enumerate(self.data):
            for icol, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                self.tableWidget.setItem(irow, icol, item)
