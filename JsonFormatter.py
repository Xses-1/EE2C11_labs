import json
from pprint import pprint

path = input("input path")
file = open(path, 'r')

file.seek(0)
x = file.readline()
x = file.read().split('Step Information: ')

for i in range(1, len(x)):
    x[i] =x[i].split('\n')

for i in range(1, len(x)):
    DC_val = x[i][0].split('=')[1].split(' ')[0]
    x[i][0] = DC_val
    for j in range(1, len(x[i])):
        x[i][j] = x[i][j].split('\t')

pprint(x)

jsobject = json.dumps(x, indent = 4)

with open("sample.json", "w") as outfile:
    outfile.write(jsobject)

print(json)


#for line in file
#file.readline()