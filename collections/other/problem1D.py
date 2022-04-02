# Nonlinear optimization with Python
#
# Optimal solution
# f* = -6961.813875580139
# x0* = 14.095
# x1* = 0.8429607892154782

import math
import numpy as np
from scipy.optimize import minimize

def objective(x):
    # min f(x)
    return x[0]**2+10*math.sin(x[0])

if __name__ == "__main__":
    # initial guesses
    n = 1
    x0 = np.zeros(n)
    x0[0] = 90.0

    # show initial objective
    print('\nInitial Objective: ' + str(objective(x0)))

    # state bounds
    b1 = (-100.0, 100.0)
    bds = (b1,)
    print("\n")
    solution = minimize(objective, x0, method='SLSQP', jac=None, bounds=bds,
                        tol = 1e-20, constraints=(),
                        options={'maxiter': 1000000, 'ftol': 1e-20, 'disp': True})
    
    # z is a numpy.ndarray vector
    z = solution.x

    # show final objective
    print('\nFinal Objective')
    print('f* = ' + str(objective(z)))

    # print solution
    print('\nSolution')
    print('x1* = ' + str(z[0]))