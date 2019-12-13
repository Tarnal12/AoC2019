from Day05 import IntCodeProgram
import csv
import itertools

if __name__ == '__main__':
    f = open('Day07Input.txt', 'r')
    csv_reader = csv.reader(f)
    program_input = [i for i in next(csv_reader)]

    ## Part 1
    phase_seqs = list(itertools.permutations([0, 1, 2, 3, 4]))
    max_out = 0
    max_setting = []
    for seq in phase_seqs:
        prev_output = 0
        for amp in seq:
            program = IntCodeProgram(program_input, silent_mode=True)
            program.preload_inputs([amp, prev_output])
            result = program.run(break_on_output=True)
            prev_output = result

        if prev_output > max_out:
            max_out = prev_output
            max_setting = seq

    print("Best thrust obtainable is %d using phase inputs %s" % (max_out, '-'.join([str(i) for i in max_setting])))

    ## Part 2
    phase_seqs = list(itertools.permutations([5, 6, 7, 8, 9]))
    max_out = 0
    max_setting = []
    for seq in phase_seqs:
        prev_output = 0
        ampA = IntCodeProgram(program_input, silent_mode=True)
        ampA.preload_inputs([seq[0]])
        ampB = IntCodeProgram(program_input, silent_mode=True)
        ampB.preload_inputs([seq[1]])
        ampC = IntCodeProgram(program_input, silent_mode=True)
        ampC.preload_inputs([seq[2]])
        ampD = IntCodeProgram(program_input, silent_mode=True)
        ampD.preload_inputs([seq[3]])
        ampE = IntCodeProgram(program_input, silent_mode=True)
        ampE.preload_inputs([seq[4]])
        first_loop = True
        output = 0
        while output != -1:
            if first_loop:
                ampA.preload_inputs([0])
                first_loop = False
            else:
                ampA.preload_inputs([ampE.get_last_output()])
            ampA.run(break_on_output=True)

            ampB.preload_inputs([ampA.get_last_output()])
            ampB.run(break_on_output=True)

            ampC.preload_inputs([ampB.get_last_output()])
            ampC.run(break_on_output=True)

            ampD.preload_inputs([ampC.get_last_output()])
            ampD.run(break_on_output=True)

            ampE.preload_inputs([ampD.get_last_output()])
            output = ampE.run(break_on_output=True)

        output = ampE.get_last_output()
        if output > max_out:
            max_out = output
            max_setting = seq

    print("Best thrust obtainable is %d using phase inputs %s" % (max_out, '-'.join([str(i) for i in max_setting])))