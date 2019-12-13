from math import gcd

class moon:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.dx = 0
        self.dy = 0
        self.dz = 0
        self.init_x = self.x
        self.init_y = self.y
        self.init_z = self.z

    def at_start(self):
        return self.at_initial_x() and self.at_initial_y() and self.at_initial_z()

    def at_initial_x(self):
        return self.init_x == self.x

    def at_initial_y(self):
        return self.init_y == self.y

    def at_initial_z(self):
        return self.init_z == self.z

    def gravitate(self, other):
        if self.x < other.x:
            self.dx = self.dx + 1
        if self.x > other.x:
            self.dx = self.dx - 1

        if self.y < other.y:
            self.dy = self.dy + 1
        if self.y > other.y:
            self.dy = self.dy - 1

        if self.z < other.z:
            self.dz = self.dz + 1
        if self.z > other.z:
            self.dz = self.dz - 1

    def tick(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.z = self.z + self.dz

    def get_total_energy(self):
        return self.get_kinetic_energy() * self.get_potential_energy()

    def get_potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def get_kinetic_energy(self):
        return abs(self.dx) + abs(self.dy) + abs(self.dz)

    def __str__(self):
        return "%s: pos=<x=%d, y=%d, z=%d>, vel=<x=%d, y=%d, z=%d>" % (
            self.name,
            self.x,
            self.y,
            self.z,
            self.dx,
            self.dy,
            self.dz
        )

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    moon_names = ['Io', 'Europa', 'Ganymede', 'Callisto']
    moon_index = 0
    with open("Day12Input.txt", "r") as f:
        moons = []
        for line in f:
            line = line.strip().strip('<').strip('>')
            coords = line.split(',')
            x_coord = int(coords[0].split('=')[1])
            y_coord = int(coords[1].split('=')[1])
            z_coord = int(coords[2].split('=')[1])
            moon_name = moon_names[moon_index]
            moon_index = moon_index + 1

            new_moon = moon(moon_name, x_coord, y_coord, z_coord)
            print(new_moon)
            moons.append(new_moon)

    for i in range(1000):
        for moon in moons:
            for other_moon in moons:
                if moon != other_moon:
                    moon.gravitate(other_moon)

        for moon in moons:
            moon.tick()
            print(moon)

        print()

    total_energy = 0
    for moon in moons:
        energy = moon.get_total_energy()
        print(moon.name, "energy =", energy)
        total_energy = total_energy + energy
    print(total_energy)

    steps_taken = 1000
    x_cycle = -1
    y_cycle = -1
    z_cycle = -1
    while x_cycle < 0 or y_cycle < 0 or z_cycle < 0:
        for moon in moons:
            for other_moon in moons:
                if moon != other_moon:
                    moon.gravitate(other_moon)

        for moon in moons:
            moon.tick()

        steps_taken = steps_taken + 1
        if x_cycle < 0 and moons[0].at_initial_x() and moons[1].at_initial_x() and moons[2].at_initial_x() and moons[3].at_initial_x():
            x_cycle = steps_taken + 1
        if y_cycle < 0 and moons[0].at_initial_y() and moons[1].at_initial_y() and moons[2].at_initial_y() and moons[3].at_initial_y():
            y_cycle = steps_taken + 1
        if z_cycle < 0 and moons[0].at_initial_z() and moons[1].at_initial_z() and moons[2].at_initial_z() and moons[3].at_initial_z():
            z_cycle = steps_taken + 1

    cycles = [x_cycle, y_cycle, z_cycle]
    print(cycles)
    lcm = cycles[0]
    for i in cycles[1:]:
        lcm = lcm * i // gcd(lcm, i)

    print("For full meeting we need %d cycles" % lcm)
