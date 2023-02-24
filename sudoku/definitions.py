import colors
import math
import combinations
import csv


def getCoordinates(num, matrixSize):
    return [combinations.realTrueDiv(num, matrixSize), ((num - 1) % matrixSize)]


def makeDummyValues(teller, aantal):
    return [-x - 1 + teller * -10 for x in range(aantal)]


def checkInputCSV(matrixcsv):
    res = []
    for x in matrixcsv:
        for y in x[2:]:
            res.append(int(y))
    res.sort()
    if len(res) == 16 or len(res) == 25 or len(res) == 36:
        if len(list(set(res))) < len(res):
            print("too few items, or duplicates", res)
            return False
    else:
        print("too many or too few items", res)
        return False
    return True


def printMatrixDef(matrix, matrixSize):
    print("Dit is de puzzel zoals ik die heb ingevoerd!")
    print()
    tmp = [[0 for i in range(matrixSize)] for j in range(matrixSize)]
    for x in matrix:
        for y in x[3]:
            a = int(y[0])
            b = int(y[1])
            format_x2 = "{:4d}".format(x[2])
            tmp[a][b] = str(int(x[0]) ) +str(format_x2 ) +x[1]
    for w in tmp:
        for q in w:
            num = int(q[0:2])
            print(colors.colorprint(str(q[2:]).rjust(5, " "), num), end="")
        print(colors.colorprint("", 300))
    print()


def makeMatrixDefinition(matrixcsv):
    teller = 0
    result = []
    matrixSize = int(math.sqrt(sum([len(x) for x in matrixcsv]) - 2 * (len(matrixcsv))))
    for x in matrixcsv:
        coordinaten = [getCoordinates(int(y), matrixSize) for y in x[2:]]
        result.append([teller, x[0], int(x[1]), coordinaten, makeDummyValues(teller, len(coordinaten))])
        teller += 1
    return result


def leesCSV(matrixFileName):
    with open(matrixFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        vlakkies = []
        for row in csv_reader:
            vlakkies.append(row)

    return vlakkies

