# Nonlinear optimization with Python
# Link: http://apmonitor.com/che263/index.php/Main/PythonOptimization

import numpy as np
from scipy.optimize import minimize

def objective(x):
    # min f(x)
    return -x[0]*x[1]*x[2]

def constraint1(x):
    # g(x) >= 0
    return -x[0]-2*x[1]-2*x[2]+72.0

def constraint2(x):
    # h(x) = 0
    return x[0]+2*x[1]+2*x[2]+0.0

if __name__ == "__main__":
    # initial guesses
    n = 3
    x0 = np.zeros(n)
    x0[0] = 1.0
    x0[1] = 1.0
    x0[2] = 1.0

    # show initial objective
    print('Initial Objective: ' + str(objective(x0)))

    # optimize
    b = (0.0, 42.0)
    bnds = (b, b, b)
    con1 = {'type': 'ineq', 'fun': constraint1}
    con2 = {'type': 'ineq', 'fun': constraint2}
    cons = ([con1,con2])
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
    print('g_1* = ' + str(constraint1(z)))
    print('g_2* = ' + str(constraint2(z)))

    # print solution
    print('\nSolution')
    print('x1 = ' + str(z[0]))
    print('x2 = ' + str(z[1]))
    print('x3 = ' + str(z[2]))