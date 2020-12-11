"""Day 4 advent of code"""

PASSPORT = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
NORTH = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().split("\n\n")))
    return l

def check_passport_values(keys, values):

    for k, v in zip(keys, values):

        if k == "byr":
            if len(v) != 4 or not v.isnumeric():
                return False
            v = int(v)
            if v < 1920 or v > 2002:
                return False
            
        elif k == "iyr":
            if len(v) != 4 or not v.isnumeric():
                return False
            v = int(v)
            if v < 2010 or v > 2020:
                return False

        elif k == "eyr":
            if len(v) != 4 or not v.isnumeric():
                return False
            v = int(v)
            if v < 2020 or v > 2030:
                return False

        elif k == "hgt":
            if not "cm" in v and not "in" in v:
                return False
            if "cm" in v:
                h = int(v.split("cm")[0])
                if h < 150 or h > 193:
                    return False
            elif "in" in v:
                h = int(v.split("in")[0])
                if h < 59 or h > 76:
                    return False
                
        elif k == "hcl":
            if len(v) != 7 or v[0] != "#" or "#" in v[1:]:
                return False

        elif k == "ecl":
            if v not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False

        elif k == "pid":
            if len(v) != 9 or not v.isnumeric():
                return False

    return True

def main():
    X = read_input(str)
    X[len(X) -1] = X[len(X) -1][:-1]
    p = 0
    for x in X:
        d = x.replace('\n', ' ').split(" ")
        keys = [f.split(":")[0] for f in d if f.split(":")[0]]
        values = [f.split(":")[1] for f in d if f.split(":")[1]]
            
        if set(keys) == PASSPORT or set(keys) == NORTH:
            if check_passport_values(keys, values):
                p += 1

    print(p)


if __name__=="__main__":
    main()
