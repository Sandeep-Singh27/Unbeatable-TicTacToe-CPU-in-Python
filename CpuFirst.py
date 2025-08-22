from basicFunctions.display import displayBoard
from generatePossibleBoards import generatePossibleBoards
from minmax import maxFunction
from boardConditions.checkEndNode import checkEndNode
import time
import os
import random

#clear screen at run
os.system("clear")

board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"],
]

x = random.choice([0, 1, 2])
y = random.choice([0, 1, 2])

print("CPU PLAYED:")
board[x][y] = "O"
displayBoard(board)

cpu_turn = False

while True:
    #CPU's TURN
    if cpu_turn:
        possibleBoards = generatePossibleBoards("O",board)
        board = possibleBoards[index]

        print("CPU PLAYED:")
        displayBoard(board)
        print()
        cpu_turn = False

    #PLAYER's TURN
    else:
        print("PLAYER TURN:")
        coordinates = input("Enter the coordinates where you want to play \"X\": ")
        row = int(coordinates[0])
        column = int(coordinates[1])
        board[row][column] = "X"
        
        os.system("clear")
        print("PLAYER PLAYED:")
        displayBoard(board)
        print()
        print("CPU is thinking...")
        cpu_turn = True
        time.sleep(1)
        os.system("clear")
        
    #If the game is over
    index, points = maxFunction(board,0)
    if index == None:
        if points[0]==10:
            print("CPU WON")
            break
        elif points[0]==0:
            displayBoard(board)
            print("GAME DRAW")
            break
        else:
            displayBoard(board)
            print("PLAYER WON")
            break
