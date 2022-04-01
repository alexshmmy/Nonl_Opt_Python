# Nonlinear optimization with Python
#
# Optimal solution
# f* = -6961.813875580139
# x0* = 14.095
# x1* = 0.8429607892154782

import numpy as np
from scipy.optimize import minimize

def objective(x):
    # min f(x)
    return (x[0]-10.0)**3+(x[1]-20.0)**3

def g1(x):
    # g1(x) >= 0
    return (x[0] - 5.0)**2 + (x[1] - 5.0)**2 - 100.0

def g2(x):
    # g2(x) = 0
    return (-1)*(x[1] - 5)**2 - (x[0] - 6)**2 + 82.81

if __name__ == "__main__":
    # initial guesses
    n = 2
    x0 = np.zeros(n)
    x0[0] = 90.0
    x0[1] = 90.0

    # show initial objective
    print('\nInitial Objective: ' + str(objective(x0)))

    # state bounds
    b1 = (13.0, 100.0)
    b2 = (0.0, 100.0)
    bnds = (b1, b2)
    con1 = {'type': 'ineq', 'fun': g1}
    con2 = {'type': 'ineq', 'fun': g2}
    cons = ([con1,con2])
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
    print('g_2* = ' + str(g2(z)))

    # print solution
    print('\nSolution')
    print('x1* = ' + str(z[0]))
    print('x2* = ' + str(z[1]))