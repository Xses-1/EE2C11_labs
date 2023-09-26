import numpy as np
import json
from pprint import pprint


in_file = open("sample.json")

sample = json.loads(in_file.read())

Id = []
Vgs = []
Vds = []

#known variables
for i in range(1, len(sample)-1):
    Id.append([])
    Vgs.append([])
    Vds.append([])
    for j in range(1, len(sample[i])-1):
        Id[i-1].append(float(sample[i][j][1]))
        Vgs[i-1].append(float(sample[i][j][0]))

            
        match sample[i][0]:
            case "600m":
                Vds[i-1].append(0.6)
            case "630m":
                Vds[i-1].append(0.63)
            case "660m":
                Vds[i-1].append(0.66)
            case "690m":
                Vds[i-1].append(0.69)
            case "720m":
                Vds[i-1].append(0.72)
            case "750m":
                Vds[i-1].append(0.75)
            case "780m":
                Vds[i-1].append(0.78)
            case "810m":
                Vds[i-1].append(0.81)
            case "840m":
                Vds[i-1].append(0.84)
            case "870m":
                Vds[i-1].append(0.87)
            case "900m":
                Vds[i-1].append(0.90)
            case "930m":
                Vds[i-1].append(0.93)
            case "960m":
                Vds[i-1].append(0.96)
            case "990m":
                Vds[i-1].append(0.99)
            case _ :
                Vds[i-1].append(float(sample[i][0]))

#formula : Id = 1/2 k (Vgs - Vt) ^ 2

#slope of y = sqrt(Id) x = Vgs in saturation region, calculate intersect on x axis -> Vt

#slope of last two coordinates
#y2-y1/x2-x1

def linear_region(x,y):
    derivatives = []
    maxslope = 0
    maxindex = None
    for i in range(10, len(x)):
        x1 = x[i-1]
        x2 = x[i]
        y1 = y[i-1]
        y2 = y[i]
        slope = (y2 - y1) / (x2 - x1)
        if slope > maxslope :
            maxslope = slope
            maxindex = i
        derivatives.append(slope)

    return maxindex


Vt = []
K = []
K2 = []
lamarray = []
i = 1
while i < len(Id): 
    index = linear_region(Id[i], Vgs[i])
    print (index)
    y1 = np.sqrt(Id[i][index])   # Set the points to the 46th and 47th because there is 91
    y2 = np.sqrt(Id[i][index + 5])   # points, so this is somwhere in the middle

    x1 = Vgs[i][index - 5]
    x2 = Vgs[i][index]

    Slope = (y2 - y1) / (x2 - x1)
    # y = slope(x - x1) + y1
    # Vt = x when y = 0
    # Vt = -y1

    Vt.append((-y1/Slope) + x1) 

    K.append((2*(Slope**2))/((x1-Vt[i-1])**2))

    #Finding Lamda line
    x1 = Vds[index - 1][50]
    x2 = Vds[index][50]

    y1 = Id[index - 1][50]
    y2 = Id[index][50]

    slope = (y2 - y1) / (x2 - x1)

    # lamda = -1/vds when id = 0

    vdslam = (-y1/slope) + x1

    lamarray.append(-1/vdslam)

    #K2: Id = idprime when vds = 0 

    idprime = (-slope * x1) + y1

    K2.append((2*idprime)/((Vgs[i]-Vt[i-1])**2))
     

    i += 1

vt = np.average(Vt)
k = np.average(K)
k2 = np.average(K2)
lamda = np.average(lamarray)

print("vt = " + str(vt))
print("k = " + str(k))
print("k2 = " + str(k2))
print("lamda = " + str(lamda))
