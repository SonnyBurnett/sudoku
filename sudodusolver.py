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


# Real the values from the inputfile and put them in de sudoku-matrix
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
def makeQuadrantList(hor, ver, sudoku):
    h = realTrueDiv(hor, 3)
    v = realTrueDiv(ver, 3)
    result = []
    for x in range(0,9):
        for y in range(0,9):
            if realTrueDiv(x, 3) == h and realTrueDiv(y, 3) == v:
                result.append(sudoku[x][y])
    return result


# Merge 3 lists, and remove duplicate values
def makeOneListToRuleThemAll(hor,ver,quad):
    return list(set(itertools.chain(hor,ver,quad)))


# Make a list of values that are not in a list
def findValuesNotInList(lijstje):
    return [x for x in range(1,10) if x not in lijstje]


# *************************** Last Value Left ****************************************************


# Try for this coordinate if the horizontal, vertical, or quadrant row leaves one option
def seekIfForThisCoordinateOnlyOneValueExists(sudoku, hor, vert):
    result = 0
    h = makeHorizontalLine(hor + 1, sudoku)
    v = makeVerticalLine(vert + 1, sudoku)
    q = makeQuadrantList(hor, vert, sudoku)
    h1 = findValuesNotInList(h)
    v1 = findValuesNotInList(h)
    q1 = findValuesNotInList(q)
    l1 = findValuesNotInList(makeOneListToRuleThemAll(h,v,q))
    if len(h1) == 1:
        result = h1[0]
    elif len(v1) == 1:
        result = v1[0]
    elif len(q1) == 1:
        result = q1[0]
    elif len(l1) ==  1:
        result = l1[0]
    return result


# Loop through sudoku matrix
# for every zero value, check if we can determine the value
# by checking horizontally, verticaly and square if one value is left.
def findLastValues(sudoku):
    horizontal = 0
    vertical = 0
    while horizontal <= 8:
        while vertical <= 8:
            if sudoku[horizontal][vertical] == 0:
                l = seekIfForThisCoordinateOnlyOneValueExists(sudoku, horizontal, vertical)
                if l > 0:
                    sudoku[horizontal][vertical] = l
            vertical+=1
        horizontal+=1
        vertical=0
    return sudoku





# Main procedure for finding values with the last possible value method
def findLastPossibleValue(sudoku):
    prevnullen = 81
    nullen = countZerosInMatrix(sudoku)
    teller = 0
    while nullen < prevnullen:
        prevnullen = nullen
        teller += 1
        sudoku = findLastValues(sudoku)
        nullen = countZerosInMatrix(sudoku)
        print("number of zeros", prevnullen)
    return sudoku

# ******************************** Last Value Left ***********************************************


# ******************************** Only Candidate crap ***********************************************


def findPossibleValues(h,v,q):

    a = list(set(itertools.chain(h, v, q)))
    #a = makeOneListToRuleThemAll(h,v,q)
    print("samenvoeging h v en q", a)
    b = findValuesNotInList(a)
    print("en de omgekeerde waardxen:", b)
    return b



def findOnlyCandidateVertical(sudoku):
    allPossibilities = fillMatrixPossibilities(sudoku, 9)
    result = sudoku
    nummer = 0
    for x in range(9):
        result.append(allPossibilities[x][nummer])

    return result

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
def fillMatrixPossibilities(sudoku, matrixSize):
    result = []
    for horizontaal in range(0,matrixSize):
        for verticaal in range(0,matrixSize):
            if sudoku[horizontaal][verticaal] == 0:
                h = makeHorizontalLine(horizontaal + 1, sudoku)
                v = makeVerticalLine(verticaal + 1, sudoku)
                q = makeQuadrantList(horizontaal, verticaal, sudoku)
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



# Make the shadow matrix of all possible values per cel
# Once that is done, check per row if there is an only candidate
# this is the case if
def findOnlyCandidateHorizontal(sudoku, matrixSize):
    allPossibilities = fillMatrixPossibilities(sudoku, matrixSize)
    hor = horizontalePossibilities(allPossibilities)
    verticalrotatedSudoku = [list(col) for col in zip(*sudoku)]
    verticalrotatedPossibilities = [list(col) for col in zip(*hor)]

    teller = 0
    for x in hor:
        i = traceUniqueValues(x)
        for j in i:
            if j not in sudoku[teller]:
                print("horizontal succes", i, teller, sudoku[teller])
                telq = 0
                for w in hor[teller]:
                    if j in w:
                        #print("plek in de matrix is rij :", teller, "plek", telq)
                        sudoku[teller][telq] = j
                    telq += 1
                #print(hor[teller])
        teller += 1

    teller = 0
    for x in verticalrotatedPossibilities:
        i = traceUniqueValues(x)
        for j in i:
            if j not in verticalrotatedSudoku[teller]:
                print("vertical succes, getal", j, "rij", teller, verticalrotatedSudoku[teller])
                telq = 0
                for w in verticalrotatedPossibilities[teller]:
                    if j in w:
                        #print("plek in de matrix is rij", teller, "plek", telq)
                        #print("sudoku", sudoku[telq][teller])
                        sudoku[telq][teller] = j
                    telq+=1
                #print(verticalrotatedPossibilities[teller])
        teller += 1
    return sudoku







def main():
    matrixSize = 9
    filename = "moeilijk.txt"
    sudoku = createMatrixFromFileinput(makeEmptyMatrix(matrixSize), leesFile(SUDOKUPATHIN+filename))
    for x in range(4):
        sudoku = findLastPossibleValue(sudoku)
        sudoku = findOnlyCandidateHorizontal(sudoku, matrixSize)
        printSudoku(sudoku)




if __name__ == '__main__':
    main()
