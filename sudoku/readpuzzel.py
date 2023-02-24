import math
from os import listdir
from os.path import isfile, join
import calcgui


#
# Files and file manipulation
#
SUDOKUPATHOUT = "/Users/tacobakker/PycharmProjects/sudoku/puzzels/"
SUDOKUPATHIN = "/Users/tacobakker/PycharmProjects/sudoku/input/"


def leesFile(fileName):
    file1 = open(fileName, 'r')
    lines = file1.readlines()
    return lines


def leesFilesAndConvert():
    sudokuinputfiles = [f for f in listdir(SUDOKUPATHIN) if isfile(join(SUDOKUPATHIN, f))]
    for sudokuFile in sudokuinputfiles:
            convertInputToCSV(SUDOKUPATHIN+sudokuFile, SUDOKUPATHOUT + sudokuFile)


def writeRegelsToFile(regels, filename):
    f = open(filename, "w")
    for x in regels:
        f.write(x+"\n")
    f.close()


def convertToMatrix(inhoud):
    matrix = []
    counter = 1
    for regel in inhoud:
        cijfer = ""
        regel = regel.strip()
        teller = 0
        while teller < len(regel):
            if regel[teller] in ["+","-","*","%"]:
                cijfer=cijfer+regel[teller]
                matrix.append([counter, cijfer])
                cijfer = ""
                counter+=1
            elif int(regel[teller]) in range(0,10):
                cijfer=cijfer+regel[teller]
            else:
                print("illegal character found", regel[teller])
            teller+=1
    return matrix


def getMatrixSize(matrix):
    return int(math.sqrt(len(matrix)))



def findNeighbours(nummer, matrixSize):
    #hoekje links boven
    if nummer == 1:
        neighbours = [nummer+1,nummer+matrixSize]
    #hoekje rechts onder
    elif nummer == matrixSize*matrixSize:
        neighbours = [nummer-1,nummer-matrixSize]
    #hoekje links onder
    elif nummer == (matrixSize*matrixSize)-matrixSize+1:
        neighbours = [nummer+1, nummer-matrixSize]
    #hoekje rechts boven
    elif nummer == matrixSize:
        neighbours = [matrixSize-1, 2*matrixSize]
    #kantstukje links
    elif nummer % matrixSize == 1:
        neighbours = [nummer+1,nummer+matrixSize,nummer-matrixSize]
    #kantstukje rechts
    elif nummer % matrixSize == 0:
        neighbours = [nummer-1,nummer+matrixSize,nummer-matrixSize]
    #kantstukje boven
    elif nummer <= matrixSize:
        neighbours = [nummer + 1, nummer - 1, nummer + matrixSize]
    #kantstukje onder
    elif nummer > (matrixSize*matrixSize)-matrixSize:
        neighbours = [nummer + 1, nummer - 1, nummer - matrixSize]
    #middenstukje
    else:
        neighbours = [nummer+1,nummer-1,nummer+matrixSize,nummer-matrixSize]
    neighbours.sort()
    neighbours.insert(0,nummer)
    return neighbours


def getAllNeighbours(matrix, matrixSize):
    result = []
    for x in matrix:
        tmp = findNeighbours(x[0], matrixSize)
        result.append(tmp)
    return result


def findEquals(matrix, neighbours, nummer, operatie, results):
    for x in neighbours[nummer-1]:
        if x != nummer and matrix[x-1][1] == operatie and x not in results:
            results.append(x)
            findEquals(matrix, neighbours, x, operatie, results)
    return results


def getVakjes(maxnum, matrix,neighbours):
    vakjes = []
    for nummer in range(1, maxnum + 1):
        operatie = matrix[nummer - 1][1]
        tmp = findEquals(matrix, neighbours, nummer, operatie, [nummer])
        tmp.sort()
        tmp.insert(0, operatie)
        if not tmp in vakjes:
            vakjes.append(tmp)
    return vakjes


def writeLines(vakjes):
    result = []
    for regel in vakjes:
        tmp =""
        tmp+=regel[0][-1]+","+regel[0][:-1]+","
        for element in regel[1:]:
            tmp+=str(element)+","
        result.append(tmp[:-1])
    return result


def convertInputToCSV(filenamein, filenameout):
    #inhoud = leesFile(filenamein)
    #print("[INFO] ", filenamein, "read!")
    inhoudGui = []
    answer = input("Hoe groot (4/5/6) ")
    if answer == '4':
        inhoudGui = calcgui.getPuzzelGui(4)
    if answer == '5':
        inhoudGui = calcgui.getPuzzelGui(5)
    if answer == '6':
        inhoudGui = calcgui.getPuzzelGui(6)

    if answer in ['4','5','6']:
        matrix = convertToMatrix(inhoudGui)
        print("[INFO] file converted to matrix!")
        matrixSize = getMatrixSize(matrix)
        print("[INFO] matrix size is:", matrixSize)
        maxnum = matrixSize * matrixSize
        print("[INFO] maxnum is:", maxnum)
        neighbours = getAllNeighbours(matrix, matrixSize)
        print("[INFO] made a list of all neighbours in matrix!")
        vakjes = getVakjes(maxnum, matrix, neighbours)
        print("[INFO] determined the calculation blocks in the matrix!")
        result = writeLines(vakjes)
        print("[INFO] converted the calculation blocks to strings!")
        writeRegelsToFile(result, filenameout)
        print("[INFO] wrote the strings to a new file!")




# def main():
#     leesFilesAndConvert()
#
#
# if __name__ == '__main__':
#     main()
