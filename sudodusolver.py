import itertools

SUDOKUPATHOUT = "/Users/tacobakker/PycharmProjects/sudoku/sudoku/"
SUDOKUPATHIN = "/Users/tacobakker/PycharmProjects/sudoku/sudoku/"


# Return x div y without the remainder
def realTrueDiv(x, y):
    teller = 0
    while x >= y:
        x = x - y
        teller += 1
    return (teller)


#Create an empty matrix with all zero's
def makeEmptyMatrix(matrixSize):
    return [[0 for i in range(matrixSize)] for j in range(matrixSize)]


# Count all zero's in the sudoku matrix
def countZerosInMatrix(sudoku):
    result = 0
    for x in sudoku:
        for y in x:
            if y == 0:
                result+=1
    return result


# nicely print the sudoku matrix
def printSudoku(sudoku):
    for x in sudoku:
        print(x)
    print()


def leesFile(fileName):
    file1 = open(fileName, 'r')
    lines = file1.readlines()
    return lines


def createQuadsFromFile(filename):
    sudoku = []
    matrixinput = leesFile(SUDOKUPATHIN+filename)
    teller = 1
    while teller <= 9:
        tmp = []
        horizontal = 0
        vertical = 0
        for x in matrixinput:
            for y in x.strip():
                if int(y) == teller:
                    tmp.append([horizontal, vertical])
                vertical += 1
            vertical = 0
            horizontal += 1
        sudoku.append(tmp)
        teller += 1
    return sudoku


def createStandardQuads():
    result = []
    hor = 0
    ver = 0
    while hor < 9:
        while ver < 9:
            tmp = []
            for telhor in range(0, 3):
                for telver in range(0, 3):
                    tmp.append([hor + telhor, ver + telver])
            result.append(tmp)
            ver += 3
        hor += 3
        ver = 0
    return result



# Read the values from the inputfile and put them in de sudoku-matrix
# This is our starting point
def createMatrixFromFileinput(sudoku, matrixinput):
    horizontal = 0
    vertical = 0
    for x in matrixinput:
        for y in x.strip():
            sudoku[horizontal][vertical] = int(y)
            vertical += 1
        vertical = 0
        horizontal += 1
    return sudoku


# Extract 1 horizontal row from the sudoku matrix
def makeHorizontalLine(nummer, sudoku):
    return [x for x in sudoku[nummer-1]]


# Extract 1 vertical line from the sudoku matrix, and make a row of it
def makeVerticalLine(nummer, sudoku):
    result = []
    for x in range(9):
        result.append(sudoku[x][nummer-1])
    return result


# Extract 1 quadrant from the sudoku matrix, and make a row of it
def makeQuadrantList2222(hor, ver, sudoku):
    h = realTrueDiv(hor, 3)
    v = realTrueDiv(ver, 3)
    result = []
    for x in range(0,9):
        for y in range(0,9):
            if realTrueDiv(x, 3) == h and realTrueDiv(y, 3) == v:
                result.append(sudoku[x][y])
    return result


# Extract 1 quadrant from the sudoku matrix, and make a row of it
def makeQuadrantList(hor, ver, sudoku, qf):
    result = []
    teller = 0
    rij = 0
    while teller < len(qf):
        if [hor,ver] in qf[teller]:
            rij = teller
        teller+=1
    for x in qf[rij]:
        a = int(x[0])
        b = int(x[1])
        c = sudoku[a][b]
        result.append(c)
    return result

# Extract cross rowleft to right
def makeCrossRowLeftToRight(sudoku):
    result = []
    rij = 8
    kolom = 0
    for x in range(9):
        result.append(sudoku[rij][kolom])
        rij-=1
        kolom+=1
    return result


# Extract cross rowleft to right
def makeCrossRowRightToLeft(sudoku):
    result = []
    rij = 0
    kolom = 8
    for x in range(9):
        result.append(sudoku[rij][kolom])
        rij+=1
        kolom-=1
    return result


# Merge 3 lists, and remove duplicate values
def makeOneListToRuleThemAll(hor,ver,quad):
    return list(set(itertools.chain(hor,ver,quad)))

def makeOneListToRuleThemAller(h,v,q,c1,c2):
    return list(set(itertools.chain(h,v,q,c1,c2)))

def makeOneListToRuleHV(hor,ver):
    return list(set(itertools.chain(hor,ver)))

# Make a list of values that are not in a list
def findValuesNotInList(lijstje):
    return [x for x in range(1,10) if x not in lijstje]


