# Nonlinear Optimizaiton with Python

A collection of nonlinear optimization problems of the form

``            min f(x)                ``

subjet to   

``           g_i(x) >= 0, i=1,2,...N  ``

``            h_j(x) = 0,  j=1,2,...M `` 

``            -lb <= x_k <= Ub, k=1,2,...n ``

where `f(x), g_i(x), h_j(x)` are inherently nonlinear by using the for open source `scipy.optimize` Python library.

### Dependencies
The following packages are required to run the scripts:

`numpy`

`scipy`

The problems have been tested with `Python 3.7.4, numpy>=1.7.3, scipy>=1.4.1`.
