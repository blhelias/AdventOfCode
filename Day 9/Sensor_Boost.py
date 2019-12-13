import copy
from typing import List, Dict
from itertools import permutations

PHASES = range(5)
LOOP_MODE_PHASES = range(5, 10)


def add_omitted_zeros(opcode: str) -> str:
    return '{:>05}'.format(opcode)

def fill_memory_with_zeros(s, memory_overflow):
    return s + ["0" for _ in range((memory_overflow + 3) - len(s))]

def core_intcode(sequence: List[str], intcode_input: List[str], instruction_pt: int=0):
    """opcode logic:
        opcode 1 ADD
        opcode 2 MULTIPLY
        opcode 3 SAVE input at the position of its parameter
        opcode 4 OUTPUT the value of its only parameter
        Opcode 5 jump-if-true: if the first parameter is non-0,
                 it sets the instruction pointer to the value from the second parameter.
                 Otherwise, it does nothing.
        Opcode 6 jump-if-false: if the first parameter is zero,
                 it sets the instruction pointer to the value from
                 the second parameter. Otherwise, it does nothing.
        Opcode 7 is less than: if the first parameter is less than the second parameter,
                 it stores 1 in the position given by the third parameter.
                 Otherwise, it stores 0.
        Opcode 8 is equals: if the first parameter is equal to the second parameter,
                 it stores 1 in the position given by the third parameter.
                 Otherwise, it stores 0.
        Opcode 9 adjusts the relative base by the value of its only parameter.
    """
    input_counter = 0
    relative_base = 0
    output = []
    mode_2 = 0

    while True:
        # print("pointer: ", instruction_pt)
        opcode = sequence[instruction_pt]
        opcode_with_zeros = add_omitted_zeros(opcode)
        # print("opcode", opcode_with_zeros)
        if "99" in opcode_with_zeros:
            # print("Intcode halting after encountering 99 opcode")
            return ",".join(sequence), ",".join(output), 1, instruction_pt
        # PARAMETER 1
        if opcode_with_zeros[2] == "0":
            # Position mode
            try:
                instr1 = int(sequence[int(sequence[instruction_pt+1])])
            except IndexError as e:
                instr1 = 0
        elif opcode_with_zeros[2] == "1":
            # Immediate mode
            try:
                instr1 = int(sequence[instruction_pt+1])
            except IndexError as e:
                instr1 = 0
        elif opcode_with_zeros[2] == "2":
            # Relative mode
            try:
                instr1 = int(sequence[int(sequence[instruction_pt+1]) + relative_base])
            except IndexError as e:
                instr1 = 0
        else:
            # print("Invalid parameter 1 for opcode: " + opcode_with_zeros)
            pass
        # PARAMETER 2
        if opcode_with_zeros[1] == "0" and opcode_with_zeros[-1] not in ["3", "4", "9"]:
            # Position mode
            try:
                instr2 = int(sequence[int(sequence[instruction_pt+2])])
            except IndexError as e:
                instr2 = 0
        elif opcode_with_zeros[1] == "1" and opcode_with_zeros[-1] not in ["3", "4", "9"]:
            # Immediate mode
            try:
                instr2 = int(sequence[instruction_pt+2])
            except IndexError as e:
                instr2 = 0
        elif opcode_with_zeros[1] == "2" and opcode_with_zeros[-1] not in ["3", "4", "9"]:
            # Relative mode
            try:
                instr2 = int(sequence[int(sequence[instruction_pt+2]) + relative_base])
            except IndexError as e:
                instr2 = 0
        else:
            # print("Invalid parameter 2 for opcode: " + opcode_with_zeros)
            pass
        
        if opcode_with_zeros[0] == "2":
            mode_2 = 1
        else:
            mode_2 = 0

        # OPCODE if/else CONDITIONS
        if opcode_with_zeros[-1] in ["3", "4", "9"]:
            # read parameters and apply instructions
            if opcode_with_zeros[-1] == "4":
                output.append(str(instr1))

            elif opcode_with_zeros[-1] == "3":
                try:
                    if opcode_with_zeros[2] == "2":
                        sequence[int(sequence[instruction_pt+1]) + relative_base] = intcode_input[input_counter]
                    else:
                        sequence[int(sequence[instruction_pt+1])] = intcode_input[input_counter]
                    # input_counter += 1
                except IndexError:
                    # It means you don't have any input left to provide
                    print("NotMoreInput: Amplifier set to pause")
                    return ",".join(sequence), ",".join(output), 0, instruction_pt
            elif opcode_with_zeros[-1] == "9":
                relative_base += instr1
                # print("rel_base", relative_base)

            increment = 2

        # JUMP OPCODE
        elif opcode_with_zeros[-1] in ["5", "6"]:
        
            if opcode_with_zeros[-1] == "5":
                if str(instr1) != "0":
                    instruction_pt = instr2 # jump
                    increment = 0
                else:
                    increment = 3
            elif opcode_with_zeros[-1] == "6":
                if str(instr1) == "0":
                    instruction_pt = instr2 # jump
                    increment = 0
                else:
                    increment = 3

        else:
            if mode_2:
                offset = relative_base
                temp_pointer = int(sequence[instruction_pt+3])+offset
            else:
                offset = 0
                temp_pointer = int(sequence[instruction_pt+3])+offset

            if opcode_with_zeros[-1] == "1":
                try:
                    sequence[temp_pointer] = str(instr1 + instr2)
                except IndexError as e:
                    sequence = fill_memory_with_zeros(sequence, int(sequence[instruction_pt+3])+offset)
                    sequence[temp_pointer] = str(instr1 + instr2)

            elif opcode_with_zeros[-1] == "2":
                try:
                    sequence[temp_pointer] = str(instr1 * instr2)
                except IndexError as e:
                    sequence = fill_memory_with_zeros(sequence, temp_pointer)
                    sequence[temp_pointer] = str(instr1 * instr2)

            elif opcode_with_zeros[-1] == "7":
                if instr1 < instr2:
                    sequence[temp_pointer] = "1"
                else:
                    sequence[temp_pointer] = "0"

            elif opcode_with_zeros[-1] == "8":
                if instr1 == instr2:
                    sequence[temp_pointer] = "1"
                else:
                    sequence[temp_pointer] = "0"

            else:
                # print("An error occured with opcode: "+ opcode_with_zeros)
                pass

            increment = 4

        instruction_pt += increment

    return ",".join(sequence), ",".join(output), 0, 0

def run(sequence, input_):
    amp, diagnostic, status, pointer = core_intcode(sequence.split(","), [input_])
    return diagnostic

if __name__ == "__main__":

    assert run("109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99", "0") == "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    assert run("1102,34915192,34915192,7,4,7,99,0", "0") == "1219070632396864"
    assert run("104,1125899906842624,99", "0") == "1125899906842624"

    with open("input.txt", "r") as BOOST_PROGRAM:
        sequence = BOOST_PROGRAM.read()
        print(run(sequence, "1"))
        print(run(sequence, "2"))
        BOOST_PROGRAM.close()