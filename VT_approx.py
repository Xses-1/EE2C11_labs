import numpy as np
import json
from pprint import pprint


in_file = open("sample.json")

sample = json.loads(in_file.read())

Id = []
Vgs = []
vds = []

#known variables
for i in range(1, len(sample)-1):
    Id.append([])
    Vgs.append([])
    for j in range(1, len(sample[i])-1):
        Id[i-1].append(float(sample[i][j][1]))
        Vgs[i-1].append(float(sample[i][j][0]))

            
        match sample[i][0]:
            case "600m":
                vds.append(0.6)
            case "630m":
                vds.append(0.63)
            case "660m":
                vds.append(0.66)
            case "690m":
                vds.append(0.69)
            case "720m":
                vds.append(0.72)
            case "750m":
                vds.append(0.75)
            case "780m":
                vds.append(0.78)
            case "810m":
                vds.append(0.81)
            case "840m":
                vds.append(0.84)
            case "870m":
                vds.append(0.87)
            case "900m":
                vds.append(0.90)
            case "930m":
                vds.append(0.93)
            case "960m":
                vds.append(0.96)
            case "990m":
                vds.append(0.99)
            case _ :
                vds.append(float(sample[i][0]))

#formula : Id = 1/2 k (Vgs - Vt) ^ 2

#slope of y = sqrt(Id) x = Vgs in saturation region, calculate intersect on x axis -> Vt

#slope of last two coordinates
#y2-y1/x2-x1

Vt = []
i = 1
while i < len(Id): 
    y1 = np.sqrt(Id[i][20])   # Set the points to the 46th and 47th because there is 91
    y2 = np.sqrt(Id[i][20 + 5])   # points, so this is somwhere in the middle

    x1 = Vgs[i][20]
    x2 = Vgs[i][20+ 5]

    Slope = (y2 - y1) / (x2 - x1)
    # y = slope(x - x1) + y1
    # Vt = x when y = 0
    # Vt = -y1

    Vt.append((-y1/Slope) + x1) # This might cause an overflow, but whatever; fuck it
                                      # Let's see wheather Python can take that;
                                      # This is not my fault that I can't even check for fucking
                                      # overflow because this piece of garbage languge is supposed to
                                      # do fucking memory management for you;
                                      # in C/C++ I know that long long is 64bit or whatever and won't
                                      # overflow, but idk here; fuck this shit

    i += 1

vt = np.average(Vt)
print("vt = " + str(vt))
