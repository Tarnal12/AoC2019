with open('Day06Input.txt', 'r') as f:
    orbits = {}
    orbiters = {}
    for line in f:
        (center, orbiter) = line.strip().split(')')
        orbits[orbiter] = center
        if center in orbiters:
            orbiters[center].append(orbiter)
        else:
            orbiters[center] = [orbiter]
    print(orbits)
    print(orbiters)

    # Calc total number of direct + indirect orbits
    checksum = 0
    for key in orbits.keys():
        indirect_orbits = 0
        which_orbits = orbits[key]
        while which_orbits != 'COM':
            which_orbits = orbits[which_orbits]
            indirect_orbits = indirect_orbits + 1
        print('%s has %d orbits' % (key, indirect_orbits + 1))
        checksum = checksum + indirect_orbits + 1
    print('Sum of all direct and indirect orbits = %d' % checksum)

    # Calc minimum number of transfers from YOU to whatever SAN orbits
    start = orbits['YOU']
    target = orbits['SAN']
    route_found = False
    steps_taken = 0
    possible_locations = {start}
    while not route_found:
        new_locations = set()
        steps_taken = steps_taken + 1
        for start_loc in possible_locations:
            if start_loc in orbits:
                new_locations.add(orbits[start_loc])

            if start_loc in orbiters:
                for orbiter in orbiters[start_loc]:
                    new_locations.add(orbiter)

        possible_locations.update(x for x in new_locations if x not in possible_locations)
        print('----- After %d Steps -----' % steps_taken)
        print(possible_locations)
        if target in possible_locations:
            route_found = True
            break

    print(steps_taken)
