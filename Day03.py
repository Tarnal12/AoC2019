def trace_path(route):
    stages = route.split(',')
    (x, y) = (0, 0)
    places_visited = []
    for stage in stages:
        direction = stage[0]
        distance = int(stage[1:])
        for i in range(distance):
            if direction == 'U':
                y = y + 1
            if direction == 'D':
                y = y - 1
            if direction == 'L':
                x = x - 1
            if direction == 'R':
                x = x + 1

            places_visited.append((x, y))

    return places_visited


def manhattan_distance(point):
    return abs(point[0]) + abs(point[1])


def min_manhattan_distance(points):
    closest_point = points[0]
    for point in points:
        if manhattan_distance(point) < manhattan_distance(closest_point):
            closest_point = point

    return closest_point


def num_steps(point, route):
    i = 0
    for loc in route:
        i = i + 1
        if point == loc:
            return i


with open('Day03Input.txt', 'r') as f:
    wire1 = f.readline()
    wire2 = f.readline()

route1 = trace_path(wire1)
print('Route 1 Calced - Length = %d' % len(route1))
route2 = trace_path(wire2)
print('Route 2 Calced - Length = %d' % len(route2))
closest_intersection = (9999, 9999)
for point1 in route1:
    if point1 in route2 and manhattan_distance(point1) < manhattan_distance(closest_intersection):
        closest_intersection = point1

print(manhattan_distance(closest_intersection))

least_steps = 999999999
for point1 in route1:
    if point1 in route2 and num_steps(point1, route1) + num_steps(point1, route2) < least_steps:
        least_steps = num_steps(point1, route1) + num_steps(point1, route2)

print(least_steps)
