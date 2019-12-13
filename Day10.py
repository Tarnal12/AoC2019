import math

asteroids = []


def can_a_see_b(a, b):
    #print("Testing ", a, "vs.", b)
    x_diff = abs(b[0] - a[0])
    y_diff = abs(b[1] - a[1])
    if x_diff == 0 and y_diff == 0:
        return False
    elif x_diff == 0:
        for dy in range(1, y_diff):
            if b[1] > a[1]:
                coord_to_check = (a[0], a[1] + dy)
            else:
                coord_to_check = (a[0], a[1] - dy)

            if coord_to_check in asteroids:
                return False
    elif y_diff == 0:
        for dx in range(1, x_diff):
            if b[0] > a[0]:
                coord_to_check = (a[0] + dx, a[1])
            else:
                coord_to_check = (a[0] - dx, a[1])

            if coord_to_check in asteroids:
                return False
    else:
        common_factors = get_factors(x_diff).intersection(get_factors(y_diff))
        #print('Common factors =', common_factors)
        for factor in common_factors:
            dx = int((b[0] - a[0]) / factor)
            dy = int((b[1] - a[1]) / factor)
            i = 1
            while abs(dx * i) != x_diff and abs(dy * i) != y_diff:
                coord_to_check = (a[0] + (dx * i), a[1] + (dy * i))
                i = i + 1
                if coord_to_check in asteroids:
                    return False
    return True


def angle_to_target(a, b):
    if a[1] == b[1] and a[0] < b[0]:
        return 90
    if a[1] == b[1] and a[0] > b[0]:
        return 270
    if a[1] < b[1] and a[0] == b[0]:
        return 180
    if a[1] > b[1] and a[0] == b[0]:
        return 0

    tan = abs(b[0] - a[0]) / abs(b[1] - a[1])
    angle_of_incident = abs(math.degrees(math.atan(tan)))
    if a[0] <= b[0] and a[1] >= b[1]:      # Top-Right
        angle_of_incident = angle_of_incident + 0
    elif a[0] <= b[0] and a[1] <= b[1]:     # Bottom-Right
        angle_of_incident = angle_of_incident + 90
    elif a[0] >= b[0] and a[1] <= b[1]:    # Bottom-Left
        angle_of_incident = 270 - angle_of_incident
    elif a[0] >= b[0] and a[1] >= b[1]:   # Top-Left
        angle_of_incident = 360 - angle_of_incident
    #print('Angle between', a, 'and', b, 'is', angle_of_incident)
    return angle_of_incident % 360


def get_factors(n):
    #print(n)
    factors = set()
    for i in range(2, n + 1):
        #print('Checking: ', n, i, n%i)
        if n % i == 0:
            factors.add(i)
    #print(factors)
    return factors


if __name__ == '__main__':
    with open('Day10Input.txt', 'r') as f:
        y = 0
        for line in f:
            x = 0
            for letter in line.strip():
                if letter == '#':
                    asteroids.append((x, y))
                x = x + 1
            y = y + 1

    print(asteroids)

    best_base = asteroids[0]
    best_base_score = 0
    for base_asteroid in asteroids:
        num_visible = 0
        for viewable_asteroid in asteroids:
            if can_a_see_b(base_asteroid, viewable_asteroid):
                num_visible = num_visible + 1
        #print(num_visible)

        if num_visible > best_base_score:
            best_base = base_asteroid
            best_base_score = num_visible

    print('The best base is', best_base, 'scoring', best_base_score)

    asteroids.remove(best_base)
    asteroids_removed = 0
    while len(asteroids) > 0:
        targets = {}
        for target_asteroid in asteroids:
            if can_a_see_b(best_base, target_asteroid):
                angle = angle_to_target(best_base, target_asteroid)
                #print(best_base, 'to', target_asteroid, 'is', angle, 'degrees')
                targets[target_asteroid] = angle

        targets = {k: v for k, v in sorted(targets.items(), key=lambda item: item[1])}
        print("New rotation")
        print(targets)
        for target in targets:
            asteroids.remove(target)
            asteroids_removed = asteroids_removed + 1
            print('Destroyed', target, '-', asteroids_removed, 'gone.')
