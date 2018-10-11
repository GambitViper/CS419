# FILE CONTENTS:	This is a simple implementation for
# constructing K-D trees and then finding neighbor sets
# for some data along with the nearest neighbor in that set.
# Classifying new data according to median values of tree. 
# Author: Zachary Baklund
# Date-Last-Modified: 10/10/18

from os import system, name
import sys

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    
    # for mac and linux
    else:
        _ = system('clear')

clear()

dataFile = sys.argv[1]
minSetSize = sys.argv[2]

print(f"...Extracting Data from {dataFile}")
print(f"minimal set-size: {minSetSize}")

dataFeed = []
with open(dataFile, 'r') as f:

    for line in f:
        dataFeed.append(line.strip('\n\r').split(' '))

dimensions = dataFeed[0][0]
data = dataFeed[1:len(dataFeed)]
print(f"data-set defined with {dimensions} dimensions")
for d in data:
    print(d)