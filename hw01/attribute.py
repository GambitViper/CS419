# FILE CONTENTS:	A class to contain the information and 
# methods associated with instances of the data from the data set: properties.txt 
# Author: Zachary Baklund
# Date-Last-Modified: 30/9/18

class Attribute:

    def __init__(self, name, values):
        self.name = name
        self.values = values

    def debug_data(self):
        string = ("\n ~~~~~Attribute~~~~~\n"
                f"Name: \t{self.name},\n"
                f"Values: \t{self.values}\n"
                f"~~~~~~~~~~~~~~~~~~~ \n")
        return string

    def pick_property_at(self, pos):
        return self.asArray[pos]

    def pick_random_prop(self):
        idx = pick_random_idx(len(self.asArray))
        return self.asArray[idx]

    def pick_random_idx(set_size):
        idx = random.randint(0, set_size - 1)
        print(f"...Choosing from size: {set_size}")
        print(f"...{idx}")
        return idx

    def classification(self):
        return self.pick_property_at(22)