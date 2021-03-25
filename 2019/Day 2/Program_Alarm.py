import os
import copy


def programm_alarm(sequence):
    for index in range(0, len(sequence), 4):
        if sequence[index] == "99":
            break
        if sequence[index] == "1":
            sequence[int(sequence[index + 3])] = str(
                int(sequence[int(sequence[index + 1])])
                + int(sequence[int(sequence[index + 2])])
            )
        elif sequence[index] == "2":
            sequence[int(sequence[index + 3])] = str(
                int(sequence[int(sequence[index + 1])])
                * int(sequence[int(sequence[index + 2])])
            )
        else:
            print("error")
    return ",".join(sequence)


if __name__ == "__main__":
    assert programm_alarm("1,0,0,0,99".split(",")) == "2,0,0,0,99"
    assert programm_alarm("2,3,0,3,99".split(",")) == "2,3,0,6,99"
    assert programm_alarm("2,4,4,5,99,0".split(",")) == "2,4,4,5,99,9801"
    assert programm_alarm("1,1,1,4,99,5,6,0,99".split(",")) == "30,1,1,4,2,5,6,0,99"

    # read Input file
    with open("input.txt", "r") as input_file:

        program = input_file.readline()

        # PART 1
        program_sequence = program.split(",")
        program_sequence[1] = "12"
        program_sequence[2] = "2"

        print(programm_alarm(program_sequence))

        # PART 2
        program_sequence_2 = program.split(",")

        for noun in range(100):
            for verb in range(100):

                sequence_copy = copy.deepcopy(program_sequence_2)

                sequence_copy[1] = str(noun)
                sequence_copy[2] = str(verb)

                compute_memory_0 = programm_alarm(sequence_copy)[:8]

                if compute_memory_0 == "19690720":
                    print(noun, verb)
