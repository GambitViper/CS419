# FILE CONTENTS:	This is a sample run of the learning program, 
# allowing the training set to grow up to 250 members, and 
# tracking results for learning in increments of 10. 
# Author: Zachary Baklund
# Date-Last-Modified: 3/10/18

from os import system, name
import math
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
    return vals

attribute_set = []

with open('./input_files/properties.txt', 'r') as f:
    
    for line in f:
        attribute_set.append(parse_and_create_attribute(line))

print(f"\nLoading Property Information from file.")
print(f"Loading Data from database.\n")

testing_set = list(data_set)
training_set = []

def pick_random_idx(set_size):
    idx = random.randint(0, set_size - 1)
    return idx

#Adds mushroom data to distinct training and testing sets for strict seperation
for x in range(t_size):
    idx = pick_random_idx(len(testing_set))
    training_set.append(testing_set[idx])
    testing_set.pop(idx)

# print(f"\nData_Set len: {len(data_set)}")
# print(f"Traing_Set len: {len(training_set)}")
# print(f"Testing_Set len: {len(testing_set)}\n")

def decision_tree_learning(examples, attributes, parent_examples):
    if(not examples or len(examples) == 0):
        # print(">>>in if of dst")
        return plurality_value(parent_examples)
    elif(test_classification_equality(examples)):
        # print(">>>in elif #1 of dst")
        return examples[0].classification()
    elif(not attributes or len(attributes) == 0):
        # print(">>>in elif #2 of dst")
        return plurality_value(examples)
    else:
        # print(">>>in else of dst")
        attribute = math_argmax([importance(a, examples) for a in attributes])
        tree = Tree(attribute)
        # print(f"pre-for {attribute}")
        attributes.pop(attribute)
        for v in attribute_set[attribute]:
            exs = find_matched_assignments(examples, v, attribute)
            # print(f"{attribute_set[attribute]} \n {attributes} \n {attribute}")
            subtree = decision_tree_learning(exs, attributes, examples)
            tree.add_child(subtree)
    return tree

def find_matched_assignments(examples, value, attribute):
    exs = []
    for ex in examples:
        if(ex.pick_property_at(attribute) == value):
            exs.append(ex)
    # print(exs)
    return exs

def math_argmax(set_of_data):
    h_idx = 0
    for s in range(len(set_of_data) - 1):
        if(set_of_data[s] > set_of_data[h_idx]):
            h_idx = s
    return h_idx

def test_classification_equality(examples):
    check = True
    classification = examples[0].classification()
    for ex in examples[1: (len(examples)-1)]:
        if(ex.classification() != classification):
            # print(f"testing classification : {ex.classification()}")
            check = False
    return check

def plurality_value(examples):
    count_e = 0
    count_p = 0
    for ex in examples:
        if(ex.classification == "p"):
            count_p = count_p + 1
        elif(ex.classification == "e"):
            count_e = count_e + 1
    if(count_e > count_p):
        return "e"
    elif(count_p > count_e):
        return "p"
    else:
        flip = random.randint(0, count_e + count_p)
        if(flip % 2 == 0):
            return "e"
        else:
            return "p"

def entropy(poisin, edible):
    entropy_attr = 0
    poisin_coef = 0
    edible_coef = 0
    if(poisin != 0):
        poisin_coef = poisin / (poisin + edible)
    if(edible != 0):
        edible_coef = edible / (poisin + edible)
    entropy_attr = 0
    if(poisin_coef != 0):
        entropy_attr += ( (poisin_coef) * math.log2(poisin_coef) )
    if(edible_coef != 0):
        entropy_attr += ( (edible_coef) * math.log2(edible_coef) )
    if(entropy_attr != 0):
        entropy_attr = entropy_attr * (-1)
    return entropy_attr

def importance(attribute, examples):
    entropy_arr = []
    total = []
    for a in attribute_set[attribute]:
        poisin = 0
        edible = 0
        for ex in examples:
            if(ex.pick_property_at(attribute) == a):
                if(ex.classification() == "e"):
                    edible = edible + 1
                else:
                    poisin = poisin + 1
        entropy_attr = entropy(poisin, edible)
        entropy_arr.append(entropy_attr)
        total.append(poisin + edible)
    # print(f"{attribute}...{entropy_arr}")
    # print(f"{attribute}...{total}")
    remainder = 0
    divisor = len(examples)
    for x in range(len(total)):
        remainder += (total[x] / divisor) * entropy_arr[x]
    # print(f"{attribute}...remainder...{remainder}")
    return (1 - remainder)

print(f"Collecting set of {t_size} training examples.\n")
for curr_incr in range(t_incr, t_size, t_incr):
    curr_training_set = []
    for ct in range(curr_incr):
        idx = pick_random_idx(len(training_set))
        curr_training_set.append(training_set[idx])
    
    # Build a decision tree for the current size of the incrementation on the training_set
    # print(f"=== len = {len(curr_training_set)}")
    decision_tree = decision_tree_learning(curr_training_set, list(range(21)), [])

    correct_decisions = 0
    total_tested = 0
    print(f"Running with {curr_incr} examples in training set.")
    for i in range(len(testing_set) - 1):
        mushroom = testing_set[i]
        test_tree = decision_tree
        while(not test_tree.is_leaf()):
            attr = test_tree.data
            mattr = mushroom.pick_property_at(attr)
            search = attribute_set[attr].index(mattr)
            test_tree = test_tree.children[search]
        if(mushroom.classification() == test_tree.data):
            # print(f"correctness-{mushroom.classification()} =? {test_tree.data}")
            correct_decisions += 1
        total_tested += 1
    print(decision_tree)
    # print(f"-correctness = {correct_decisions / total_tested}")
    correctness = (correct_decisions / total_tested) * 100
    pout = '{:.4f}'.format(correctness)
    outdata = (f"\nGiven current tree, there are {correct_decisions} correct classifications"
               f"\nout of {len(testing_set)} possible (a success rate of {pout} percent).\n")
    print(outdata)

            
        


