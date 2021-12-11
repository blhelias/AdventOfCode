def main1(input_f):
    SIZE = 10
    rep = [[0 for i in range(SIZE)] for j in range(SIZE)]
    for cloud in input_f.split("\n"):
        start = list(map(int, cloud.split(" -> ")[0].split(",")))
        end = list(map(int, cloud.split(" -> ")[1].split(",")))

        if start[0] == end[0] and start[1] == end[1]:
            rep[start[0]][start[1]] += 1
        
        elif start[0] == end[0]:
            if start[1] < end[1]:
                inc = 1
            else:
                inc = -1
            for i in range(start[1], end[1] + inc, inc):
                rep[start[0]][i] += 1

        elif start[1] == end[1]:
            if start[0] < end[0]:
                inc = 1
            else:
                inc = -1
            for i in range(start[0], end[0] + inc, inc):
                rep[i][start[1]] += 1

    count = 0
    for x in range(len(rep)):
        for y in range(len(rep[0])):
            if rep[x][y] > 1:
                count += 1
    
    print(count)





def main2(input_f):
    SIZE = 1000
    rep = [[0 for i in range(SIZE)] for j in range(SIZE)]
    for cloud in input_f.split("\n"):
        start = list(map(int, cloud.split(" -> ")[0].split(",")))
        end = list(map(int, cloud.split(" -> ")[1].split(",")))



        if start[0] == end[0] and start[1] == end[1]:
            rep[start[0]][start[1]] += 1
        
        elif start[0] == end[0]:
            if start[1] < end[1]:
                inc = 1
            else:
                inc = -1
            for i in range(start[1], end[1] + inc, inc):
                rep[start[0]][i] += 1

        elif start[1] == end[1]:
            if start[0] < end[0]:
                inc = 1
            else:
                inc = -1
            for i in range(start[0], end[0] + inc, inc):
                rep[i][start[1]] += 1

        elif abs(start[0] - end[0]) == abs(start[1] - end[1]):
            if start[0] < end[0]:
                inc = 1
            else:
                inc = -1
            a = (end[1] - start[1])/(end[0] - start[0])
            b = start[1] - (start[0] * a)
            for x in range(start[0], end[0] + inc, inc):
                y = int(a * x + b)
                rep[x][y] += 1
            

    count = 0

    for x in range(len(rep)):
        for y in range(len(rep[0])):
            if rep[x][y] > 1:
                count += 1
    
    print(count)

if __name__ == "__main__":
    # Test our functions
    TEST = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
    # Read input file
    # main1("%s" % TEST)
    # main2("%s" % TEST)
    with open("input.txt", "r") as input_file:
        f = input_file.read()
        # main1("%s" % f)
        main2("%s" % f)

    input_file.close()