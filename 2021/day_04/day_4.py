def parse_board(board):
    return [line.split() for line in board.split("\n")]

def check_rows(list_of_coors):
    list_of_coors.sort(key=lambda x:x[0])
    if len(list_of_coors) > 5:
        dep = list_of_coors[0][0]
        count = 0
        for i in range(len(list_of_coors)):
            if list_of_coors[i][0] == dep:
                count += 1
                if count == 5:
                    return True
            else:
                dep = list_of_coors[i][0]
                count = 1
        
    return False

def check_cols(list_of_coors):
    list_of_coors.sort(key=lambda x:x[1])
    if len(list_of_coors) > 5:
        dep = list_of_coors[0][1]
        count = 0
        for i in range(len(list_of_coors)):
            if list_of_coors[i][1] == dep:
                count += 1
                if count == 5:
                    return True
            else:
                dep = list_of_coors[i][1]
                count = 1
        
    return False

def get_missing_list(list_of_coors):
    list_of_coors.sort(key=lambda x:(x[0], x[1]))
    filtre = []
    for i in range(5):
        for j in range(5):
            filtre.append((i, j))

    return list(set(filtre) - set(list_of_coors))

def main1(input_f):
    input_str = input_f.split("\n\n")
    numbers = list(map(int, input_str[0].split(",")))
    boards = input_str[1:]
    rep = {}
    for n1 in numbers:
        for z in range(len(boards)):
            board = parse_board(boards[z])
            for x in range(len(board)):
                for y in range(len(board[x])):
                    n2 = board[x][y]
                    if int(n1) == int(n2):
                        if z not in rep:
                            rep[z] = [(x,y)]
                        else:
                            rep[z].append((x,y))
            if z in rep: 
                if check_rows(rep[z]) or check_cols(rep[z]):
                    print(sum([int(board[ii][jj]) for ii, jj in get_missing_list(rep[z])]) * int(n1))
                    return

def main2(input_f):
    W = []
    input_str = input_f.split("\n\n")
    numbers = list(map(int, input_str[0].split(",")))
    boards = input_str[1:]
    rep = {}
    for n1 in numbers:
        for z in range(len(boards)):
            board = parse_board(boards[z])
            for x in range(len(board)):
                for y in range(len(board[x])):
                    n2 = board[x][y]
                    if int(n1) == int(n2):
                        if z not in rep:
                            rep[z] = [(x,y)]
                        else:
                            rep[z].append((x,y))
            if z in rep and z not in W: 
                if check_rows(rep[z]) or check_cols(rep[z]):
                    print(sum([int(board[ii][jj]) for ii, jj in get_missing_list(rep[z])]) * int(n1))
                    W.append(z)


# 14,30,18,8,3,10,77,4,48,67,28,38,63,43,62,12,68,88,54,32,17,21,83,64,97,53,24,2,60
# 60 53 43 12  2
# 26 25 49 61 54
# 17 73 75 47 19
#  9 95 67 46 98
# 86  8 35 81 77


if __name__ == "__main__":
    # Test our functions
    TEST = """7,4,9,5,11,17,23,2,0,14,21,3,20,24,10,16,13,6,15,25,12,22,18,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
    # Read input file
    main1("%s" % TEST)
    # main2("%s" % TEST)
    with open("input.txt", "r") as input_file:
        f = input_file.read()
        main1("%s" % f)
        main2("%s" % f)

    input_file.close()