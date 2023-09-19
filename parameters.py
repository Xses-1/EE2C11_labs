#
# Parameter personalization script for EE2C11, 2022, NvdM
#

import random

# Invoke this function with one of the netids of the team as an
# argument. It computes three modified parameters.
# These have to be inserted in the spice model .mod file.
# Example function call: [u0, tox, lint] = parameters ("mynetid")
# Or run it as a commandline script.

# see https://docs.python.org/3/library/random.html

def parameters (netid):
    # initialize random number generator from netid
    random.seed (netid)

    # Assume a stddeviation of 5%.
    # Then, 99.7% of all parameters will be within +/- 15%
    sigma = 0.05

    # generate parameters
    # default PTM180 values are 3.5E-2, 4.0e-9 and 4.0e-8 respectively
    u0 = 3.5e-2 * random.gauss (1, sigma)
    tox = 4.0e-9 * random.gauss (1, sigma)
    lint = 4.0e-8 * random.gauss (1, sigma)

    return ([u0, tox, lint])



# For running as a commandline script
# It will ask to enter your netid
# The if __name__ construct will evaluate true when the module is not initialized from
# an import statement and the corresponding code is executed.
# See https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    netid = input ("Enter netid: ")
    [u0, tox, lint] = parameters (netid)
    print (f'netid: {netid}')
    print ("use the following values for the corresponding parameters\nin the ptm180.mod file:")
    print (f'u0  : {u0*1e2:.2f}E-2 (mobility, in cm^2/Vs)')
    print (f'Tox : {tox*1e9:.2f}E-9 (gate oxide thickness, in m)')
    print (f'Lint: {lint*1e8:.2f}E-8 (under-diffusion length, in m)')

