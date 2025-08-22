from minmax import maxFunction
import os
current_board = [
    ['O', 'O', 'X'],
    ['X', 'X', 'X'],
    ['O', 'O', 'X'],
]
os.system("clear")
print("NOTE THAT FIRST ELEMENT IS INDEX OF POSSIBLE GENERATIONS",maxFunction(current_board,0),sep="\n")