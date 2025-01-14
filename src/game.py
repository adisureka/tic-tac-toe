'''
	Title: Tic-Tac-Toe Game
	Author: Abhyuday Sureka
	Version: 1.0
	Date: 14th January 2025
	License: MIT License
'''
def display(grid):
	for row in grid:
		print(row)

def create_board():
	'''
	- Description: This function creates the game board
	- Param: null
	- Return: 2D Python List
	- Pre Condition: The game board must be a 3x3 table
	'''

	# To create a game board
	board = []
	for i in range(3):
		board.append([" ", " ", " "])
	return board

def get_row(rownum, board):
	'''
	- Description: This function gets the game board rows
	- Param: rownum, board
	- Return: 1D Python List
	- Pre Condition: Board must be a 3x3 table, rownum must be between 0 and 2 - inclusive of 2
	'''

	return board[rownum]

def main():
	board = create_board()
	display(board)

if __name__ == ("__main__"):
	main()