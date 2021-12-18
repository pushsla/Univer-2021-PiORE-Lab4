from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

import numpy as np


class Impacts(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi("frontend/impacts.ui", self)

        self.data = np.array([[],[]])
        self.__data_fig: plt.figure = None
        self.__data_canvas: FigureCanvas = None

    def exec(self) -> int:
        self.__connect_matplotlib()
        self.draw_data()
        return self.exec_()

    def set_data(self, data: np.array):
        self.data = data

    def draw_data(self):
        labels = list(range(self.data.shape[0]))
        values = self.data

        self.__data_fig.clear()
        ax = self.__data_fig.add_subplot()
        ax.bar(labels, values)
        self.__data_canvas.draw()

    def __connect_matplotlib(self):
        self.__data_fig = plt.figure()
        self.__data_canvas = FigureCanvas(self.__data_fig)
        self.verticalLayout.addWidget(self.__data_canvas)