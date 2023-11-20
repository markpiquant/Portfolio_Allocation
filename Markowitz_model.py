import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt
from math import sqrt

class Markowitz:
    def __init__(self, mu, p, l):
        self.mu = mu
        self.p = p
        self.l = l

    def classic_markowitz_Maximise_return_for_a_given_risk(self):
        inverse_p = np.linalg.inv(self.p)
        wMV = np.dot(self.mu, inverse_p) / (np.ones(len(np.transpose(self.mu))) @ inverse_p @ np.transpose(self.mu))
        return wMV

    def classic_markowitz_Minimise_risk(self):
        inverse_p = np.linalg.inv(self.p)
        wMV = (np.dot(np.transpose(np.ones(len(np.transpose(self.mu)))), inverse_p)) / (np.ones(len(np.transpose(self.mu))) @ inverse_p @ np.ones(len(np.transpose(self.mu))))
        return wMV

    def robust_markowitz(self, Theta, Ke):
        weights = cp.Variable(len(self.mu))
        constraints = [cp.sum(weights) == 1, weights >= 0]
        objective = cp.Maximize(self.mu @ weights - Ke * cp.norm(cp.sqrt(Theta) @ weights, 2) - (self.l / 2) * cp.quad_form(weights, self.p))
        problem = cp.Problem(objective, constraints)
        problem.solve()
        return weights.value
