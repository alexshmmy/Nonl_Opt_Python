# Nonlinear optimization with Python
#
# Optimal solution
# f*  = 1.0
# x0* = 1.0
# x1* = 0.0

import numpy as np
from scipy.optimize import minimize

def objective(x):
    # min f(x)
    return x[0]**2+x[1]**2+x[2]**2

def g1(x):
    # g1(x) >= 0
    return x[0]**2+x[1]**2-1.0

if __name__ == "__main__":
    # initial guesses
    n = 3
    x0 = np.zeros(n)
    x0[0] = 10.0
    x0[1] = 9.5
    x0[2] = -9.5

    # show initial objective
    print('Initial Objective: ' + str(objective(x0)))

    # state bounds
    b1 = (1.0, 10.0)
    b2 = (-10.0, 10.0)
    bnds = (b1, b2, b2)
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
    print('x2 = ' + str(z[2]))