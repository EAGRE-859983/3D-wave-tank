# Firedrake code for the 3D numerical wave tank
This repository contains Firedrake codes for the four test cases (TCs) in the paper *Variational and numerical modelling strategies for cost-effective simulations of driven free-surface waves*, which is to be submitted to *Journal of Computational Physics*.

## How to use the code?
- First, you need to install [Firedrake](https://www.firedrakeproject.org/download.html), which is a finite-element simulation environment.
- One test case consists of 5 code files, including 4 shared files among all the TCs (i.e., the **main file `3D_tank.py`**, `vertical_discr_full.py`, `solvers_full.py`, `savings.py`) and one exclusive file for setting parameters for that TC (i.e., `settings_TCx.py`).
- To switch between different TCs, specify the case you are going to run by changing the string for the parameter `case` at the beginning of the main file `3D_tank.py`. For example, if you want to run Test Case 1, set it as: `case = 'TC1'`.
- In the `settings_TCx.py` file, you can set the name of the folder storing numerical results by modifing `save_path` in the function `test_case`. You can also change the spatial or temporal resolution of the case by modifing `res_x`, `res_y` in the function `domain`, or `dt` in the function `set_time`.
- In addtion, you can also create your own test case by modifing `settings_User.py` and set `case = 'TCU'` in the beginning of `3D_tank.py`.
- The code can be run in serial, but also in parallel using P processes by doing:
```
$ mpiexec -n P python3 3D_tank.py
```

## How to reproduce the results?
