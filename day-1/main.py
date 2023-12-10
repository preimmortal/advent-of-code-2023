from collections import defaultdict

if __name__ == "__main__":
    def part1():
        res = 0
        f = open("./input", "r")
        for line in f.readlines():
            first = last = -1
            for c in line:
                if c.isdigit():
                    last = int(c)
                    if first == -1: first = int(c)
            res += first*10+last
        print(res)

    def part2():
        numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        res = 0
        f = open("./input", "r")
        for line in f.readlines():
            first = last = -1
            for i,c in enumerate(line):
                if c.isdigit():
                    last = int(c)
                    first = int(c) if first == -1 else first
                else:
                    for n,number in enumerate(numbers):
                        if line[i] != number[0]: continue
                        if line[i:i+len(number)] == number: 
                            last = n+1
                            first = n+1 if first == -1 else first
            res += first*10 + last
        print(res)

    part1()
    part2()
