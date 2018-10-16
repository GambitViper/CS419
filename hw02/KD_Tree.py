from collections import namedtuple
from pprint import pformat

class Node(namedtuple('Node', 'point left_child right_child')):
    def __repr__(self):
        return pformat(tuple(self))
    
def kdbuild(point_list, minSet, dimAtt, depth=0):

    n = len(point_list)

    dim_split = depth % int(dimAtt)
    sorted_points = sorted(point_list, key=lambda point: point[dim_split])
    mid = int(n / 2)

    if n <= int(minSet):
        return Node(
            point = sorted_points,
            left_child = None,
            right_child = None
        )

    return Node(
        point = sorted_points[mid],
        left_child = kdbuild(sorted_points[:mid], minSet, dimAtt, depth + 1),
        right_child = kdbuild(sorted_points[mid + 1:], minSet, dimAtt, depth + 1)
    )
    