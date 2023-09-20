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

Vt = 0
i = 0
while i < 41: 
    y1 = np.sqrt(Id[-46])   # Set the points to the 46th and 47th because there is 91
    y2 = np.sqrt(Id[-47])   # points, so this is somwhere in the middle

    x1 = Vgs[-46 - i*90]
    x2 = Vgs[-47 - i*90]

    Slope = (y2 - y1) / (x2 - x1)
    # y = slope(x - x1) + y1
    # Vt = x when y = 0

    y = 0

    Vt = Vt + ( (y - y1)/Slope ) + x1 # This might cause an overflow, but whatever; fuck it
                                      # Let's see wheather Python can take that;
                                      # This is not my fault that I can't even check for fucking
                                      # overflow because this piece of garbage languge is supposed to
                                      # do fucking memory management for you;
                                      # in C/C++ I know that long long is 64bit or whatever and won't
                                      # overflow, but idk here; fuck this shit

    i += 1

Vt = Vt / 41
print(Vt);
