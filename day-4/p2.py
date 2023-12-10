
f = open("./input", "r")
res = 0
cardsList = [1 for _ in range(210)]
for line in f.readlines():
    card, data = line.split(":")
    winning, have = data.split("|")
    winningNumbers = set(winning.split())
    count = 0
    cardNumber = int(card.split()[1])
    for number in have.split():
        if number in winningNumbers:
            count += 1
    if count == 0: continue
    for i in range(cardNumber,cardNumber+count):
        cardsList[i] += cardsList[cardNumber-1]

print(sum(cardsList[:204]))
