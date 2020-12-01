"""Day 1 advent of code"""
if __name__=="__main__":
    # Read input file
    with open("input.txt", "r") as f:
        exp_report = list(map(int, f.read().splitlines()))
        n = len(list(exp_report))
        for i in range(n):
            for j in range(i+1, n):
                for k in range(i+2, n):
                    if exp_report[i] + exp_report[j] + exp_report[k] == 2020:
                        print(exp_report[i] * exp_report[j] * exp_report[k])
                        break
