# just read the file, line by line
# automatically determine the matrix size
# interpret the CSV lines and create the first 5 columns of the definition of the matrix
# per calculation area, determine a list of possible values that fit that calculation
# add all those possibilities to the matrix definition, and print it on the screen
# Make an empty matrix to start with. We fill it with negative numbers to not disrupt checks
# Recursively check all possible values to find the correct outcome of the calcudoku


import itertools
from functools import reduce
import csv
import math
from os import listdir
from os.path import isfile, join

SUDOKUPATH = "/Users/tacobakker/PycharmProjects/sudoku/puzzels/"


def colored(r, g, b, text):
    return "\033[7m\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def red(text):
    return colored(255,0,0,text)

def green(text):
    return colored(0, 153,0, text)

def blue(text):
    return colored(102, 204, 255, text)

def yellow(text):
    return colored(103, 102, 100, text)

def purple(text):
    return colored(204, 0,204, text)

def darkred(text):
    return colored(204, 0,0, text)

def orange(text):
    return colored(255, 153, 0, text)

def browne(text):
    return colored(153, 102, 51, text)

def rose(text):
    return colored(255, 204, 255, text)

def darkblue(text):
    return colored(0, 0, 255, text)

def oldpink(text):
    return colored(204, 102, 153, text)


def colorprint(tekst, num):
    if num == 0:
        return red(tekst)
    elif num == 1:
        return green(tekst)
    elif num == 2:
        return oldpink(tekst)
    elif num == 3:
        return blue(tekst)
    elif num == 4:
        return darkblue(tekst)
    elif num == 5:
        return purple(tekst)
    elif num == 6:
        return darkred(tekst)
    elif num == 7:
        return orange(tekst)
    elif num == 8:
        return browne(tekst)
    elif num == 9:
        return rose(tekst)
    elif num == 10:
        return yellow(tekst)
    else:
        return "\033[0m"


# a list of any numbers will be multiplied
def multList(lijstje):
        return reduce(lambda x, y: x * y, lijstje)


# a list of any numbers will be added
def addList(lijstje):
        return reduce(lambda x, y: x + y, lijstje)


# a list of any numbers will be substracted
def subList(lijstje):
        res = lijstje[0]
        for x in lijstje[1:]:
                res = res - x
        return res

def divList(lijstje):
        res = lijstje[0]
        for x in lijstje[1:]:
                res = res / x
        return res

# a list of any numbers will be divided
def divList2(lijstje):
        return reduce(lambda x, y: x / y , lijstje )


# all combinations of a list of numbers of a certain length
def findAllCombinations(lenMatrix, lenCalc):
        return [p for p in itertools.product(list(range(1,lenMatrix+1)), repeat=lenCalc)]


# extract all valid combinations that add up to a number
def findValidCombinationsAdd(lenMatrix, lenCalc, antwoord):
        return [x for x in findAllCombinations(lenMatrix, lenCalc) if addList(x) == antwoord]


# extract all valid combinations that substract to a number
def findValidCombinationsMult(lenMatrix, lenCalc, antwoord):
        return [x for x in findAllCombinations(lenMatrix, lenCalc) if multList(x) == antwoord]


# extract all valid combinations that multiply up to a number
def findValidCombinationsSub(lenMatrix, lenCalc, antwoord):
        return [x for x in findAllCombinations(lenMatrix, lenCalc) if abs(subList(x)) == antwoord]


# extract all valid combinations that divide to a number
def findValidCombinationsDiv(lenMatrix, lenCalc, antwoord):
        return [x for x in findAllCombinations(lenMatrix, lenCalc) if divList(list([x[0],x[1]])) == antwoord or divList(list([x[1],x[0]]))]


def findValidCombinations(lenMatrix, lenCalc, antwoord, calcType):
        res = []
        if calcType == "+":
                res = findValidCombinationsAdd(lenMatrix, lenCalc, antwoord)
        elif calcType == "*":
                res = findValidCombinationsMult(lenMatrix, lenCalc, antwoord)
        elif calcType == "-":
                res = findValidCombinationsSub(lenMatrix, lenCalc, antwoord)
        elif calcType == "%":
                res = findValidCombinationsDiv(lenMatrix, lenCalc, antwoord)
        else:
                print("invalid calculation value")
        return res


