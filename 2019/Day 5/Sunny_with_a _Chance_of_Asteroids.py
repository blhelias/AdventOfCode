"""
Pour rappel :
    opcode 1 : ADD
    opcode 2 : MULTIPLY
    opcode 3 : Save input at the position of its parameter
    opcode 4 : output the value of its only parameter
    Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.

input = 0
3,12,9,12,15,1,13,14,13,4,13,99,0,0,1,9


    position mode : 0
    immediate mode : 1

    output 0 means success
    output non-0 means fail

Example:
    1002,4,3,4,33
"""

import os
import copy

# # INPUT = "1"
# INPUT = "5"


def add_omitted_zeros(opcode: str) -> str:
    return "{:>05}".format(opcode)


def test_diagnostic(sequence, intcode_input):
    instruction_pt = 0
    running = True
    OUTPUT = []

    while running:

        opcode = sequence[instruction_pt]
        opcode_with_zeros = add_omitted_zeros(opcode)

        if "99" in opcode_with_zeros:
            running = not running
            continue

        if opcode_with_zeros[2] == "0":
            instr1 = int(sequence[int(sequence[instruction_pt + 1])])
        else:
            instr1 = int(sequence[instruction_pt + 1])

        if opcode_with_zeros[1] == "0" and opcode_with_zeros[-1] != "4":
            instr2 = int(sequence[int(sequence[instruction_pt + 2])])
        else:
            instr2 = int(sequence[instruction_pt + 2])

        if opcode_with_zeros[-1] == "3" or opcode_with_zeros[-1] == "4":
            # read parameters and apply instructions
            if opcode_with_zeros[-1] == "4":
                OUTPUT.append(str(instr1))

            if opcode_with_zeros[-1] == "3":
                sequence[int(sequence[instruction_pt + 1])] = intcode_input

            increment = 2

        elif opcode_with_zeros[-1] == "5" or opcode_with_zeros[-1] == "6":
            # read parameters and apply instructions
            if opcode_with_zeros[-1] == "5":
                if str(instr1) != "0":
                    instruction_pt = instr2  # jump
                    increment = 0
                else:
                    increment = 3

            elif opcode_with_zeros[-1] == "6":
                if str(instr1) == "0":
                    instruction_pt = instr2  # jump
                    increment = 0
                else:
                    increment = 3
            else:
                increment = 3

        else:

            if opcode_with_zeros[-1] == "1":
                sequence[int(sequence[instruction_pt + 3])] = str(instr1 + instr2)

            elif opcode_with_zeros[-1] == "2":
                sequence[int(sequence[instruction_pt + 3])] = str(instr1 * instr2)

            elif opcode_with_zeros[-1] == "7":
                if instr1 < instr2:
                    sequence[int(sequence[instruction_pt + 3])] = "1"
                else:
                    sequence[int(sequence[instruction_pt + 3])] = "0"

            elif opcode_with_zeros[-1] == "8":
                if instr1 == instr2:
                    sequence[int(sequence[instruction_pt + 3])] = "1"
                else:
                    sequence[int(sequence[instruction_pt + 3])] = "0"

            increment = 4

        instruction_pt += increment

    return ",".join(sequence), ",".join(OUTPUT)


if __name__ == "__main__":
    # read Input file
    INPUT = 5
    with open("input.txt", "r") as input_file:
        program = input_file.readline()
        program_sequence = program.split(",")

        sequence, diagnostic = test_diagnostic(program_sequence, INPUT)

        print(diagnostic)
