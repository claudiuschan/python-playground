#!/usr/bin/python

#based on the Bailey-Borwein-Plouffe formula
from math import pi

k = 10
ppi = 0

for i in range(k):
    ppi += (1/16**i) * (4/(8*i+1) - 2/(8*i+4) - 1/(8*i+5) - 1/(8*i+6))
    
 

print("Built-in PI value: {:.{}g}".format(pi, k))
print("Calculated  value: {:.{}g}".format(ppi, k))