def makeVerticalList(sudokuMatrix, matrixSize):
        res = []
        for x in range(matrixSize):
                tmp = []
                for y in range(matrixSize):
                        tmp.append(sudokuMatrix[y][x])
                res.append(tmp)
        return res


def checkValidityOfMatrix(sudokuMatrix, matrixSize):
        result = True
        vert = makeVerticalList(sudokuMatrix, matrixSize)
        for x in range(matrixSize):
                if len(list(set(sudokuMatrix[x]))) < matrixSize:
                        result = False
                if len(list(set(vert[x]))) < matrixSize:
                        result = False
        return result


def checkCalculations(matrix, matrixDef, matrixSize):
        oordeel = True
        teller = 0
        printRegels = []
        while teller < len(matrixDef):
                result = 0
                calcType = matrixDef[teller][1]
                uitkomst = matrixDef[teller][2]
                regel = ""

                if calcType == "+":
                        for x in matrixDef[teller][3]:
                                num1 = matrix[x[0]][x[1]]
                                result += num1
                                regel += str(num1) + " + "
                        regel = regel[0:-3]
                elif calcType == "*":
                        result=1
                        for x in matrixDef[teller][3]:
                                num1 = matrix[x[0]][x[1]]
                                result *= num1
                                regel += str(num1) + " * "
                        regel = regel[0:-3]

                elif calcType == "-":
                        num1 = matrix[matrixDef[teller][3][0][0]][matrixDef[teller][3][0][1]]
                        num2 = matrix[matrixDef[teller][3][1][0]][matrixDef[teller][3][1][1]]
                        result = abs(num1 - num2)
                        regel = str(num1) + " - " + str(num2)
                elif calcType == "%":
                        num1 = matrix[matrixDef[teller][3][0][0]][matrixDef[teller][3][0][1]]
                        num2 = matrix[matrixDef[teller][3][1][0]][matrixDef[teller][3][1][1]]
                        regel = str(num1) + " % " + str(num2)
                        if num1 / num2 == uitkomst:
                                result = num1 / num2
                        else:
                                result = num2 / num1
                else:
                        print("invalid calculation value")

                if result == uitkomst:
                        printRegels.append(["ok: "+regel+" = "+ str(result)])
                else:
                        printRegels.append(["nok", regel, " = ", result, " moet zijn: ", uitkomst])
                        oordeel = False
                teller += 1
        if oordeel:
                print("Ik ga de uitkomst controleren:")
                print()
                for x in printRegels:
                        print(''.join(x))
                print()
        return oordeel


def tryMatrixChange(waardes, sukDef, suk):
        if len(waardes) == len(sukDef):
                count = 0
                for x in sukDef:
                        suk[x[0]][x[1]] = waardes[count]
                        count+=1
        else:
                print("invalid values entered for change")
                print(waardes)
                print(sukDef)
        return suk


def createAllPossibilities(matrixSize, matrixDefinition):
        possibilities = []
        for x in matrixDefinition:
                possibilities.append((findValidCombinations(matrixSize, len(x[3]), x[2], x[1])))
        return possibilities


def addPossibilities(possibilities, matrixDefinition):
        res = []
        teller = 0
        while teller < len(possibilities):
                matrixDefinition[teller].append(possibilities[teller])
                res.append(matrixDefinition[teller])
                teller+=1
        return res


def makeInitialMatrix(matrixSize, defMatrix):
        matrix = [[0 for i in range(matrixSize)] for j in range(matrixSize)]
        for a in defMatrix:
                matrix = tryMatrixChange(a[4], a[3], matrix)
        return matrix


