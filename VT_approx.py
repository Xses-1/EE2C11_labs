import numpy as np
import json
import matplotlib.pyplot as plt
from pprint import pprint

def FormatSample(sample):
    #known variables
    for i in range(0, len(sample)):
        Id.append([])
        Vgs.append([])
        match sample[i][0]:
                case "600m":
                    Vds.append(0.6)
                case "630m":
                    Vds.append(0.63)
                case "660m":
                    Vds.append(0.66)
                case "690m":
                    Vds.append(0.69)
                case "720m":
                    Vds.append(0.72)
                case "750m":
                    Vds.append(0.75)
                case "780m":
                    Vds.append(0.78)
                case "810m":
                    Vds.append(0.81)
                case "840m":
                    Vds.append(0.84)
                case "870m":
                    Vds.append(0.87)
                case "900m":
                    Vds.append(0.90)
                case "930m":
                    Vds.append(0.93)
                case "960m":
                    Vds.append(0.96)
                case "990m":
                    Vds.append(0.99)
                case _ :
                    Vds.append(float(sample[i][0]))
        for j in range(1, len(sample[i])-1):
            Id[i-1].append(float(sample[i][j][1]))
            Vgs[i-1].append(round(float(sample[i][j][0]),4))

            
    print(len(Id[1]))
    print("\n")
    print(len(Vds))
    print("\n")
    print(len(Vgs[1]))
    print("\n")



def linear_region(x,y):
    derivatives = []
    for i in range(1, len(x)):
        x1 = x[i-1]
        x2 = x[i]
        y1 = y[i-1]
        y2 = y[i]
        print(y1,y2,x1,x2)
        slope = (y2 - y1) / (x2 - x1)
        
        derivatives.append(slope)
    print('\n\n')

   

    maxder = derivatives.index(max(derivatives))
    return maxder


def findVal():
    Vt = []
    K = []
    K2 = []
    lamarray = []
    for i in range(1, len(Vds)) :

        ################################
        #Find the Treshold Voltage
        ################################

        #Val VGs i val Vgs 25 because that is assumed to be in the saturation region 

        #formula : Id = 1/2 k (Vgs - Vt) ^ 2

        #slope of y = sqrt(Id) x = Vgs in saturation region, calculate intersect on x axis -> Vt
        
        #slope of last two coordinates
        #y2-y1/x2-x1

        y1 = np.sqrt(Id[i][25])   
        y2 = np.sqrt(Id[i][25 + 5])  

        x1 = Vgs[i][25]
        x2 = Vgs[i][25 + 5]

        Slope = (y2 - y1) / (x2 - x1)
        # y = slope(x - x1) + y1
        # Vt = x when y = 0
        # Vt = -y1/slope + x1

        vt = -y1/slope + x1
        Vt.append(vt) 

        #---------------------------------------------------------------- Vt Found

        

        K.append((2*(Slope**2))/((x1-Vt[i-1])**2))

        #Finding Lamda line
        x1 = Vds[i-1][50]
        x2 = Vds[i][50]

        y1 = Id[i-1][50]
        y2 = Id[i][50]

        slope = (y2 - y1) / (x2 - x1)

        # lamda = -1/vds when id = 0

        vdslam = (-y1/slope) + x1

        lamarray.append(-1/vdslam)

        #K2: Id = idprime when vds = 0 

        idprime = (-slope * x1) + y1

        K2.append((2*idprime)/((Vgs[i]-Vt[i-1])**2))

    pprint(K2)
    vt = np.average(Vt)
    k = np.average(K)
    k2 = np.average(K2)
    lamda = np.average(lamarray)

    print("vt = " + str(vt))
    print("k = " + str(k))
    print("k2 = " + str(k2))
    print("lamda = " + str(lamda))

def plotSample(id, vgs, vds):

    # place the legend, given the labels above for each of the lines.
    for i in range(0, len(vds)):
        #plot Id vs 
        label = f'$V_{{GS}}$ = {vds[i]}V'
        plt.plot(vgs[i-1], id[i-1], label = label)

        
    plt.legend(loc="upper left")

    # Place labels at x- and y-axis, and title above the plot.
    # Matplotlib can use LaTeX notation for formulas.
    # Braces can be doubled {{}} to escape f-string interpolation
    plt.title(f'Derivative of $I_D$ over $V_{{DS}}$ for different Vgs')
    

    # show it on the screen
    plt.grid(color='gray', linestyle=':', linewidth=0.5)
    plt.show()


if __name__ == "__main__":

    in_file = open("EE2C11_labs\I(Vds).json")
    sample = json.loads(in_file.read())

    Id = []
    Vgs = []
    Vds = []

    FormatSample(sample)

    findVal()

