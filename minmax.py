from generatePossibleBoards import generatePossibleBoards
from boardConditions.checkEndNode import checkEndNode
from minmaxDictionary.maxOfDictionary import maxOfDictionary
from minmaxDictionary.minOfDictionary import minOfDictionary

def maxFunction(board:list,depth:int):
    isEndNode, returnValue = checkEndNode(board)
    if isEndNode:
        return None,(returnValue,depth)
    else:
        possibleBoards = generatePossibleBoards("O",board)
        returnValueOfPossibleBoards = []

        for eachBoard in possibleBoards:
            _,returnValueOfEachBoardAndDepth = minFunction(eachBoard,depth+1)
            returnValueOfPossibleBoards.append(returnValueOfEachBoardAndDepth)

        returnValueDictionary = dict(enumerate(returnValueOfPossibleBoards))
        # print("max",returnValueDictionary)
        # print(maxOfDictionary(returnValueDictionary))

        return maxOfDictionary(returnValueDictionary)
    
def minFunction(board,depth):
    isEndNode, returnValue = checkEndNode(board)
    if isEndNode:
        return None,(returnValue,depth)
    else:
        possibleBoards = generatePossibleBoards("X",board)
        returnValueOfPossibleBoards = []

        for eachBoard in possibleBoards:
            _, returnValueOfEachBoardAndDepth = maxFunction(eachBoard,depth+1)
            returnValueOfPossibleBoards.append(returnValueOfEachBoardAndDepth)

        returnValueDictionary = dict(enumerate(returnValueOfPossibleBoards))
        # print("min",returnValueDictionary)
        # print(minOfDictionary(returnValueDictionary))

        return minOfDictionary(returnValueDictionary)