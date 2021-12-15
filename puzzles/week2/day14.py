def p1(polymer, rules):
    for step in range(10):
        temp_str = polymer[0]

        for i in range(len(polymer) - 1):
            temp_str += rules[polymer[i] + polymer[i + 1]]
            temp_str += polymer[i + 1]
        polymer = temp_str

    count_dict = {}
    for char in polymer:
        if char not in count_dict:
            count_dict[char] = 0
        count_dict[char] += 1

    print(count_dict)

    count = list(count_dict.values())
    count.sort()

    return count[-1] - count[0]


def p2(polymer):
    return 0
'''
#-------------------------------------------------------------------------------
# Eigener Lösungsansatz:
# (Sowohl dieser Ansatz, als auch die Verwendung von dem obigen Code aus Part 1
# mit 40 statt 10 steps, sorgen für Probleme, da der Aufwand zu hoch ist und das 
# Programm zu lange zum Beenden braucht)
#-------------------------------------------------------------------------------

   
    global counts_dict
    counts_dict = {}

    for i in range(len(polymer) - 1):
        down(polymer[i] + polymer[i + 1], 20)
    print(counts_dict)

    count = list(counts_dict.values())
    count.sort()

    return (count[-1] - count[0]) / 2


def down(pair, depth):
    depth -= 1
    if depth < 0:
        for char in pair[:2]:
            if char not in counts_dict:
                counts_dict[char] = 0
            counts_dict[char] += 1
        return

    left = pair[:1] + rules[pair]
    right = rules[pair] + pair[1:]

    down(left, depth)
    down(right, depth)
    return
'''


with open('../../input/week2/day14.txt') as file:
    rules = {}
    polymer = file.readline().strip()
    file.readline()
    for line in file.readlines():
        split = line.strip().split(' -> ')
        rules[split[0]] = split[1]
    print(polymer)
    print(rules)

    print('part 1: ' + str(p1(polymer, rules)))
    print('part 2: ' + str(p2(polymer, rules)))
