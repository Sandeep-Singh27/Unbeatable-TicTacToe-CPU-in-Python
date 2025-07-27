from .checkWin import checkWin
from .checkDraw import checkDraw

def checkEndNode(board):
    whoWins = checkWin(board) # -10 if "X" | +10 if "O" , None if nobody does
    if whoWins == None:
        if checkDraw(board):
            return (True,0)
        else:
            return (False,None)
    else:
        return (True,whoWins) # (True,-10) if "X" | (True,+10) if "O" , None if nobody does

if __name__ == "__main__":
    board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['-', '-', 'X'],
    ]

    print(checkEndNode(board))
    
