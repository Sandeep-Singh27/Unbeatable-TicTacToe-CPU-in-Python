#this should return 0 if the board is full

def checkDraw(board):
    for row in board:
        for element in row:
            if element == "-":
                return False
    return True

if __name__ == "__main__":
    board = [
        ["X","X","X"], #for empty space use "-"
        ["X","X","X"],
        ["X","X","X"],
    ]
    print("If the Board is full it returns \"True\" else \"False\"")
    print(checkDraw(board))