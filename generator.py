from random import shuffle

print("Skriv in paren här: ")

pairs = input().split()

n = len(pairs)

pairList = [x for x in range(n)]
shuffle(pairList)

pairGrid = []

firstCourse = []
secondCourse = []
thirdCourse = []

for x in range(0, len(pairList), int(n/3)):
    pairGrid.append(pairList[x:x+int(n/3)])

def offsetList(list, steps):
    newList = [x for x in list]
    for x in range(steps):
        newList.insert(0, newList.pop())
    return newList

def numberToPair(number):
    return pairs[number]

def hostOrder(course):
    if course == "firstCourse":
        return pairGrid[0]
    elif course == "secondCourse":
        return offsetList(pairGrid[1], int(n/3)-1)
    else:
        return pairGrid[2]

for x in range(int(n/3)):
    list = [pairGrid[y][x] for y in range(3)]
    firstCourse.append(list)

pairGrid[1] = offsetList(pairGrid[1], 1)
pairGrid[2] = offsetList(pairGrid[2], 2)

for x in range(int(n/3)):
    list = [pairGrid[y][x] for y in range(3)]
    secondCourse.append(list)

pairGrid[1] = offsetList(pairGrid[1], 1)
pairGrid[2] = offsetList(pairGrid[2], int(n/3)-1)

for x in range(int(n/3)):
    list = [pairGrid[y][x] for y in range(3)]
    thirdCourse.append(list)

print("\nFörrätt:\n")

order = hostOrder("firstCourse")

for x in range(len(firstCourse)):
    line = "Hos " + str(numberToPair(order[x])) + ": "
    for y in range(3):
        line += numberToPair(firstCourse[x][y]) + " "
    print(line)

print("\nHuvudrätt:\n")

order = hostOrder("secondCourse")

for x in range(len(secondCourse)):
    line = "Hos " + str(numberToPair(order[x])) + ": "
    for y in range(3):
        line += numberToPair(secondCourse[x][y]) + " "
    print(line)

print("\nEfterrätt:\n")

order = hostOrder("thirdCourse")

for x in range(len(thirdCourse)):
    line = "Hos " + str(numberToPair(order[x])) + ": "
    for y in range(3):
        line += numberToPair(thirdCourse[x][y]) + " "
    print(line)

print("\n")
