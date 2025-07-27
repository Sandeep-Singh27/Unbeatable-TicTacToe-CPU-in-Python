#should return -10 if X won and +10 if O won

def checkWin(board):
    #for row check
    for i in range(0,3):
        if (board[i][0]==board[i][1]) and (board[i][1]==board[i][2]) and (board[i][0]!="-"):
            if board[i][0] == "X":
                return -10
            else:
                return +10
    
    #for column check
    for i in range(0,3):
        if (board[0][i]==board[1][i]) and (board[1][i]==board[2][i]) and (board[0][i]!="-"):
            if board[0][i] == "X":
                return -10
            else:
                return +10
            
    #for diagonal-1
    if (board[0][0]==board[1][1]) and (board[1][1]==board[2][2]) and (board[1][1]!="-"):
        if board[1][1] == "X":
            return -10
        else:
            return +10
        
    #for diagonal-2
    if (board[0][2]==board[1][1]) and (board[1][1]==board[2][0]) and (board[1][1]!="-"):
        if board[1][1] == "X":
            return -10
        else:
            return +10
    
    return None
        
if __name__ == "__main__":
    board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['-', '-', 'X'],
    ]
    print("if X(Player) wins then -10")
    print("if O(PLayer) wins then +10")
    print(checkWin(board))
        