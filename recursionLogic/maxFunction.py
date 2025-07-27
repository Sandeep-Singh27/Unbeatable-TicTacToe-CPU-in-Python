from generatePossibleBoards import generatePossibleBoards
from boardConditions import checkEndNode
from minmaxDictionary import maxOfDictionary
from .minFunction import minFunction

def maxFunction(board):
    isEndNode, returnValue = checkEndNode(board)
    if isEndNode:
        return (None,returnValue)
    else:
        possibleBoards = generatePossibleBoards(board)
        returnValueOfPossibleBoards = []

        for eachBoard in possibleBoards:
            _, returnValueOfEachBoard = minFunction(eachBoard)
            returnValueOfPossibleBoards.append(returnValueOfEachBoard)

        returnValueDictionary = dict(enumerate(returnValueOfPossibleBoards))

        return maxOfDictionary(returnValueDictionary)