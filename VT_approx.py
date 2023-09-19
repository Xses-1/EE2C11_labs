import numpy as np

input_file = []

#known variables
Id =[]
Vds = []
Vgs = []

#formula : Id = 1/2 k (Vgs - Vt) ^ 2

#slope of y = sqrt(Id) x = Vgs in saturation region, calculate intersect on x axis -> Vt

#slope of last two coordinates
#y2-y1/x2-x1

y1 = np.sqrt(Id[-1])
y2 = np.sqrt(Id[-2])

x1 = Vgs[-1]
x2 = Vgs[-2]

Slope = (y2 - y1) / (x2 - x1)
# y = slope(x - x1) + y1
# Vt = x when y = 0

y = 0

Vt = ( (y - y1)/Slope ) + x1


