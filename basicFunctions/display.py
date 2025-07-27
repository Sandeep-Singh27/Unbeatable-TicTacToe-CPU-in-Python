def displayBoard(board):
    for i in board:
        print(i)

if __name__ == "__main__":
    board = [
        ["X","-","-"],
        ["O","-","-"],
        ["-","-","-"],
    ]
    displayBoard(board)