import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

class QualitativeCAPM:
    def __init__(self, Weq, p, Omega, k, l, s, Score, TE):
        self.Weq = Weq
        self.p = p
        self.Omega = Omega
        self.k = k
        self.l = l
        self.s = s
        self.Score = Score
        self.TE = TE

    def calculate_optimal_weights(self):
        Wunconstrained = [self.TE * self.Score[i] / self.s[i] for i in range(len(self.s))]
        d = [self.l * Wunconstrained[k] for k in range(len(Wunconstrained))]
        mu_imp = [(self.k * self.Omega[i, i] * Wunconstrained[i]) / np.sqrt(Wunconstrained[i] * self.Omega[i, i] * Wunconstrained[i]) + d[i] if Wunconstrained[i] != 0 else 0 for i in range(len(Wunconstrained))]
        
        weights = cp.Variable(len(mu_imp))
        constraints = [cp.sum(weights) == 1, weights >= 0]
        objective = cp.Maximize(mu_imp @ weights - self.k * cp.norm(cp.sqrt(self.Omega) @ weights, 2) - (self.l / 2) * cp.quad_form(weights, self.p))
        problem = cp.Problem(objective, constraints)
        problem.solve()

        return weights.value

# Example Usage
Weq = [25/100, 25/100, 25/100, 25/100, 0]
p = [[1, 0.821, 0.285, -0.06, 0], [0.821, 1, 0.344, 0.017, 0], [0.285, 0.344, 1, 0.589, 0], [-0.06, 0.017, 0.589, 1, 0], [0, 0, 0, 0, 1]]
Omega = np.diag(np.matrix(p).diagonal())
k = 0.2
l = 13.3
s = [14.3/100, 16.4/100, 8.3/100, 7/100, 0.1/100]
Score = [-25/100, 75/100, 0, -50/100, 0]
TE = 3/100

capm = QualitativeCAPM(Weq, p, Omega, k, l, s, Score, TE)
optimal_weights = capm.calculate_optimal_weights()

# Plotting the results
asset_labels = ['Equity USA', 'Equity EMU', 'Bond EUR Sovereign 5Y', 'Bond EUR Sovereign 10Y', 'Cash']
colors = ['blue', 'green', 'red', 'purpl
