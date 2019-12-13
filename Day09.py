from Day05 import IntCodeProgram
import csv

if __name__ == '__main__':
    f = open('Day09Input.txt', 'r')
    csv_reader = csv.reader(f)
    program_input = [i for i in next(csv_reader)]
    prog = IntCodeProgram(program_input)
    results = prog.run()
