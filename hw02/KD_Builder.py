# FILE CONTENTS:	This is a simple implementation for
# constructing K-D trees and then finding neighbor sets
# for some data along with the nearest neighbor in that set.
# Classifying new data according to median values of tree. 
# Author: Zachary Baklund
# Date-Last-Modified: 10/10/18

from os import system, name
import sys
from KD_Tree import kdbuild, Node
from KD_Util import distance, nearest_neighbor

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    
    # for mac and linux
    else:
        _ = system('clear')

clear()

debug = False

def open_to_parse(fileName):
    dataFeed = []
    with open(fileName, 'r') as f:
        for line in f:
            dataFeed.append(tuple(line.strip('\n\r').split(' ')))
    return dataFeed

dataFile = sys.argv[1]
minSetSize = sys.argv[2]

dataFeed = open_to_parse(dataFile)

dimensions = dataFeed[0][0]
data = dataFeed[1:]
tree = kdbuild(data, minSetSize, dimensions)

if(debug):
    print(f"dimensions = {dimensions}")
    print(tree)

idx = 0

def getBounding(node):
    points = getattr(node, "point")
    total_dims = len(points[0])
    minVal = list(points[0])
    maxVal = list(points[0])
    for point in points[1:]:
        for i in range(total_dims):
            if point[i] < minVal[i]:
                minVal[i] = point[i]
            if point[i] > maxVal[i]:
                maxVal[i] = point[i]
    return [tuple(minVal), tuple(maxVal)]
    
def printPathRec(node, path):
    global idx
    if node == None:
        return ""
    elif getattr(node, "left_child") == None and getattr(node, "right_child") == None:
        retVal = f"\n{idx}. {path} : Bounding Box: {getBounding(node)}\nData in leaf: {getattr(node, 'point')}\n"
        idx += 1
        return retVal
    else:
        return printPathRec(getattr(node, "left_child"), path + "L") + printPathRec(getattr(node, "right_child"), path + "R")

def printPath(node):
    if debug:
        print("Starting recursion")
    return printPathRec(node , "")

def print_leaves(tree):
    #function that prints the leaves and bounding boxes of each leaf
    printed_leaves = printPath(tree)
    print(printed_leaves)

def find_leaf(test_point, node):
    if node == None:
        return node
    elif getattr(node, "left_child") == None and getattr(node, "right_child") == None:
        return node
    else:
        dim = getattr(node, "dim")
        if test_point[dim] < getattr(node, "point"):
            return find_leaf(test_point, getattr(node, "left_child"))
        else:
            return find_leaf(test_point, getattr(node, "right_child"))

def test_against_kdtree(test_points):
    for test_point in test_points:
        neighbor_leaf = find_leaf(test_point, tree)
        if neighbor_leaf == None:
            print(f"{test_point} has no nearest neighbor (in an empty set).")
        else:
            nearest_point = nearest_neighbor(getattr(neighbor_leaf, "point"), test_point)
            distance_to_point = distance(test_point, nearest_point)
            print(f"\n{test_point} is in the set: {getattr(neighbor_leaf, 'point')}\nNearest neighbor: {nearest_point} (distance = {distance_to_point})\n")



def test_data_prompt():
    #function prompts user to whether or not they wish to test data
    ui_test_data = input("Test data? (Enter Y for yes, anything else to quit): ")
    if ui_test_data == 'y' or ui_test_data == 'Y':
        #prompt user for name of their data file within current directory
        ui_test_data_file = input("Name of data-file: ")
        test_tree_data = open_to_parse(ui_test_data_file)
        test_dimensions = test_tree_data[0][0]
        test_data = test_tree_data[1:]
        #traversing the tree and then finding the closest distance
        test_against_kdtree(test_data)
    print(f"\n------------------------\n")
    print(f"Goodbye.")


def main():
    clear()
    ui_print_tree_leaves = input("Print tree leaves? (Enter Y for yes, anything else for no): ")
    if ui_print_tree_leaves == 'y' or ui_print_tree_leaves == 'Y':
        #call function for printing the leaves of the tree
        #then call prompt for testing data
        print(f"\n------------------------")
        print_leaves(tree)
        print(f"------------------------\n")
        test_data_prompt()
    else:
        #call prompt for testing data
        test_data_prompt()

main()
