# FILE CONTENTS:	This is a simple implementation of a utility for building 
# and training neural networks on some data extracted from image files. 
# This code allows the user to specify the structure of one or more 
# multi-layer feed-forward neural networks. 
# It will then train those networks by back-propagation. 
# The tool will also allow trained networks to be saved to files and 
# loaded again for later re-use.
# 
# (Note: Since this is a tool meant to allow a user to explore different possible 
#  data-sets and structures, it will be possible to repeat this process ad-infinitum.)
#
# Author: Zachary Baklund
# Date-Last-Modified: 26/10/18

import math
import random

import Utilities as util

def promptOption():
    check = True
    while check:
        try: 
            ui_ltq = input("Enter L to load trained network, T to train a new one, Q to quit: ")
            ui_ltq.lower()
            if ui_ltq != "l" and ui_ltq != "t" and ui_ltq != "q":
                util.clear()
            else:
                check = False
        except ValueError:
            util.clear()
    return ui_ltq

def promptRes():
    check = True
    while check:
        try:
            ui_res = int(input("Resolution of data (5/10/15/20): "))
            if ui_res <= 20 and ui_res % 5 == 0:
                check = False
        except ValueError:
            check = True
    return ui_res

def promptHLayers():
    # Non-negative integer no greater than 10; 
    # note that it mayin fact be 0 (resulting in a single-layer perceptron network
    check = True
    while check:
        try:
            ui_hamt = int(input("Number of hidden layers: "))
            if ui_hamt >= 0 and ui_hamt <= 10:
                check = False
        except ValueError:
            check = True
    return ui_hamt

def promptLayerSize(depth):
    # Each layer-size value will be a positive integer no greater than 500
    check = True
    while check:
        try: 
            ui_hiddensize = int(input(f"Size of hidden layer {depth + 1}: "))
            if ui_hiddensize >= 1 and ui_hiddensize <= 500:
                check = False
        except ValueError:
            check = True
    return ui_hiddensize

def promptFile():
    # Might check extension type after I define Network Save type
    return input("Network file-name: ")

def fetchFiles(res):
    # Define the function
    if res == 5:
        res = "05"
    trainFile = f"trainSet_{res}.dat"
    testFile = f"testSet_{res}.dat"
    # print(f"~Debug~ {res} -> {trainFile}, {testFile}")
    return [trainFile, testFile]            

def train():
    print("")
    resolution = promptRes()
    amt_hidden = promptHLayers()
    layer_total = amt_hidden + 2
    temp_h = []
    for h in range(amt_hidden):
        temp_h.append(promptLayerSize(h))

    print("\nInitializing network...")
    
    # Add constructor for NeuralNetwork
    
    trainingFiles = fetchFiles(resolution)

    print(f"Training on {trainingFiles[0]}...")
    
    # Add training algorithm here
    
    print(f"Testing on {trainingFiles[1]}...")
    
    # Add testing algorithm here
    accuracy = 0
    print(f"Accuracy achieved: {accuracy}%")

    
    



def load():
    print("")
    network_file = promptFile()
    try:
        with open(network_file, 'r') as f:
            for line in f:
                pass #do stuff here
    except IOError:
        print("Could not read file:", network_file)

def main():
    util.clear()
    while True:
        opt = promptOption()
        if opt == "t":
            train()
        elif opt == "l":
            load()
        else:
            print("\nGoodbye.")
            quit()
  
if __name__== "__main__":
    main()