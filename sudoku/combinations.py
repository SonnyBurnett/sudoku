import itertools
from functools import reduce


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


def realTrueDiv(x, y):
    teller = 0
    while x > y:
        x = x - y
        teller += 1
    return (teller)