# *************************** Last Value Left ****************************************************


# Try for this coordinate if the horizontal, vertical, or quadrant row leaves one option
# optie 1 = hor + ver + quadr standard
# optie 2 = hor + ver + quadr from file
# optie 3 = hor + ver + quadr standard + cross
def seekIfForThisCoordinateOnlyOneValueExists(sudoku, hor, vert, optie):
    result = 0
    h1 = v1 = q1 = l1 = []
    h = makeHorizontalLine(hor + 1, sudoku)
    v = makeVerticalLine(vert + 1, sudoku)
    h1 = findValuesNotInList(h)
    v1 = findValuesNotInList(v)

    if optie == 2:
        qf = createQuadsFromFile("combi.txt")
    else:
        qf = createStandardQuads()

    q = makeQuadrantList(hor, vert, sudoku, qf)
    q1 = findValuesNotInList(q)

    clr = makeCrossRowLeftToRight(sudoku)
    c1 = findValuesNotInList(clr)
    crl = makeCrossRowRightToLeft(sudoku)
    c2 = findValuesNotInList(crl)

    if optie == 3:
        l1 = findValuesNotInList(makeOneListToRuleThemAller(h, v, q, c1, c2))
    else:
        l1 = findValuesNotInList(makeOneListToRuleThemAll(h, v, q))
    if len(h1) == 1:
        result = h1[0]
        print("SUCCESS HOR regel ", hor+1, "waarden", h, "nog over", h1)
    elif len(v1) == 1:
        result = v1[0]
        print("SUCCESS VER regel ", vert+1, "waarden", v, "nog over", v1)
    elif len(q1) == 1:
        result = q1[0]
        print("SUCCESS QUAD regel ", "waarden", q, "nog over", q1)
    elif len(l1) == 1:
        result = l1[0]
        print("SUCCESS ALLES regel nog over", l1)
    return result


# Loop through sudoku matrix
# for every zero value, check if we can determine the value
# by checking horizontally, vertically and square if one value is left.
def findLastValues(sudoku, optie, up, sudoku1):
    horizontal = 0
    vertical = 0
    while horizontal <= 8:
        while vertical <= 8:
            if sudoku[horizontal][vertical] == 0:
                l = seekIfForThisCoordinateOnlyOneValueExists(sudoku, horizontal, vertical, optie)
                if l > 0:
                    if overlappingRowsAndColumns(horizontal, vertical, up):
                        if checkValidValue(sudoku1, horizontal, vertical, l, up):
                            sudoku[horizontal][vertical] = l
                            print("Laatste waarde.             Rij:", horizontal + 1, "kolom:", vertical + 1,
                                  "moet een ", l, "zijn.")
                        else:
                            print("ho stop, mag niet")

                    else:
                        sudoku[horizontal][vertical] = l
                        print("Laatste waarde.             Rij:", horizontal+1, "kolom:", vertical+1, "moet een ", l, "zijn.")
            vertical+=1
        horizontal+=1
        vertical=0
    return sudoku


# Main procedure for finding values with the last possible value method
def findLastPossibleValue(sudoku, optie, up, sudoku1):
    prevnullen = 81
    nullen = countZerosInMatrix(sudoku)
    teller = 0
    while nullen < prevnullen:
        prevnullen = nullen
        teller += 1
        sudoku = findLastValues(sudoku, optie, up, sudoku1)
        nullen = countZerosInMatrix(sudoku)
        #print("number of zeros", prevnullen)
    return sudoku

# ******************************** Last Value Left ***********************************************




# ******************************** Only Candidate ***********************************************


def makeListofAllNumbersThatAppearOnlyOnce(flatList):
    return [a for a in range(1,10) if flatList.count(a) == 1]


def makeFlatSortedList(nestedList):
    result = []
    if len(nestedList) == 1:
        result.append(nestedList[0])
    for x in result:
        if type(x) is int:
            result.append(x)
    result.sort()
    return result

def makeNotNestedList(nestedList):
    return list(itertools.chain.from_iterable(nestedList))

# Voeg alle mogelijke waarden van de rij toe aan 1 lijst en sorteer die lijst
# tel van elk mogelijk cijfer hoe vaak het voorkomt.
# als een cijfer exact 1 keer voorkomt betekent dit
# of deze waarde was al bekend, in dat geval is het van type int
# of we hebben een hit, ofwel een nieuwe waarde gevonden.
# dan moet er in de sudoku natuurlijk wel een nul staan, ofwel waarde was nog niet bekend.

