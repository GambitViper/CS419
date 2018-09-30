# FILE CONTENTS:	This is a sample run of the learning program, 
# allowing the training set to grow up to 250 members, and 
# tracking results for learning in increments of 10. 
# Author: Zachary Baklund
# Date-Last-Modified: 24/9/18

from os import system, name
import random
from mushroom import Mushroom

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

def parse_and_create_obj(line):
    arr = line.strip().split(' ')
    return Mushroom(arr)

data_set = []

with open('./input_files/mushroom_data.txt', 'r') as f:

    for line in f:
        data_set.append(parse_and_create_obj(line))

testing_set = list(data_set)
training_set = []

def pick_random_idx(set_size):
    idx = random.randint(0, set_size - 1)
    print(f"...Choosing from size: {set_size}")
    print(f"...{idx}")
    return idx

for x in range(t_size):
    idx = pick_random_idx(len(testing_set))
    training_set.append(testing_set[idx])
    print(f"...Adding {testing_set[idx]} to Training_Set")
    testing_set.pop(idx)
    print(f"...Removing {training_set[x]} from Testing_Set")
    print(f"{training_set[x].debug_data()}\n...")

print(f"Data_Set len: {len(data_set)}")
print(f"Traing_Set len: {len(training_set)}")
print(f"Testing_Set len: {len(testing_set)}")