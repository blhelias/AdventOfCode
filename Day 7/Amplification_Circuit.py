"""
position mode : 0
immediate mode : 1

output 0 means success
output non-0 means fail
"""
import os
import copy
from typing import List, Dict
from itertools import permutations

PHASES = range(5)
LOOP_MODE_PHASES = range(5, 10)


def add_omitted_zeros(opcode: str) -> str:
    return '{:>05}'.format(opcode)

def test_diagnostic(sequence: List[str], intcode_input: List[str], instruction_pt: int=0):
    """opcode logic:
        opcode 1 : ADD
        opcode 2 : MULTIPLY
        opcode 3 : Save input at the position of its parameter
        opcode 4 : output the value of its only parameter
        Opcode 5 is jump-if-true: if the first parameter is 
                 non-zero, it sets the instruction pointer to 
                 the value from the second parameter. Otherwise, it does nothing.
        Opcode 6 is jump-if-false: if the first parameter is zero, 
                 it sets the instruction pointer to the value from 
                 the second parameter. Otherwise, it does nothing.
        Opcode 7 is less than: if the first parameter is less than the second parameter, 
                 it stores 1 in the position given by the third parameter. 
                 Otherwise, it stores 0.
        Opcode 8 is equals: if the first parameter is equal to the second parameter, 
                 it stores 1 in the position given by the third parameter. 
                 Otherwise, it stores 0.
    """
    input_counter = 0
    
    output = []

    while True:
        opcode = sequence[instruction_pt]
        opcode_with_zeros = add_omitted_zeros(opcode)

        if "99" in opcode_with_zeros:
            # print("Intcode halting after encountering 99 opcode")
            return ",".join(sequence), ",".join(output), 1, instruction_pt

        if opcode_with_zeros[2] == "0":
            # Position mode
            instr1 = int(sequence[int(sequence[instruction_pt+1])])
        else:
            # Immediate mode
            instr1 = int(sequence[instruction_pt+1])

        # No second instruction with opcode 4 and 3
        if (opcode_with_zeros[1] == "0" and opcode_with_zeros[-1] != "4" and opcode_with_zeros[-1] != "3"):
            # Position mode
            instr2 = int(sequence[int(sequence[instruction_pt+2])])
        else:
            # Immediate mode
            instr2 = int(sequence[instruction_pt+2])

        if opcode_with_zeros[-1] == "3" or opcode_with_zeros[-1] == "4":
            # read parameters and apply instructions
            if opcode_with_zeros[-1] == "4":
                output.append(str(instr1))
            
            if opcode_with_zeros[-1] == "3":
                try:
                    sequence[int(sequence[instruction_pt+1])] = intcode_input[input_counter]
                    input_counter += 1
                except IndexError:
                    # It means you don't have any input left to provide
                    # print("NotMoreInput: Amplifier set to pause")
                    return ",".join(sequence), ",".join(output), 0, instruction_pt
                
            increment = 2
        # JUMP OPCODE
        elif opcode_with_zeros[-1] == "5" or opcode_with_zeros[-1] == "6":
            # read parameters and apply instructions
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
                increment = 3
            
        else:

            if opcode_with_zeros[-1] == "1":
                sequence[int(sequence[instruction_pt+3])] = str(instr1 + instr2)
            
            elif opcode_with_zeros[-1] == "2":
                sequence[int(sequence[instruction_pt+3])] = str(instr1 * instr2)
            
            elif opcode_with_zeros[-1] == "7":
                if instr1 < instr2:
                    sequence[int(sequence[instruction_pt+3])] = "1"
                else:
                    sequence[int(sequence[instruction_pt+3])] = "0"

            elif opcode_with_zeros[-1] == "8":
                if instr1 == instr2:
                    sequence[int(sequence[instruction_pt+3])] = "1"
                else:
                    sequence[int(sequence[instruction_pt+3])] = "0"

            else:
                print("An error occured with opcode: "+ opcode_with_zeros)

            increment = 4
        
        instruction_pt += increment

    return ",".join(sequence), ",".join(output), 0, 0


def run(intcode, init_input):
    reponse = []

    for phases_settings in permutations(LOOP_MODE_PHASES):
        input_ = init_input
        for phase in phases_settings:
            try:
                sequence = copy.deepcopy(intcode)
                sequence, diagnostic, _ = test_diagnostic(sequence, (str(phase), input_))

                input_ = diagnostic     

            except IndexError as e:
                print("Verifiez l'input")
                print(e)
        reponse.append(diagnostic)
    return reponse

def init_amplifiers(sequence, phase_settings):
    """initialize each amplifier with corresponding phase
    and save it in a map
    """
    config_map = {}

    for idx, phase in enumerate(phase_settings):
        s = copy.deepcopy(sequence)
        amp, diagnostic, status, pointer = test_diagnostic(s, [phase])
        
        config_map[idx] = {"intcode": amp,
                            "output": diagnostic,
                            "status": status,
                            "pointer": pointer}

    return config_map

def run_bis(intcode, init_input):
    # 2 - make the loop 
    response = []

    for phases_settings in permutations(LOOP_MODE_PHASES):

        amplifiers_states = init_amplifiers(intcode, phases_settings)

        input_ = init_input
        running = True
        
        while running:
            for amp_key in range(5):

                amp, diagnostic, status, pointer = test_diagnostic(amplifiers_states[amp_key]["intcode"].split(","), 
                                                                   [str(input_)],
                                                                   amplifiers_states[amp_key]["pointer"])

                amplifiers_states[amp_key]["intcode"] = amp
                amplifiers_states[amp_key]["status"] = status
                amplifiers_states[amp_key]["pointer"] = pointer

                input_ = diagnostic.split(",")[0]
                if amp_key == 4 and status == 1:
                    response.append(int(diagnostic))

                    running = False
    print(response)
    return response


if __name__ == "__main__":
    # read Input file
    # test1 = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
    # test2 = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
    # test3 = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"

    # assert max(run(test1.split(","), "0")) == "43210"
    # assert max(run(test2.split(","), "0")) == "54321"
    # assert max(run(test3.split(","), "0")) == "65210"
    
    # with open("input.txt", "r") as input_file:
    #     program = input_file.readline()
    #     program_sequence = program.split(",")
    #     puzzle_sequence = program_sequence
    #     rep = run(puzzle_sequence, "0")
    #     print(max(rep))

    test1  = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
    puzzle_intcode1 = test1.split(",")

    assert str(max(run_bis(puzzle_intcode1, 0))) == "139629729"

    test2  = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
    puzzle_intcode2 = test2.split(",")
    assert str(max(run_bis(puzzle_intcode2, 0))) == "18216"

    with open("input.txt", 'r') as input_puzzle:
        puzzle = input_puzzle.readline()
        puzzle_intcode = puzzle.split(",")
        print(max(run_bis(puzzle_intcode, 0)))