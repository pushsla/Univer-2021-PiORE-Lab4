from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from frontend.impacts import Impacts
from frontend.features import Features
from frontend.dispersions import Dispersions
from frontend.correlations import Correls

from lib.Data import Dataset


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("frontend/main_window.ui", self)

        self.dataset = Dataset.from_random(2, 2)
        self.translation = 2

        self._connect_data_slots()
        self._connect_event_slots()

    def _connect_data_slots(self):
        pass

    def _connect_event_slots(self):
        self.spinBoxDim.valueChanged.connect(self._new_dataset)
        self.spinBoxSamples.valueChanged.connect(self._new_dataset)

        self.spinBoxTranslate.valueChanged.connect(self._new_translation)

        self.pushButtonTranslate.clicked.connect(self._translate)
        self.pushButtonCorrelations.clicked.connect(self._correls)
        self.pushButtonDispersions.clicked.connect(self._disps)
        self.pushButtonImpacts.clicked.connect(self._impacts)
        self.pushButtonFeatures.clicked.connect(self._features)
        self.pushButtonNorm.clicked.connect(self._norm)
        self.pushButtonOriginal.clicked.connect(self._orig)
        self.pushButtonPresent.clicked.connect(self._pres)

    def _new_dataset(self):
        self.dataset = Dataset.from_random(self.spinBoxDim.value(), self.spinBoxSamples.value())

    def _new_translation(self):
        self.translation = self.spinBoxTranslate.value()

    def _norm(self):
        self.dataset.normalize()

    def _translate(self):
        self.dataset = self.dataset.z_translate(self.spinBoxTranslate.value())

    def _correls(self):
        correls = self.dataset.correlations()
        dlg = Correls(self)
        dlg.set_data(correls)
        dlg.exec()

    def _disps(self):
        disps = self.dataset.derivations()
        dlg = Dispersions(self)
        dlg.set_data(disps)
        dlg.exec()

    def _impacts(self):
        imps = self.dataset.derivation_impacts()
        dlg = Impacts(self)
        dlg.set_data(imps)
        dlg.exec()

    def _features(self):
        dlg = Features(self)
        dlg.set_data(self.dataset.data, self.dataset.result)
        dlg.exec()

    def _orig(self):
        data = self.dataset.original_data
        dlg = Correls(self)
        dlg.setWindowTitle("Original")
        dlg.set_data(data)
        dlg.exec(vlabel='s')

    def _pres(self):
        data = self.dataset.data
        dlg = Correls(self)
        dlg.setWindowTitle("Present")
        dlg.set_data(data)
        dlg.exec(vlabel='s')