def traceUniqueValues(possibilitiesRow):
    result = []
    flatList = makeNotNestedList(possibilitiesRow)
    onceList = makeListofAllNumbersThatAppearOnlyOnce(flatList)
    for uniqueNum in onceList:
        result.append(uniqueNum)
    return result


# Make a shadow matrix with per vakje all values that are possible there
def fillMatrixPossibilities(sudoku, matrixSize, optie):
    result = []
    if optie == 2:
        qf = createQuadsFromFile("combi.txt")
    else:
        qf = createStandardQuads()

    for horizontaal in range(0,matrixSize):
        for verticaal in range(0,matrixSize):
            if sudoku[horizontaal][verticaal] == 0:
                h = makeHorizontalLine(horizontaal + 1, sudoku)
                v = makeVerticalLine(verticaal + 1, sudoku)
                q = makeQuadrantList(horizontaal, verticaal, sudoku, qf)
                result.append([x for x in range(1, 10) if x not in h and x not in v and x not in q])
            else:
                result.append([sudoku[horizontaal][verticaal]])
    return result

def horizontalePossibilities(volledigeLijst):
    result = []
    for teller in range(0,73,9):
        result.append([x for x in volledigeLijst[teller:teller+9]])
    return result


def verticalePossibilities(volledigeLijst):
    result = []
    for x in range(0,9):
        tmp = []
        for teller in range(x, 81, 9):
            tmp.append(volledigeLijst[teller])
        result.append(tmp)
    return result


def quadrantPossibilities(horlijst):
    result = []
    tel1 = 0
    tel2 = 0
    for z in range(9):
        tmp = []
        for x in range(3):
            for y in range(3):
                tmp.append(horlijst[x+tel1][y+tel2])
        result.append(tmp)
        tel2+=3
        if tel2 > 8:
            tel2 = 0
            tel1+=3
            if tel1 > 8:
                tel1 = 0
    return result


# Make the shadow matrix of all possible values per cel
# Once that is done, check per row if there is an only candidate
# this is the case if
def findOnlyCandidateHorizontal(sudoku, matrixSize, optie):
    allPossibilities = fillMatrixPossibilities(sudoku, matrixSize, optie)
    hor = horizontalePossibilities(allPossibilities)
    verticalrotatedSudoku = [list(col) for col in zip(*sudoku)]
    verticalrotatedPossibilities = [list(col) for col in zip(*hor)]

    teller = 0
    for x in hor:
        i = traceUniqueValues(x)
        for j in i:
            if j not in sudoku[teller]:
                #print("horizontal succes", i, teller, sudoku[teller])
                telq = 0
                for w in hor[teller]:
                    if j in w:
                        #print("plek in de matrix is rij :", teller, "plek", telq)
                        sudoku[teller][telq] = j
                        print("Enige mogelijkheid (rij).   Rij:", teller + 1, "kolom:", telq + 1, "moet een ", j, "zijn.")

                    telq += 1
                #print(hor[teller])
        teller += 1

    teller = 0
    for x in verticalrotatedPossibilities:
        i = traceUniqueValues(x)
        for j in i:
            if j not in verticalrotatedSudoku[teller]:
                #print("vertical succes, getal", j, "rij", teller, verticalrotatedSudoku[teller])
                telq = 0
                for w in verticalrotatedPossibilities[teller]:
                    if j in w:
                        #print("plek in de matrix is rij", teller, "plek", telq)
                        #print("sudoku", sudoku[telq][teller])
                        sudoku[telq][teller] = j
                        print("Enige mogelijkheid (kolom). Rij:", telq + 1, "kolom:", teller + 1, "moet een ", j, "zijn.")

                    telq+=1
                #print(verticalrotatedPossibilities[teller])
        teller += 1
    return sudoku


def overlappingRowsAndColumns(row, column, up):
    result = False
    overlapUp = [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]
    overlapDown = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    if up == True:
        if [row,column] in overlapUp:
            result = True
    else:
        if [row,column] in overlapDown:
            result = True
    return result


def findOverlappingCoordinates(row, column):
    r = c = 0
    if row < 6:
        r = row + 6
    else:
        r = row - 6
    if column < 6:
        c = column + 6
    else:
        c = column - 6
    return [r, c]


