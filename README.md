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

### Collections of problems

`W. Hock and K. Schittkowski: Test Examples for Nonlinear Programming Codes, 1981` is widely accepted as one of the mandatory test scenarios for Nonlinear Programming codes. The 121 problems along with solutions, have been posted in [[link]](https://www.stfmc.de/fmc/rhs/x/tlf.html)

### Other references

[1] http://apmonitor.com/che263/index.php/Main/PythonOptimization


[2] adsf https://docs.scipy.org/doc/scipy/tutorial/optimize.html#sequential-least-squares-programming-slsqp-algorithm-method-slsqp

[3] adsf https://docs.scipy.org/doc/scipy/reference/optimize.html

[4] adsf https://asset-pdf.scinapse.io/prod/2012884505/2012884505.pdf 
