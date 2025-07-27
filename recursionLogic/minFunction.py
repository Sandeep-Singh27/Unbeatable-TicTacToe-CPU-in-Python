from generatePossibleBoards import generatePossibleBoards
from boardConditions import checkEndNode
from minmaxDictionary import minOfDictionary
from .maxFunction import maxFunction

def minFunction(board):
    isEndNode, returnValue = checkEndNode(board)
    if isEndNode:
        return (None,returnValue)
    else:
        possibleBoards = generatePossibleBoards(board)
        returnValueOfPossibleBoards = []

        for eachBoard in possibleBoards:
            _, returnValueOfEachBoard = maxFunction(eachBoard)
            returnValueOfPossibleBoards.append(returnValueOfEachBoard)

        returnValueDictionary = dict(enumerate(returnValueOfPossibleBoards))

        return minOfDictionary(returnValueDictionary)