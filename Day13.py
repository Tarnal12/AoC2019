from Day05 import IntCodeProgram
import csv
from os import system


class Grid:
    def __init__(self):
        self.x_size = 46
        self.y_size = 26
        self.score = 0
        self.grid = [['0' for i in range(self.x_size)] for j in range(self.y_size)]
        self.filled_in = False
        print(self.grid)

    def set_cell(self, x, y, val):
        if x == -1 and y == 0:
            self.score = val
        else:
            self.grid[y][x] = val

        # Print, if the screen has been fully initialised
        if y == self.y_size - 1 and x == self.x_size - 1:
            self.filled_in = True
        #if self.filled_in:
        #    print(self)

    def __str__(self):
        system('clear')
        str_rep = '  SCORE = %d\n' % self.score
        for row in self.grid:
            for cell in row:
                if cell == 0:
                    str_rep = str_rep + ' '
                elif cell == 1:
                    str_rep = str_rep + '#'
                elif cell == 2:
                    str_rep = str_rep + '~'
                elif cell == 3:
                    str_rep = str_rep + '-'
                elif cell == 4:
                    str_rep = str_rep + '*'
            str_rep = str_rep + '\n'
        return str_rep


f = open('Day13Input.txt', 'r')
csv_reader = csv.reader(f)
program_input = [i for i in next(csv_reader)]
program = IntCodeProgram(program_input, silent_mode=True)
program.program[0] = 2
game_screen = Grid()
ball_xpos = -1
paddle_xpos = -1
while True:
    result = program.run(break_on_output=True)
    if result == -99:
        break

    output_triplet = []
    output_triplet.append(result)
    output_triplet.append(program.run(break_on_output=True))
    output_triplet.append(program.run(break_on_output=True))

    if output_triplet[2] == 4:
        ball_xpos = output_triplet[0]
        if paddle_xpos < ball_xpos:
            program.preload_inputs([1], True)
        elif paddle_xpos > ball_xpos:
            program.preload_inputs([-1], True)
        else:
            program.preload_inputs([0], True)
    if output_triplet[2] == 3:
        paddle_xpos = output_triplet[0]

    game_screen.set_cell(output_triplet[0], output_triplet[1], output_triplet[2])

    # print(output_triplet)
print(game_screen.score)