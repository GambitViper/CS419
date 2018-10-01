# FILE CONTENTS:	A class to contain a basic implementation of a generic tree structure
# with one important distinction the importace function used to assign a value to how
# important any given attribute is to accurately describing the informational gain of the property 
# Author: Zachary Baklund
# Date-Last-Modified: 30/9/18

class Tree(object):

    def __init__(self, data, children=None, parent=None):
        self.data = data
        self.children = children or []
        self.parent = parent
    
    def __str__(self):
        if(self.is_leaf()):
            return str(self.data)
        return '{data} children=[{children}]'.format(data=self.data, children=', '.join(map(str, self.children)))

    def add_child(self, data):
        new_child = Tree(data, parent=self)
        self.children.append(new_child)
        return new_child

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.children
        