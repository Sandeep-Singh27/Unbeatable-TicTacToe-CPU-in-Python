import copy
def copyBoard(board):
    return copy.deepcopy(board)
    

if __name__=="__main__":

    from basicFunctions.display import displayBoard

    board = [
        ["X","-","-"],
        ["O","-","-"],
        ["-","-","-"],
    ]

    copied_board = copyBoard(board)
    copied_board[2][2] = "X"

    print("Copied Board")
    displayBoard(copied_board)
    print("Actual Board")
    displayBoard(board)

    