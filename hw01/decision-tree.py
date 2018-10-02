# FILE CONTENTS:	This is a sample run of the learning program, 
# allowing the training set to grow up to 250 members, and 
# tracking results for learning in increments of 10. 
# Author: Zachary Baklund
# Date-Last-Modified: 24/9/18

from os import system, name
import random
from mushroom import Mushroom
from tree import Tree
from attribute import Attribute

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    
    # for mac and linux
    else:
        _ = system('clear')

clear()
t_size = 0
t_incr = 0
check_t_size = True
while check_t_size:
    try:
        usr_training_set_size = input("Please enter a training set size (a positive multiple of 250 that is <= 1000): ")
        t_size = int(usr_training_set_size)
        if(t_size % 250 != 0 or t_size > 1000):
            clear()
            print("--Invalid training set size---")
        else:
            check_t_size = False
    except ValueError:
        clear()
        print("--Unnacceptable Value Type---")

check_t_incr = True
while check_t_incr:
    try:
        usr_training_increment = input("Please enter a training increment (either 10, 25, or 50): ")
        t_incr = int(usr_training_increment)
        if(t_incr != 10 and t_incr != 25 and t_incr != 50):
            clear()
            print("--Invalid training increment--")
        else:
            check_t_incr = False
    except ValueError:
        clear()
        print("--Unnacceptable Value Type--")

def parse_and_create_mushroom(line):
    arr = line.strip().split(' ')
    return Mushroom(arr)

data_set = []

with open('./input_files/mushroom_data.txt', 'r') as f:

    for line in f:
        data_set.append(parse_and_create_mushroom(line))

def parse_and_create_attribute(line):
    arr = line.strip().split(':')
    vals = arr[1].strip().split(' ')
    return Attribute(arr[0], vals)

attribute_set = []

with open('./input_files/properties.txt', 'r') as f:
    
    for line in f:
        attribute_set.append(parse_and_create_attribute(line))

testing_set = list(data_set)
training_set = []

def pick_random_idx(set_size):
    idx = random.randint(0, set_size - 1)
    return idx

#Adds mushroom data to distinct training and testing sets for strict seperation
for x in range(t_size):
    idx = pick_random_idx(len(testing_set))
    training_set.append(testing_set[idx])
    # print(f"...Adding {testing_set[idx]} to Training_Set")
    testing_set.pop(idx)
    # print(f"...Removing {training_set[x]} from Testing_Set")

print(f"\nData_Set len: {len(data_set)}")
print(f"Traing_Set len: {len(training_set)}")
print(f"Testing_Set len: {len(testing_set)}\n")

for curr_incr in range(t_incr, t_size + 1, t_incr):
    curr_training_set = []
    for ct in range(curr_incr):
        idx = pick_random_idx(len(training_set))
        curr_training_set.append(training_set[idx])
    
    # Build a decision tree for the current size of the incrementation on the training_set
    


def decision_tree_learning(examples, attributes, parent_examples):
    if(not examples):
        return plurality_value(parent_examples)
    elif(test_classification_equality(examples)):
        return examples[0].classification
    elif(not attributes):
        return plurality_value(examples)
    else:
        a_idx = math_argmax([importance(a) for a in attributes])
        tree = Tree(a_idx)
        for v in attributes[a_idx]:
            exs = find_matched_assignments(examples, v)
            reduced_attributes = remove_attr(a_idx, attributes)
            subtree = decision_tree_learning(exs, reduced_attributes, examples)
            tree.add_child(subtree)
        return tree  

def find_matched_assignments(examples, value):
    exs = []
    for ex in examples:
        if(ex.pick_property_at(0) == value):
            exs.append(ex)
        
    return exs

def math_argmax(set_of_data):
    h_idx = 0
    for s in range(len(set_of_data) - 1):
        if(set_of_data[s] > set_of_data[h_idx]):
            h_idx = s
    return h_idx

def test_classification_equality(examples):
    check = False
    classification = examples[0].classification
    for ex in examples[1: (len(examples)-1)]:
        if(ex.classification != classification):
            check = True
    return check

# def plurality_value(examples):

# def importance(attribute, examples):
#     for v in range(len(attribute) - 1):