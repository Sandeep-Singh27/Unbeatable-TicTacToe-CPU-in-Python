from basicFunctions.copyBoard import copyBoard  

def generatePossibleBoards(value:str,board:list):
    possibleBoard = list()
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == "-":
                newBoard = copyBoard(board)
                newBoard[i][j] = value
                possibleBoard.append(newBoard)
    if len(possibleBoard) != 0:
        return possibleBoard
    else:
        return None

if __name__=="__main__":
    from basicFunctions.display import displayBoard

    board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['-', '-', 'X'],
    ]
    print("Actual board")
    displayBoard(board)
    
    possibilities = generatePossibleBoards("X",board)

    if possibilities != None:
        count = 1
        for possibility in possibilities:
            print(f"possible board {count}")
            displayBoard(possibility)
            count += 1

