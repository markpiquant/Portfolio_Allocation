# README - Portfolio Optimization Scripts
### Overview

This repository contains Python scripts for portfolio optimization using the Markowitz model and an extension to the Qualitative Capital Asset Pricing Model (CAPM). The code allows users to calculate the optimal weights of assets in a portfolio based on their expected returns, risks, and correlations.
Markowitz Model

The Markowitz class implements the classical Markowitz portfolio optimization model. It includes methods for maximizing portfolio return for a given risk level (classic_markowitz_Maximise_return_for_a_given_risk), minimizing risk (classic_markowitz_Minimise_risk), and a robust version of the Markowitz model (robust_markowitz). The robust version accounts for uncertainties in return estimates, enhancing the portfolio's resilience to estimation errors.

### Usage

To use the Markowitz model, create an instance of the Markowitz class with the expected returns (mu), covariance matrix (p), and a risk aversion parameter (l). Call the appropriate method depending on the optimization goal. The code snippet below demonstrates this process:
```
from Markowitz_model import Markowitz

# Example initialization and usage
mu = [0.0548, 0.0706, 0.0038, 0.0041]  # Expected returns
p = [[1, 0.821, 0.285, 0.06], ...]      # Covariance matrix
l = 0.5                                 # Risk aversion parameter

markowitz = Markowitz(mu, p, l)
W_MVO = markowitz.classic_markowitz_Maximise_return_for_a_given_risk()
W_MV = markowitz.classic_markowitz_Minimise_risk()
robust_weights = markowitz.robust_markowitz(Theta, Ke)
```

 ### Qualitative CAPM

The QualitativeCAPM class is an implementation of a qualitative approach to the Capital Asset Pricing Model. This model considers subjective scores and additional constraints to optimize the portfolio weights, aiming to align with specific investment strategies or constraints.
Usage

Initialize the QualitativeCAPM class with market equilibrium weights (Weq), covariance matrix (p), diagonal matrix Omega (Omega), a constant for risk aversion (k), leverage (l), scores (Score), and tracking error (TE). The calculate_optimal_weights method computes the optimal asset weights.

```
from QualitativeCAPM_model import QualitativeCAPM

Weq = [0.25, 0.25, 0.25, 0.25, 0]
p = [[1, 0.821, 0.285, -0.06, 0], ...]
Omega = np.diag(np.matrix(p).diagonal())
k = 0.2
l = 13.3
s = [0.143, 0.164, 0.083, 0.07, 0.001]
Score = [-0.25, 0.75, 0, -0.5, 0]
TE = 0.03

capm = QualitativeCAPM(Weq, p, Omega, k, l, s, Score, TE)
optimal_weights = capm.calculate_optimal_weights()
```

### Future Additions

Future updates will include additional methods for portfolio optimization to cater to a broader range of investment strategies and risk preferences.

### Requirements

    - Python 3.x
    - NumPy
    - CVXPY
    - Matplotlib