def checkValidValue(sudoku, row, column, value, up):
    result = False
    newCoords = findOverlappingCoordinates(row, column)
    r = newCoords[0]
    c = newCoords[1]
    h = makeHorizontalLine(r, sudoku)
    v = makeVerticalLine(c, sudoku)
    if up == True:
        qf = createQuadsFromFile("combi.txt")
    else:
        qf = createStandardQuads()
    q = makeQuadrantList(r, c, sudoku, qf)
    q1 = findValuesNotInList(q)
    h1 = findValuesNotInList(h)
    v1 = findValuesNotInList(v)
    if value not in q1 and value not in h1 and value not in v1:
        result = True
    return result


def swapCoordinates(sudokudown, sudokuup, up):
    if up == True:
        sudokuup[6][6] = sudokudown[0][0]
        sudokuup[6][7] = sudokudown[0][1]
        sudokuup[6][8] = sudokudown[0][2]
        sudokuup[7][6] = sudokudown[1][0]
        sudokuup[7][7] = sudokudown[1][1]
        sudokuup[7][8] = sudokudown[1][2]
        sudokuup[8][6] = sudokudown[2][0]
        sudokuup[8][7] = sudokudown[2][1]
        sudokuup[8][8] = sudokudown[2][2]
        return sudokuup
    else:
        sudokudown[0][0] = sudokuup[6][6]
        sudokudown[0][1] = sudokuup[6][7]
        sudokudown[0][2] = sudokuup[6][8]
        sudokudown[1][0] = sudokuup[7][6]
        sudokudown[1][1] = sudokuup[7][7]
        sudokudown[1][2] = sudokuup[7][8]
        sudokudown[2][0] = sudokuup[8][6]
        sudokudown[2][1] = sudokuup[8][7]
        sudokudown[2][2] = sudokuup[8][8]
        return sudokudown


def main():
    matrixSize = 9
    STANDAARD = 1
    VARIABEL = 2
    CROSS = 3

    filename1 = "makkie.txt"
    sudokuUp = createMatrixFromFileinput(makeEmptyMatrix(matrixSize), leesFile(SUDOKUPATHIN + filename1))

    filename = "moeilijk.txt"
    sudokuDown = createMatrixFromFileinput(makeEmptyMatrix(matrixSize), leesFile(SUDOKUPATHIN+filename))
    print("down starting point")
    printSudoku(sudokuDown)

    for x in range(5):
        print(countZerosInMatrix(sudokuDown))
        sudokuDown = findLastPossibleValue(sudokuDown, CROSS, False, sudokuUp)
        sudokuDown = findOnlyCandidateHorizontal(sudokuDown, matrixSize, CROSS)

    print("down after first round")
    printSudoku(sudokuDown)

    print("up starting point")
    printSudoku(sudokuUp)
    sudokuUp = swapCoordinates(sudokuDown, sudokuUp, True)
    print("up after swap from down")
    printSudoku(sudokuUp)

    for x in range(12):
        print(countZerosInMatrix(sudokuUp))
        sudokuUp = findLastPossibleValue(sudokuUp, VARIABEL, True, sudokuDown)
        sudokuUp = findOnlyCandidateHorizontal(sudokuUp, matrixSize, VARIABEL)

    print("up after first round")
    printSudoku(sudokuUp)


    sudokuDown = swapCoordinates(sudokuDown, sudokuUp, False)
    print("down after swapping with up")
    printSudoku(sudokuDown)

    for x in range(5):
        print(countZerosInMatrix(sudokuDown))
        sudokuDown = findLastPossibleValue(sudokuDown, 3, False, sudokuUp)
        sudokuDown = findOnlyCandidateHorizontal(sudokuDown, matrixSize, CROSS)

    sudokuUp = swapCoordinates(sudokuDown, sudokuUp, True)
    print("up after 2nd swap from down")
    printSudoku(sudokuUp)

    for x in range(12):
        print(countZerosInMatrix(sudokuUp))
        sudokuUp = findLastPossibleValue(sudokuUp, VARIABEL, True, sudokuDown)
        sudokuUp = findOnlyCandidateHorizontal(sudokuUp, matrixSize, VARIABEL)

    print("up after second round")
    printSudoku(sudokuUp)

    sudokuDown = swapCoordinates(sudokuDown, sudokuUp, False)
    print("down after swapping with up")
    printSudoku(sudokuDown)

    for x in range(7):
        print(countZerosInMatrix(sudokuDown))
        sudokuDown = findLastPossibleValue(sudokuDown, 3, False, sudokuUp)
        sudokuDown = findOnlyCandidateHorizontal(sudokuDown, matrixSize, CROSS)

    print()
    printSudoku(sudokuUp)

    print()
    printSudoku(sudokuDown)



if __name__ == '__main__':
    main()
