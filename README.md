# :ocean: Firedrake code for the 3D numerical wave tank
This repository contains Firedrake codes for the four test cases (TCs) in the paper [*Variational and numerical modelling strategies for cost-effective simulations of driven free-surface waves*](https://doi.org/10.31223/X5WS8F), which has been submitted to *Journal of Computational Physics*. The preprint can also be found here.

## :ledger: How to use the code?
- First, you need to install [Firedrake](https://www.firedrakeproject.org/download.html), which is a finite-element simulation environment.
- One test case consists of 5 code files, including 4 shared files among all the TCs (the **main file `3D_tank.py`**, `vertical_discr_full.py`, `solvers_full.py`, `savings.py`) and one exclusive file used to set parameters for that TC (`settings_TCx.py`).
- To switch between different TCs, specify the case you are going to run by changing the string for the parameter `case` at the beginning of the main code `3D_tank.py`. For example, if you want to run Test Case 1, set it as: `case = 'TC1'`.
- In the `settings_TCx.py` file: 
  - You can set the *path* for storing numerical results by modifing `save_path` in the function `test_case`. 
  - If you want to run a simulation with *mild-slope approximation* (MSA), set `FWF = 0`. Alternatively, you can implement the full energy expression and full weak formulations (FWF) by setting `FWF = 1`.
  - The boolean variable `save_pvd` following `FWF` determines whether or not to output the solutions into `.pvd` files, which can be visualised using [Paraview](https://www.paraview.org/). If `save_pvd = True`, then the numerical results for the velocity potential of the whole fluid domain before coordinate transformation and the values of tilde R defined by Eq.(5) distributed over the transformed domain will be saved into `waves.pvd` and `Wavemaker.pvd`, respectively.
  - You can also change the *spatial or temporal resolution* of a test case by modifing `res_x`, `res_y` in the function `domain`, or `dt` in the function `set_time`.
- In addition, you can also create your own test case by modifing `settings_User.py` and set `case = 'TCU'` in the beginning of `3D_tank.py`.
- You may also want to output some particular results you need over time, on which you can perform your own data processing. You can do this by adding a piece of code below `# if case=='TCU':` and uncomment that line in the main code `3D_tank.py`.
- The code can be run in serial, but also in parallel using P processes without making any changes to the code itself through a MPI call:
  ```
  $ mpiexec -n P python3 3D_tank.py
  ```

## :triangular_ruler: How to reproduce the results?
The post-processing codes for the 4 test cases can be find in the folder [pp-codes](pp-codes), and the figures they produce as we used in the paper are shown in the folder [figures](figures). The instructions for reproducing each test case are summarized in the table below.

| Test Case | Figures in the paper (Code name)| Instructions |
| :---: |  :--- | :--- |
| TC1 | :black_small_square: Fig.4 (`pp_SWS_TC1.py`) | :white_small_square: To plot the energy variations and compare with exact standing wave solutions.|
| TC2 and TC2b | :black_small_square: Fig.5 for TC2, Fig.7 for TC2b (`pp_norms_TC2.py`) <br> :white_small_square: Fig.6 (`pp_h_end_TC2.py`)| :black_small_square: To calculate the order of convergence in space[^1] and plot the temporal evolutions of the spatial-convergence indices. <br> :white_small_square: To compare between TC2 and TC2b. |
| TC3 and TC3b | :black_small_square: Figs.8 \& 9 for TC3, Figs.11 \& 12 for TC3b (`pp_energy_figs_TC3.py`) <br> :white_small_square: Fig.10 (`pp_h_end_TC3.py`) |:black_small_square: To plot the energy evolutions for the two time resolutions. <br> :white_small_square: To compare between TC3 and TC3b.|
| TC4 | :black_small_square: Fig.14 (`pp_wavemaker_TC4.py`) <br> :white_small_square: Fig.17 (`pp_probes_TC4.py`) <br> :black_small_square: Fig.18 (`FFT_202002.m`[^2]) | :black_small_square: To plot the wavemaker motion and velocity. <br> :white_small_square: To compare between the numerical results and experimental data. <br> :black_small_square: To perform fast Fourier transforms (FFT) on the experimental and numerical data.|

[^1]: The results obtained from our machine are listed here for your reference. **TC2:** (1) SE: 1.9953082338032144 (L<sup>2</sup>), 1.658660903611349 (L<sup>∞</sup>); (2) SV: 1.996407364146907 (L<sup>2</sup>), 1.6579860378876148 (L<sup>∞</sup>).  **TC2b:** (1) SE: 2.005886784189062 (L<sup>2</sup>), 1.6583078228866475 (L<sup>∞</sup>); (2) SV: 2.0068434319649624 (L<sup>2</sup>), 1.6564678030892535 (L<sup>∞</sup>).
[^2]: We gratefully acknowledge the support from Dr. Elena Gagarina: she shared with us the original MATLAB code for FFT, as well as the numerical results obtained from her model for the same test case (see http://dx.doi.org/10.1016/j.jcp.2014.06.035).

## :speech_balloon: Get in touch with us!
If you have any questions, comments or suggestions on the code or coding style (e.g., you may have a more elegant way to output results during the time loops and post-process the data), do not hesitate to drop us an e-mail (*mmyl@leeds.ac.uk*). Your feedback is highly appreciated and will help us further improve the code ;)
