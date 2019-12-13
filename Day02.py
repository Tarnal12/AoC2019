import csv
import sys


def run(noun=12, verb=2):
    f = open('Day02Input.txt', 'r')
    csv_reader = csv.reader(f)
    intcode_program = [int(i) for i in next(csv_reader)]

    intcode_program[1] = noun
    intcode_program[2] = verb

    i = 0
    while True:
        opcode = intcode_program[i]
        if opcode == 1:
            a = intcode_program[i + 1]
            b = intcode_program[i + 2]
            output_index = intcode_program[i + 3]
            intcode_program[output_index] = intcode_program[a] + intcode_program[b]
            i = i + 4
        elif opcode == 2:
            a = intcode_program[i + 1]
            b = intcode_program[i + 2]
            output_index = intcode_program[i + 3]
            intcode_program[output_index] = intcode_program[a] * intcode_program[b]
            i = i + 4
        elif opcode == 99:
            break

    return intcode_program[0]


print('Part 1 result = %d' % run())

for noun in range(0, 100):
    for verb in range(0, 100):
        output = run(noun, verb)
        if output == 19690720:
            print("Necessary inputs are %d, %d (answer = %d)" % (noun, verb, (noun * 100) + verb))
            sys.exit(0)
