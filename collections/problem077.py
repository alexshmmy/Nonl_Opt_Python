# Nonlinear optimization with Python
#
# Optimal solution
# f* = 0.2415051287901787
# x0* = 1.166172189709298
# x1* = 1.182111388802704
# x2* = 1.38025704314546
# x3* = 1.506036273623046
# x4* = 0.6109201960430908

import math 
import numpy as np
from scipy.optimize import minimize

def objective(x):
    # min f(x)
    return (x[0]-1)**2+(x[0]-x[1])**2+(x[2]-1)**2+(x[3]-1)**4+(x[4]-1)**6

def h1(x):
    # h1(x) = 0
    return x[3]*x[0]**2 + math.sin(x[3] - x[4]) - 2*math.sqrt(2)

def h2(x):
    # h2(x) = 0
    return x[1] + x[2]**4*x[3]**2 - 8 - math.sqrt(2) 

if __name__ == "__main__":
    # initial guesses
    n = 5
    x0 = np.zeros(n)
    x0[0] = 0.0
    x0[1] = 0.0
    x0[2] = 0.0
    x0[3] = 0.0
    x0[4] = 0.0

    # show initial objective
    print('\nInitial Objective: ' + str(objective(x0)))

    # state bounds
    b = (-10.0, 10.0)
    bnds = (b, b, b, b, b)
    con1 = {'type': 'eq', 'fun': h1}
    con2 = {'type': 'eq', 'fun': h2}
    cons = ([con1,con2])
    print("\n")
    solution = minimize(objective, x0, method='SLSQP', jac=None, bounds = bnds,
                        constraints = cons, tol = 1e-20, 
                        options={'maxiter': 100, 'ftol': 1e-20, 'disp': True})
    
    # z is a numpy.ndarray vector
    z = solution.x

    # show final objective
    print('\nFinal Objective')
    print('f* = ' + str(objective(z)))

    # show constraint values over optimal solution
    print('\nFinal constraints')
    print('h_1* = ' + str(h1(z)))
    print('h_2* = ' + str(h2(z)))

    # print solution
    print('\nSolution')
    print('x1* = ' + str(z[0]))
    print('x2* = ' + str(z[1]))
    print('x3* = ' + str(z[2]))
    print('x4* = ' + str(z[3]))
    print('x4* = ' + str(z[4]))