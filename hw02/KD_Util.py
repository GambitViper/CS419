import math

def distance(point1, point2):
    acc = 0

    for i in range(len(point1)):
        acc += (float(point1[i]) - float(point2[i])) ** 2
    
    return math.sqrt(acc)

def nearest_neighbor(all_points, new_point):
    best_point = None
    best_distance = None

    for current_point in all_points:
        current_distance = distance(new_point, current_point)

        if best_distance is None or current_distance < best_distance:
            best_distance = current_distance
            best_point = current_point
    
    return best_point