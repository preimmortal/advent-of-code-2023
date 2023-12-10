
f = open("./input", "r")
res = 0
for line in f.readlines():
    cardNumber, data = line.split(":")
    winning, have = data.split("|")
    winningNumbers = set(winning.split())
    count = 0
    for number in have.split():
        if number in winningNumbers:
            count += 1
    res += 1 << (count-1) if count > 0 else 0
print(res)
