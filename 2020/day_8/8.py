"""Day 8 advent of code"""
import copy

class BootCode:
    """Short Description here"""
    def __init__(self, instructions):
        self.instructions = instructions
        self.acc = 0
        self.visited = []

    def run(self, debug=None):

        infinite_loop = False
        i = 0

        while not infinite_loop and i < len(self.instructions):

            if i not in self.visited:
                self.visited.append(i)
                operation = self.instructions[i][0]
                arg = self.instructions[i][1]

                if debug and i == debug:
                    if operation == "jmp":
                        operation = "nop"
                    elif operation == "nop":
                        operation = "jmp"

                if operation == "nop":
                    i += 1

                elif operation == "jmp":
                    i += arg
                    
                elif operation == "acc":
                    self.acc += arg
                    i += 1
            
            else:
                infinite_loop = True
                return False

        return True


def parse_instructions(instructions):
    lines = []
    for inst in instructions:
        operation = inst.split(" ")[0]
        arg = int(inst.split(" ")[1])
        lines.append((operation, arg))

    return lines


def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().splitlines()))
    return l


if __name__=="__main__":
    X = read_input(str)
    instructions = parse_instructions(X)

    # Part 1
    bc1 = BootCode(instructions)
    bc1.run()
    print(bc1.acc)

    # Part 2
    for i in range(max(bc1.visited), 0, -1):
        bc_loop = BootCode(instructions)
        if bc_loop.run(debug=i):
            print(bc_loop.acc)
            break
