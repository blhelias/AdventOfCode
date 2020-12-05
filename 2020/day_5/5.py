"""Day 5 advent of code"""
import math

def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().splitlines()))
    return l
    
def update_seat(seat, s):

    if s in ["B", "F"]:

        if s == "B":
            # Takes the upper half
            seat[0][0] = seat[0][1] - math.floor((seat[0][1] - seat[0][0]) / 2)
            return seat, seat[0][0]
        else:
            # Takes the lower half
            seat[0][1] = seat[0][0] + math.floor((seat[0][1] - seat[0][0]) / 2)
            return seat, seat[0][1]

    elif s in ["L", "R"]:
        if s == "R":
            # Takes the upper half
            seat[1][0] = seat[1][1] - math.floor((seat[1][1] - seat[1][0]) / 2)
            return seat, seat[1][0]
            
        else:
            # Takes the lower half
            seat[1][1] = seat[1][0] + math.floor((seat[1][1] - seat[1][0]) / 2)
            return seat, seat[1][1]

    return seat

def get_boparding_pass_id(x):
    seat = [[0, 127], [0, 7]]
    for i, s in enumerate(x):
        seat, value = update_seat(seat, s)

        if i == 6: 
            row = value

        if i == 9: 
            col = value

    return row * 8 + col

def main():
    X = read_input(str)
    p1 = [get_boparding_pass_id(x) for x in X]

    # PART 1 
    print(max(p1))

    # PART 2
    p1.sort()
    a = set(p1)
    b = set(range(p1[0], p1[-1]))
    print(b.difference(a))

if __name__=="__main__":
    main()
