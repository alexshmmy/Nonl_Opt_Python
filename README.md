# Nlopt_Python

A collection of nonlinear optimization problems of the form
``
            min f(x)

subjet to   g_i(x) >= 0, i=1,2,...N
            h_j(x) = 0,  j=1,2,...M
            -lb <= x_k <= Ub, k=1,2,...n
``
by using the for open source `scipy.optimize` Python library.
