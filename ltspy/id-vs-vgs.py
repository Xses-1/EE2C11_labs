import matplotlib.pyplot as plt
import ltspy


# Demo of ltspy module
# make a plot of I_D versus V_DS for different values of V_GS
# as simulated by ltspice
# 
# This demo uses f-string formatting. 
# So-called f-strings are '' or "" strings preceded by f: f'this is an f-string'.
# F-strings can embed variables that are placed between {}, and its value will be printed.
# Example:
#   >> a=42
#   >> print (f'The value of a is {a}')
#   >> The value of a is 42
#
# This demo also shows how matplotlib can use LaTeX notation for formulas
# Example:
#   >> vg = 2.5
#   >> plt.xlabel(f'$V_G$ = {vg} V')
# 
# LaTeX formulas use braces {} in many places.
# In f-strings, such braces can be replaced by double braces {{}}
# Example:
#   >> vgs = 2.5
#   >> plt.xlabel(f'$V_{{GS}}$ = {vgs} V')
#
# Below, simdata is an object (a python class).
# A class contains other data and functions
# that can be accessed using the . dot notation.
#
# simdata.values is a two-dimensional array:
#     the first index iterates over output variables
#     the second index over values of that variable.
# simdata.stepvalues similarly has two dimensions.
# simdata.nosteps has the number of steps
#
# simdata.summary() returns a string that summarizes
# what can be found in the input file.


def makeplot(filename):
    simdata = ltspy.SimData(filename)

    print (simdata.summary ())

    # One can use the printed summary from above for figuring
    # out the index values of the variables to be plotted. 
    # could also use the simdata.v method to index by name

    vds_index = 1 # the index of the vds values in simdata.values
    id_index = 3  # the index of the id values in simdata.values

    # The current is multiplied by 1000 to show it in mA.
    for s in range(simdata.nosteps):
        label = f'$V_{{GS}}$ = {simdata.stepvalues[0][s]}V'
        lines = plt.plot(simdata.values[vds_index][s],
            simdata.values[id_index][s] * 1000, label = label) 

    # place the legend, given the labels above for each of the lines.
    plt.legend(loc="upper left")

    # Place labels at x- and y-axis, and title above the plot.
    # Matplotlib can use LaTeX notation for formulas.
    # Braces can be doubled {{}} to escape f-string interpolation
    plt.xlabel(f'$V_{{DS}}~(V)$')
    plt.ylabel(f'$I_{{D}}~(mA)$')
    plt.title(f'$I_D$ as a function of $V_{{DS}}$ for different values of $V_{{GS}}$')


    # The following three statements help matplotlib to place the (0, 0) coordinate
    # in the origin of the plot. Feel free to see how it looks without them.
    # See https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html
    axes = plt.gca()
    axes.set_ylim([0, None])
    axes.set_xlim([0, None])

    # save the figure in a file, pdf works nice.
    plt.savefig(filename + ".pdf")

    # show it on the screen
    plt.show()


if __name__ == '__main__':
    makeplot("nmosid.raw")
