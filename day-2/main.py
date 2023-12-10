
def part1():
    def parseGame(gameNum, sets):
        for set in sets.split(";"):
            for color in set.split(","):
                num, c = color.split()
                if "red" in c:
                    if int(num) > 12:
                        return 0
                elif "green" in c:
                    if int(num) > 13:
                        return 0
                elif "blue" in c:
                    if int(num) > 14:
                        return 0
        return gameNum

    f = open("./input", "r")
    res = 0
    for line in f.readlines():
        game, sets = line.split(":")
        gameNumber = int(game.split()[1])
        res += parseGame(gameNumber, sets)
    print(res)


def part2():
    def parseGame(gameNum, sets):
        minColors = dict()
        minColors["red"] = 0
        minColors["green"] = 0
        minColors["blue"] = 0
        for set in sets.split(";"):
            for vals in set.split(","):
                num, color = vals.split()
                minColors[color] = max(minColors[color], int(num))
        return minColors["red"] * minColors["green"] * minColors["blue"]

    f = open("./input", "r")
    res = 0
    for line in f.readlines():
        game, sets = line.split(":")
        gameNumber = int(game.split()[1])
        res += parseGame(gameNumber, sets)
    print(res)


part1()
part2()

