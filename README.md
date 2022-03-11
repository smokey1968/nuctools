Nuctools is a python package which was initially intended to assist with reduction
of data taken at the RPI linear accelerator, and was significantly influenced by 
technical expertise and advice from Yaron Danon and other RPI research staff. It 
includes functions to dead-time correct [1], group counts data, convert to cps, 
and convert neutron time-of-flight (TOF) to neutron energy.

The module `trans_tools.py` was originally designed to reduce data generated by the 
Comtec MCS6A Multi-stop TDC TOF clock, but will be generalized to accept other 
formats of raw TOF data. `trans_tools.py` is designed to reduce all the data 
necessary to calculate transmission and propagate the associated covariance.

Module `sam_tools.py` has been made to assist in reading and writing files that 
are used in the i/o for the code SAMMY. The package `nuctools` also contains 
functions to assist in plotting with different styles commonly used at RPI.

--- To Install --------------

File structure being:

+ nuctools
   - docs/
   - nuctools/
   - tests/
   - README.md
   - LICENSE.md
   - setup.py

Open a terminal in the top nuctools folder, and execute (I highly recommend an Anaconda installation):

```bash
python -m pip install .
```

--- To Document -------------

Make sure you have numpydoc and sphinx installed, with anaconda installer:

```bash
conda install numpydoc
conda install sphinx
```

At the sphinx website http://www.sphinx-doc.org/en/master/usage/quickstart.html,
there is a brief walkthrough for first time sphinx users. This is a good place 
find info on sphinx, however you shouldn't have to create the documentation, it
should be good to go when the nuctools is downloaded. The sphinx-quickstart will
write a "conf.py" for you, but you should have the properly designed conf.py 
already. To use the theme I've used for the docs, you need to run 
`pip install sphinx-rtd-theme`.

In the terminal navigate to the top nuctools folder and type:

```bash
sphinx-apidoc --force -o docs/ nuctools/
```

where "docs/" is the output directory and "nuctools/" is where the documented
modules live. Then navigate inside the terminal to the "docs/" folder where you
just generated .rst files and type:

```bash
make html
```

--- To Test -----------------

Make sure you have pytest, with anaconda:

```bash
conda install pytest
```

or with `pip`:

```bash
pip install pytest
```

Then inside the top nuctools folder type:

```bash
pytest
```

Pytest should go into the "tests/" folder and find python files that start
with "test".


1. Danon, Yaron. "Design and Construction of the RPI Enhanced Thermal Neutron Target and Thermal Cross Section Measurements of Rare Earth Isotopes.", Doctoral Thesis, (1993).
