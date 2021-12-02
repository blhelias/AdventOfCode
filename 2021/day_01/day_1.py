# hello
def main1(input_str):
    input_str = input_str.split("\n")
    prev = None
    c = 0
    for i in range(len(input_str) - 1):

        el = input_str[i]
        if prev:
            if int(prev) - int(el) < 0:
                c += 1
        prev = input_str[i]

    print(c)

def main2(input_str):
    input_str = input_str.split("\n")
    prev = None
    c = 0
    for i in range(len(input_str) - 3):
        el = sum(int(input_str[j+i]) for j in range(3))
        if prev:
            if int(prev) - int(el) < 0:
                c += 1
        prev = el

    print(c)



if __name__ == "__main__":
    # Test our functions
    TEST = """199
200
208
210
200
207
240
269
260
263"""
    # Read input file
    # main(TEST)
    with open("input.txt", "r") as input_file:
        main1(input_file.read())
        main2(input_file.read())

    input_file.close()
