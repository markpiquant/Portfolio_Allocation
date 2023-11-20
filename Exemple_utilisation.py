import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt
from math import sqrt
from Markowitz_model import Markowitz
# Exemple d'utilisation
mu = [5.48/100, 7.06/100, 0.38/100, 0.41/100]
p = [[1, 0.821, 0.285, 0.06], [0.821, 1, 0.344, 0.017], [0.285, 0.344, 1, 0.589], [0.06, 0.017, 0.589, 1]]
l = 0.5
Theta = p
Ke = 0.25

markowitz = Markowitz(mu, p, l)

W_MVO = markowitz.classic_markowitz_Maximise_return_for_a_given_risk()
print('Portefeuille qui maximise le retour pour un risque donné:', W_MVO)

W_MV = markowitz.classic_markowitz_Minimise_risk()
print('Portefeuille qui minimise le risque:', W_MV)

robust_weights = markowitz.robust_markowitz(Theta, Ke)
print("Portefeuille robuste:", robust_weights)

# Préparation des données pour le graphique
portfolios = ['W_MVO', 'W_MV', 'Robust']
weights = np.column_stack((W_MVO, W_MV, robust_weights))

# Création du graphique en barres empilées
fig, ax = plt.subplots()
for i in range(len(mu)):
    ax.bar(portfolios, weights[i], bottom=np.sum(weights[:i], axis=0))

ax.set_xlabel('Portefeuille')
ax.set_ylabel('Poids (%)')
ax.set_title('Répartition des poids dans différents portefeuilles')
ax.legend(['Actif 1', 'Actif 2', 'Actif 3', 'Actif 4'], loc='upper left')
plt.grid()
plt.show()
