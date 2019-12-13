import csv


class IntCodeProgram:
    class Instruction:
        def __init__(self, instruction):
            self.opcode = int(instruction[3:])
            self.mode1 = int(instruction[2])
            self.mode2 = int(instruction[1])
            self.mode3 = int(instruction[0])

    def __init__(self, input_string, silent_mode=False):
        self.program = [int(i) for i in input_string]
        self.program.extend([0 for i in range(100000)])
        self.silent_mode = silent_mode
        self.outputs = []
        self.preloaded_inputs = []
        self.index = 0
        self.relative_index = 0

    def preload_inputs(self, inputs, clear_others=False):
        if clear_others:
            self.preloaded_inputs = []

        self.preloaded_inputs.extend(inputs)

    def get_last_output(self):
        return self.outputs[-1]

    def parse_instruction(self):
        return self.Instruction(str(self.program[self.index]).rjust(5, '0'))

    def fiddle_startup(self, noun, verb):
        self.program[1] = noun
        self.program[2] = verb

    def get_value(self, index, mode):
        param_value = self.program[index]
        if mode == 0:       # Positional
            return self.program[param_value]
        elif mode == 1:     # Immediate
            return param_value
        elif mode == 2:     # Relative
            return self.program[param_value + self.relative_index]

    def set_value(self, index, value, mode):
        param_value = self.program[index]
        if mode == 0:
            self.program[param_value] = value
        elif mode == 2:
            self.program[param_value + self.relative_index] = value

    def run(self, break_on_output=False):
        while True:
            instruction = self.parse_instruction()
            if instruction.opcode == 1:
                a = self.get_value(self.index + 1, instruction.mode1)
                b = self.get_value(self.index + 2, instruction.mode2)
                self.set_value(self.index + 3, a + b, instruction.mode3)
                self.index = self.index + 4
            elif instruction.opcode == 2:
                a = self.get_value(self.index + 1, instruction.mode1)
                b = self.get_value(self.index + 2, instruction.mode2)
                self.set_value(self.index + 3, a * b, instruction.mode3)
                self.index = self.index + 4
            elif instruction.opcode == 3:
                if len(self.preloaded_inputs) > 0:
                    val_to_use = self.preloaded_inputs[0]
                    self.preloaded_inputs = self.preloaded_inputs[1:]
                else:
                    val_to_use = int(input("Input: "))

                self.set_value(self.index + 1, val_to_use, instruction.mode1)
                self.index = self.index + 2
            elif instruction.opcode == 4:
                output = self.get_value(self.index + 1, instruction.mode1)
                if not self.silent_mode:
                    print(output)
                self.outputs.append(output)
                self.index = self.index + 2
                if break_on_output:
                    return output
            elif instruction.opcode == 5:
                if self.get_value(self.index + 1, instruction.mode1) != 0:
                    self.index = self.get_value(self.index + 2, instruction.mode2)
                else:
                    self.index = self.index + 3
            elif instruction.opcode == 6:
                if self.get_value(self.index + 1, instruction.mode1) == 0:
                    self.index = self.get_value(self.index + 2, instruction.mode2)
                else:
                    self.index = self.index + 3
            elif instruction.opcode == 7:
                if self.get_value(self.index + 1, instruction.mode1) < self.get_value(self.index + 2, instruction.mode2):
                    self.set_value(self.index + 3, 1, instruction.mode3)
                else:
                    self.set_value(self.index + 3, 0, instruction.mode3)
                self.index = self.index + 4
            elif instruction.opcode == 8:
                if self.get_value(self.index + 1, instruction.mode1) == self.get_value(self.index + 2, instruction.mode2):
                    self.set_value(self.index + 3, 1, instruction.mode3)
                else:
                    self.set_value(self.index + 3, 0, instruction.mode3)
                self.index = self.index + 4
            elif instruction.opcode == 9:
                relative_offset = self.get_value(self.index + 1, instruction.mode1)
                self.relative_index = self.relative_index + relative_offset
                self.index = self.index + 2
            elif instruction.opcode == 99:
                return -99


if __name__ == '__main__':
    f = open('Day05Input.txt', 'r')
    csv_reader = csv.reader(f)
    program_input = [i for i in next(csv_reader)]
    program = IntCodeProgram(program_input)
    results = 0
    while results != -1:
        results = program.run()
