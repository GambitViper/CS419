from collections import namedtuple
from pprint import pformat

class Node(namedtuple('Node', 'location left_child right_child')):
    def __repr__(self):
        return pformat(tuple(self))
    
def kdbuild(point_list, minSet, dimAtt, depth=0):
    n = len(point_list)

    if n <= 0:
        return None

    dim_split = depth % dimAtt
    sorted_points = sorted(point_list, key=lambda point: point[dim_split])
    mid = int(n / 2)

    return Node(
        location = sorted_points[mid],
        left_child = kdbuild(sorted_points[:mid], minSet, dimAtt, depth + 1),
        right_child = kdbuild(sorted_points[mid + 1:], minSet, dimAtt, depth + 1)
    )

# def kdtree_closest_point(root, point, dimAtt, depth=0, best=None):
#     if root is None:
#         return best
    
#     dim_split = depth % dimAtt
    