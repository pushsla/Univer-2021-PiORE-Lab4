from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

import numpy as np


class Features(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi("frontend/features.ui", self)

        self.data = np.array([[], []])
        self.reals = np.array([])
        self.feature = 0
        self.__data_fig: plt.figure = None
        self.__data_canvas: FigureCanvas = None

    def __connect_data_slots(self):
        for v in range(self.data.shape[1]):
            self.comboBox.addItem(str(v), v)

    def __connect_event_slots(self):
        self.comboBox.currentIndexChanged.connect(self._new_feature)

    def exec(self) -> int:
        self.__connect_data_slots()
        self.__connect_event_slots()
        self.__connect_matplotlib()
        self.draw_data()
        return self.exec_()

    def set_data(self, data: np.array, reals: np.array):
        self.data = data
        self.reals = reals

    def _new_feature(self):
        self.feature = self.comboBox.currentData()
        self.draw_data()

    def draw_data(self):

        self.__data_fig.clear()
        ax = self.__data_fig.add_subplot()
        print(self.feature)
        ax.scatter(self.data[:, self.feature], self.reals)
        self.__data_canvas.draw()

    def __connect_matplotlib(self):
        self.__data_fig = plt.figure()
        self.__data_canvas = FigureCanvas(self.__data_fig)
        self.verticalLayout.addWidget(self.__data_canvas)