# Nonlinear Optimization with Python

A collection of nonlinear optimization problems of the form

```
           min f(x)             

subjet to   
           g_i(x) >= 0,      i=1,2,...N
           h_j(x) = 0,       j=1,2,...M 
           l_k <= x_k <= U_k, k=1,2,...n
```

where:
* `x` is the vector of decision variables (dimension `n`).
* `f(x)` models the objective function to be minimized (in general nonlinear function). 
* The functions `g_i(x)` model the inequality constraints (in general nonlinear functions).
* The functions `h_j(x)` model the equality constraints (in general nonlinear functions). 
* `l_k, U_k` are the lower  and upper bounds, respectively, of each deciection variables `x_k`.
 
The nonlinear optimizaiton problems are solved efficiently by using the open source `scipy.optimize` Python library.

### Dependencies
The following packages are required to run the scripts:

Packages      | 
------------- |
numpy         |
scipy         |

The problems have been tested with `Python 3.7.4, numpy>=1.7.3, scipy>=1.4.1`.

### Collections of problems

`W. Hock and K. Schittkowski: Test Examples for Nonlinear Programming Codes, 1981` is widely accepted as one of the mandatory test scenarios for Nonlinear Programming codes. The 121 problems along with solutions, have been posted in [[link]](https://www.stfmc.de/fmc/rhs/x/tlf.html). In `collections` we provide some of theese benchmark problems solved by using `scipy.optimize` open source Python library.

### How to run

Open terminal and give the following commands:

```
git clone https://github.com/alexshmmy/Nonl_Opt_Python.git
cd Nonl_Opt_Python/collections
python3 problem001.py
```

### Other references


[1] W. Hock and K. Schittkowski: Test Examples for Nonlinear Programming Codes, 1981.

[2] Revised Hock & Schittkowski models for automatable test scenarios, [[link]](https://www.stfmc.de/fmc/rhs/x/tlf.html).

[3] Scipy documentation, [[Link 1]](https://docs.scipy.org/doc/scipy/tutorial/optimize.html#sequential-least-squares-programming-slsqp-algorithm-method-slsqp).

[4] Scipy documenation, [[Link 2]](https://docs.scipy.org/doc/scipy/reference/optimize.html).

[5] Nonlinear programming with pyOpt [[Link]](https://asset-pdf.scinapse.io/prod/2012884505/2012884505.pdf).
