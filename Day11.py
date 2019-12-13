from Day05 import IntCodeProgram
import csv


class HullRobot:
    def __init__(self):
        self.direction = 0  # North
        self.position = (0, 0)
        self.history = [self.position]
        self.paint_grid = {self.position: 1}

    def paint(self, color_val):
        self.paint_grid[self.position] = color_val

    def check_position(self):
        if self.position in self.paint_grid:
            return self.paint_grid[self.position]
        else:
            return 0

    def turn(self, dir_val):
        # Turn
        if dir_val == 0:
            self.direction = self.direction - 1
        elif dir_val == 1:
            self.direction = self.direction + 1
        self.direction = self.direction % 4

        # Move (NESW)
        if self.direction == 0:
            self.position = (self.position[0], self.position[1] + 1)
        if self.direction == 1:
            self.position = (self.position[0] + 1, self.position[1])
        if self.direction == 2:
            self.position = (self.position[0], self.position[1] - 1)
        if self.direction == 3:
            self.position = (self.position[0] - 1, self.position[1])
        self.history.append(self.position)


if __name__ == '__main__':
    f = open('Day11Input.txt', 'r')
    csv_reader = csv.reader(f)
    program_input = [i for i in next(csv_reader)]
    program = IntCodeProgram(program_input, silent_mode=True)
    robot = HullRobot()
    result = 0
    while True:
        current_cell = robot.check_position()
        program.preload_inputs([current_cell])

        paint_instruction = program.run(break_on_output=True)
        if paint_instruction == -1:
            break
        robot.paint(paint_instruction)

        turn_instruction = program.run(break_on_output=True)
        if paint_instruction == -1:
            break
        robot.turn(turn_instruction)

    painted_cells = [x for x in robot.paint_grid]
    print("%d panels painted." % len(painted_cells))

    black_cells = [x for x in robot.paint_grid if robot.paint_grid[x] == 1]
    black_cells.sort()
    print(black_cells)
    for i in range(10, -10, -1):
        line = ''
        for j in range(40):
            if (j, i) in black_cells:
                line = line + '#'
            else:
                line = line + '.'
        print(line)
