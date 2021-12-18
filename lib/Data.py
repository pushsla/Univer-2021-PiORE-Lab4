import numpy as np
import random as rnd


class Dataset:
    @staticmethod
    def from_random(n_factors: int, n_samples: int) -> 'Dataset':
        real_coefs = (np.random.random((n_factors, 1))-0.5)*25
        pows = np.ones((1, n_factors)) #np.array(range(n_factors))
        data = (np.random.random((n_samples, n_factors))-0.5)*5 + rnd.randint(0, 10)

        for i in range(0, n_factors, 3):
            data[:, i] *= 10

        for i in range(0, n_factors, 4):
            data[:, i] /= 20

        for i in range(0, n_factors, 8):
            data[:, i] *= 35

        for i in range(1, n_factors, 5):
            data[:, i] = 5*data[:, i-1] + rnd.randint(-1, 10)

        result = data**pows
        result = np.dot(result, real_coefs)

        return Dataset(data, result)

    def __init__(self, data: np.array, result: np.array):
        self.data = data
        self.original_data = np.copy(data)
        self.result = result
        self.n_factors = data.shape[1]
        self.n_samples = data.shape[0]

    def normalize(self):
        maximals = np.max(self.data, axis=0)
        self.data /= maximals

    def component_with_result(self, i_component: int):
        return np.append(self.data[:, i_component], self.result, axis=1)

    def correlations(self) -> np.array:
        return np.corrcoef(self.data, rowvar = False)

    def derivations(self) -> np.array:
        means = np.sum(self.data, axis=0)/self.n_samples
        errors = (self.data - means)**2
        sums = np.sum(errors, axis=0)
        sums /= self.n_samples
        derivations = np.sqrt(sums)

        return derivations

    def derivation_impacts(self) -> np.array:
        derivations = self.derivations()
        deriv_sum = np.sum(derivations)
        impatcs = derivations /deriv_sum

        return impatcs

    def z_translate(self, n_factors: int) -> 'Dataset':
        self.normalize()
        impacts = {k:v for k,v in enumerate(self.derivation_impacts())}
        impacts = {k:v for k, v in sorted(impacts.items(), key=lambda x: x[1])}

        new_data = np.array([[0] for _ in range(self.data.shape[0])])

        for i, _ in impacts.items():
            new_data = np.append(new_data, self.data[:, i].reshape(self.data.shape[0],1), axis=1)

        self.data = new_data[:, 1:]

        xTx = np.dot(self.data.T, self.data)
        own_v, own_w = np.linalg.eig(xTx)

        return Dataset(np.dot(self.data, own_w[:, :n_factors]), self.result)



