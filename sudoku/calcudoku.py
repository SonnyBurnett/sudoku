# just read the file, line by line
# automatically determine the matrix size
# interpret the CSV lines and create the first 5 columns of the definition of the matrix
# per calculation area, determine a list of possible values that fit that calculation
# add all those possibilities to the matrix definition, and print it on the screen
# Make an empty matrix to start with. We fill it with negative numbers to not disrupt checks
# Recursively check all possible values to find the correct outcome of the calcudoku

import math
import time
from os import listdir
from os.path import isfile, join
import definitions, colors, combinations
import readpuzzel, checkmatrix

SUDOKUPATH = "/Users/tacobakker/PycharmProjects/sudoku/puzzels/"


def rotatematrix(sudokuMatrix):
        return [list(reversed(col)) for col in zip(*sudokuMatrix)]


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
                possibilities.append((combinations.findValidCombinations(matrixSize, len(x[3]), x[2], x[1])))
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
        gelukt = False
        if teller < len(matrix):
                tmp = 0
                for x in matrix[teller][5]:
                        suk = tryMatrixChange(x, matrix[teller][3], suk)
                        if checkValidityOfMatrix(suk, matrixSize):
                                gelukt = sudoku(suk, matrix, teller + 1, matrixSize)
                        tmp+=1
                        if gelukt:
                                break
                suk = tryMatrixChange(matrix[teller][4], matrix[teller][3], suk)
        else:
                if checkValidityOfMatrix(suk, matrixSize):
                        if checkCalculations(suk, matrix, matrixSize):
                                print("success! De uitkomst van de puzzel is:")
                                print()
                                #printMatrix6(suk, matrixSize)
                                printMatrixColor(suk, matrixSize, makeMatrixColor(matrix, matrixSize))
                                gelukt = True
                else:
                        print("failure")
        return gelukt





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
                        print(colors.colorprint(str(y).rjust(2, " "), matrixColor[telhor][telver]), end="")
                        telver+=1
                telver=0
                telhor+=1
                print()
        print(colors.colorprint("", 300))


def findSudokuSolution(matrixCSV):
        if definitions.checkInputCSV(matrixCSV):
                matrixSize = int(math.sqrt(sum([len(x) for x in matrixCSV]) - 2 * (len(matrixCSV))))
                matrixInitialDefinition = definitions.makeMatrixDefinition(matrixCSV)
                ListOfAllPossibilities = createAllPossibilities(matrixSize, matrixInitialDefinition)
                matrixComplete = addPossibilities(ListOfAllPossibilities, matrixInitialDefinition)
                definitions.printMatrixDef(matrixComplete, matrixSize)
                emptyMatrix = makeInitialMatrix(matrixSize, matrixComplete)
                sudoku(emptyMatrix, matrixComplete, 0, matrixSize)


def leesFilesenCalculate():
        sudokufiles = [f for f in listdir(SUDOKUPATH) if isfile(join(SUDOKUPATH, f))]
        for sudokuFile in sudokufiles:
                findSudokuSolution(definitions.leesCSV(SUDOKUPATH + sudokuFile))


def main():
        answer = input("Wil je een nieuwe puzzel invoeren? (J/N) ")
        if answer == 'J' or answer == 'j' or answer == 'Y' or answer == 'y':
                readpuzzel.leesFilesAndConvert()
        checkmatrix.schowtheinput()
        start = time.time()
        leesFilesenCalculate()
        print("Ik deed er: ", round(time.time() - start, 2), "seconden over.")


if __name__ == '__main__':
        main()
