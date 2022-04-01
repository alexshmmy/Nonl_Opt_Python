# Nonlinear optimization with Python
# Problem 3 in paper https://asset-pdf.scinapse.io/prod/2012884505/2012884505.pdf
#
# Optimal solution
# f* = -5.1621
# x0* = 2.003
# x1* = 1.006 

import numpy as np
import math
from scipy.optimize import minimize

def objective(x):
    # min f(x)
    a = [3, 5, 2, 1, 7]
    b = [5, 2, 1, 4, 9]
    c = [1, 2, 5, 2, 3]
    f = 0.0

    for i in range(5):
        f += -(c[i] * math.exp(-(1/math.pi)*((x[0]-a[i])**2 + (x[1]-b[i])**2)) * math.cos(math.pi*((x[0]-a[i])**2 + (x[1]-b[i])**2)))
    
    return f

def g1(x):
    # g(x) >= 0
    return (x[0]+2.0)**2+(x[1]+1.0)**2-20.04895

if __name__ == "__main__":
    # initial guesses
    n = 2
    x0 = np.zeros(n)
    x0[0] = 2.0
    x0[1] = 1.0

    # show initial objective
    print('\nInitial Objective: ' + str(objective(x0)))

    # state bounds
    b = (-2.0, 10.0)
    bnds = (b, b)
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
    print('x1* = ' + str(z[0]))
    print('x2* = ' + str(z[1]))