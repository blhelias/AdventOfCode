def main1(input_f):
    input_str = input_f.split("\n")
    g = ""
    e = ""
    for i in range(len(input_str[0])):
        r = [input_str[x][i] for x in range(len(input_str))]

        g += max(set(r), key=r.count)
        e += min(set(r), key=r.count)

    print(int(g, 2) * int(e, 2))


def main2(input_f):
    input_str = input_f.split("\n")
    temp_list_g = input_str[:]
    temp_list_e = input_str[:]

    for i in range(len(input_str[0])):
        rg = [int(temp_list_g[x][i]) for x in range(len(temp_list_g))]
        re = [int(temp_list_e[x][i]) for x in range(len(temp_list_e))]

        countg = sum(rg)
        counte = sum(re)

        g = "1" if countg >= len(temp_list_g) / 2 else "0"
        e = "1" if counte < len(temp_list_e) / 2 else "0"

        temp_list_g = [x for x in temp_list_g if x[i] == g]
        temp_list_e = [x for x in temp_list_e if x[i] == e]
        
        if len(temp_list_g) == 1:
            rep_g = int(temp_list_g[0], 2)

        if len(temp_list_e) == 1:
            rep_e = int(temp_list_e[0], 2)

    print(rep_e * rep_g)


if __name__ == "__main__":
    # Test our functions
    TEST = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    # Read input file
    main1("%s" % TEST)
    main2("%s" % TEST)
    with open("input.txt", "r") as input_file:
        f = input_file.read()
        main1("%s" % f)
        main2("%s" % f)

    input_file.close()