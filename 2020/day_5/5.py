"""Day 5 advent of code"""
import math

def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().splitlines()))
    return l
    
def find_seat(seat, s):

    if s in ["B", "F"]:
        if s == "B":
            # Back of the plane: Takes the upper half
            seat[0][0] = seat[0][1] - math.floor((seat[0][1] - seat[0][0]) / 2)
            return seat, seat[0][0]
        else:
            # Front of the plane: Takes the lower half
            seat[0][1] = seat[0][0] + math.floor((seat[0][1] - seat[0][0]) / 2)
            return seat, seat[0][1]

    elif s in ["L", "R"]:
        if s == "R":
            # Right of the plane: Takes the upper half
            seat[1][0] = seat[1][1] - math.floor((seat[1][1] - seat[1][0]) / 2)
            return seat, seat[1][0]
            
        else:
            # Left of the plane: Takes the lower half
            seat[1][1] = seat[1][0] + math.floor((seat[1][1] - seat[1][0]) / 2)
            return seat, seat[1][1]

    return seat

def get_boparding_pass_id(x):
    seat = [[0, 127], [0, 7]]
    for i, s in enumerate(x):
        seat, value = find_seat(seat, s)

        if i == 6: 
            row = value

        if i == 9: 
            col = value

    return row * 8 + col

def main():
    X = read_input(str)
    p = [get_boparding_pass_id(x) for x in X]
    p.sort()

    # PART 1 
    print(p[-1])

    # PART 2
    print(set(range(p[0], p[-1])).difference(set(p)))

if __name__=="__main__":
    main()
