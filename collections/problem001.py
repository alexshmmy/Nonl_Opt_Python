# Nonlinear optimization with Python
# Link1: http://apmonitor.com/che263/index.php/Main/PythonOptimization
# Link2: https://docs.scipy.org/doc/scipy/tutorial/optimize.html#sequential-least-squares-programming-slsqp-algorithm-method-slsqp
# Link3: https://docs.scipy.org/doc/scipy/reference/optimize.html
# Link4: https://asset-pdf.scinapse.io/prod/2012884505/2012884505.pdf 
# Link5: https://www.stfmc.de/fmc/rhs/x/tlf.html

import numpy as np
from scipy.optimize import minimize

def objective(x):
    # min f(x)
    return x[0]*x[3]*(x[0]+x[1]+x[2])+x[2]

def constraint1(x):
    # g(x) >= 0
    return x[0]*x[1]*x[2]*x[3]-25.0

def constraint2(x):
    # h(x) = 0
    sum_eq = 40.0
    for i in range(4):
        sum_eq = sum_eq - x[i]**2
    return sum_eq

if __name__ == "__main__":
    # initial guesses
    n = 4
    x0 = np.zeros(n)
    x0[0] = 1.0
    x0[1] = 5.0
    x0[2] = 5.0
    x0[3] = 1.0

    # show initial objective
    print('Initial Objective: ' + str(objective(x0)))

    # optimize
    b = (1.0,5.0)
    bnds = (b, b, b, b)
    con1 = {'type': 'ineq', 'fun': constraint1}
    con2 = {'type': 'eq', 'fun': constraint2}
    cons = ([con1,con2])
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
    print('g_1* = ' + str(constraint1(z)))
    print('g_2* = ' + str(constraint2(z)))

    # print solution
    print('\nSolution')
    print('x1 = ' + str(z[0]))
    print('x2 = ' + str(z[1]))
    print('x3 = ' + str(z[2]))
    print('x4 = ' + str(z[3]))
