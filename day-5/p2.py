from collections import defaultdict

seedToSoil = "seed-to-soil"
soilToFertilizer = "soil-to-fertilizer"
fertilizerToWater = "fertilizer-to-water"
waterToLight = "water-to-light"
lightToTemperature = "light-to-temperature"
temperatureToHumidity = "temperature-to-humidity"
humidityToLocation = "humidity-to-location"

class Seed:
    def __init__(self, id):
        self.id = id
        self.attributes = defaultdict(lambda: id)

    def setAttribute(self, attribute, id):
        self.attributes[attribute] = id

    def getAttribute(self, attribute):
        return self.attributes[attribute]
    
    def findAttributes(self, fields):
        self.attributes["soil"] = fields.getField(seedToSoil, self.id)
        self.attributes["fertilizer"] = fields.getField(soilToFertilizer, self.attributes["soil"])
        self.attributes["water"] = fields.getField(fertilizerToWater, self.attributes["fertilizer"])
        self.attributes["light"] = fields.getField(waterToLight, self.attributes["water"])
        self.attributes["temperature"] = fields.getField(lightToTemperature, self.attributes["light"])
        self.attributes["humidity"] = fields.getField(temperatureToHumidity, self.attributes["temperature"])
        self.attributes["location"] = fields.getField(humidityToLocation, self.attributes["humidity"])

class Fields:
    def __init__(self):
        self.fields = defaultdict(list)

    def setField(self, field, d, s, r):
        self.fields[field].append((s,d,r))

    def getField(self, field, id):
        for s,d,r in self.fields[field]:
            if id >= s and id < s+r: return id + (d-s)
        return id

# Parse the File
f = open("input", "r")

# Read the Header
header = f.readline().split()[1:]
seeds = []
start = 0

# Read the Fields
field = "seeds"

fields = Fields()

for line in f.readlines():
    line = line.rstrip("\n")
    if line == "": continue
    if ":" in line:
        field = line.rstrip(" map:")
        continue
    d,s,r = line.split()
    fields.setField(field, int(d), int(s), int(r))

#res = float("inf")
res = 0
seeds = []
for i,val in enumerate(header):
    if i%2 == 0: start = int(val)
    else:
        seeds.append((start,start+int(val)))
    #    for j in range(int(val)):
    #        seed = Seed(start+j)
    #        seed.findAttributes(fields)
    #        res = min(res, seed.getAttribute("location"))
print(sorted(seeds))

print(res)


