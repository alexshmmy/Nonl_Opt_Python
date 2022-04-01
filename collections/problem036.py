# Nonlinear optimization with Python
#
# Optimal solution
# f* = -3300
# x0* = 20.0
# x1* = 11.0
# x2* = 15.0

import numpy as np
from scipy.optimize import minimize

def objective(x):
    # min f(x)
    return -x[0]*x[1]*x[2]

def g1(x):
    # g1(x) >= 0
    return -x[0]-2*x[1]-2*x[2]+72.0

if __name__ == "__main__":
    # initial guesses
    n = 3
    x0 = np.zeros(n)
    x0[0] = 0.1
    x0[1] = 0.1
    x0[2] = 0.1

    # show initial objective
    print('Initial Objective: ' + str(objective(x0)))

    # state bounds
    b1 = (0.0, 20.0)
    b2 = (0.0, 11.0)
    b3 = (0.0, 15.0)
    bnds = (b1, b2, b3)
    con1 = {'type': 'ineq', 'fun': g1}
    cons = ([con1])
    print("\n")
    solution = minimize(objective, x0, method='SLSQP', jac=None, bounds = bnds,
                        constraints = cons, tol = 1e-20, 
                        options={'maxiter': 1000000, 'ftol': 1e-20, 'disp': True})
    
    # z is a numpy.ndarray vector
    z = solution.x

    # show final objective
    print('\nFinal Objective')
    print('f* = ' + str(objective(z)))

    # show constraint values over optimal solution
    print('\nFinal constraints')
    print('g_1* = ' + str(g1(z)))

    # print solution
    print('\nSolution')
    print('x1 = ' + str(z[0]))
    print('x2 = ' + str(z[1]))
    print('x3 = ' + str(z[2]))