def sudoku(suk, matrix, teller, matrixSize):
        if teller < len(matrix):
                tmp = 0
                for x in matrix[teller][5]:
                        suk = tryMatrixChange(x, matrix[teller][3], suk)
                        if checkValidityOfMatrix(suk, matrixSize):
                                sudoku(suk, matrix, teller + 1, matrixSize)
                        tmp+=1
                suk = tryMatrixChange(matrix[teller][4], matrix[teller][3], suk)
        else:
                if checkValidityOfMatrix(suk, matrixSize):
                        if checkCalculations(suk, matrix, matrixSize):
                                print("success! De uitkomst van de puzzel is:")
                                print()
                                #printMatrix6(suk, matrixSize)
                                printMatrixColor(suk, matrixSize, makeMatrixColor(matrix, matrixSize))
                else:
                        print("failure")


def printMatrixDef(matrix, matrixSize):
        print("Dit is de puzzel zoals ik die heb ingevoerd!")
        print()
        tmp = [[0 for i in range(matrixSize)] for j in range(matrixSize)]
        for x in matrix:
                for y in x[3]:
                        a = int(y[0])
                        b = int(y[1])
                        format_x2 = "{:4d}".format(x[2])
                        tmp[a][b] = str(int(x[0]))+str(format_x2)+x[1]
        for w in tmp:
                for q in w:
                        num = int(q[0:2])
                        print(colorprint(str(q[2:]).rjust(5, " "), num), end="")
                print(colorprint("",300))
        print()


def makeMatrixColor(matrix, matrixSize):
        res = [[0 for i in range(matrixSize)] for j in range(matrixSize)]
        for x in matrix:
                for y in x[3]:
                        res[int(y[0])][int(y[1])] = x[0]
        return res


def printMatrixColor(matrix, matrixSize, matrixColor):
        telhor = 0
        telver = 0
        for x in matrix:
                for y in x:
                        print(colorprint(str(y).rjust(2," "), matrixColor[telhor][telver]), end="")
                        telver+=1
                telver=0
                telhor+=1
                print()
        print(colorprint("", 300))


def realTrueDiv(x, y):
        teller = 0
        while x > y:
                x = x - y
                teller+=1
        return(teller)


def getCoordinates(num, matrixSize):
        return [realTrueDiv(num,matrixSize), ((num-1)%matrixSize)]


def makeDummyValues(teller, aantal):
        return [-x-1+teller*-10 for x in range(aantal) ]


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


def makeMatrixDefinition(matrixcsv):
        teller = 0
        result = []
        matrixSize = int(math.sqrt(sum([len(x) for x in matrixcsv]) - 2 * (len(matrixcsv))))
        for x in matrixcsv:
                coordinaten = [getCoordinates(int(y), matrixSize) for y in x[2:]]
                result.append([teller, x[0], int(x[1]),coordinaten, makeDummyValues(teller,len(coordinaten))])
                teller+=1
        return result


def leesCSV(matrixFileName):
        with open(matrixFileName) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                vlakkies = []
                for row in csv_reader:
                        vlakkies.append(row)
        return vlakkies


def findSudokuSolution(matrixCSV):
        if checkInputCSV(matrixCSV):
                matrixSize = int(math.sqrt(sum([len(x) for x in matrixCSV]) - 2 * (len(matrixCSV))))
                matrixInitialDefinition = makeMatrixDefinition(matrixCSV)
                ListOfAllPossibilities = createAllPossibilities(matrixSize, matrixInitialDefinition)
                matrixComplete = addPossibilities(ListOfAllPossibilities, matrixInitialDefinition)
                printMatrixDef(matrixComplete, matrixSize)
                emptyMatrix = makeInitialMatrix(matrixSize, matrixComplete)
                sudoku(emptyMatrix, matrixComplete, 0, matrixSize)


def leesFilesenCalculate():
        sudokufiles = [f for f in listdir(SUDOKUPATH) if isfile(join(SUDOKUPATH, f))]
        for sudokuFile in sudokufiles:
                findSudokuSolution(leesCSV(SUDOKUPATH + sudokuFile))


def main():
        leesFilesenCalculate()


if __name__ == '__main__':
        main()
