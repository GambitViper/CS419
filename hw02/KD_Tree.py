from collections import namedtuple
from pprint import pformat

idx = 0

class Node(namedtuple('Node', 'point left_child right_child dim')):
    def __repr__(self):
        return pformat(tuple(self))      
    
def kdbuild(point_list, minSet, dimAtt, depth=0):
    # set size of the current list of points
    n = len(point_list)

    # dimensional axis for splitting and sorting to find the median
    dim_split = depth % int(dimAtt)
    sorted_points = sorted(point_list, key=lambda point: point[dim_split])
    mid = int(n / 2)

    if n <= int(minSet):
        return Node(
            point = sorted_points,
            left_child = None,
            right_child = None,
            dim = None
        )
    else:
        #0 - axis and dimension for splitting
        #1 - nodes that are less than or equal to median value on axis for splitting
        #2 - nodes that are greater than median value on axis for splitting
        return Node(
            point = sorted_points[mid][dim_split],                                #0 - No                              
            left_child = kdbuild(sorted_points[:mid], minSet, dimAtt, depth + 1), #1 - Noleft
            right_child = kdbuild(sorted_points[mid:], minSet, dimAtt, depth + 1), #2 - Noright
            dim = dim_split
        )

    