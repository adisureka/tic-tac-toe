from game import *

def test_get_row():
	board = [["X", "X", "O"],["O", "O", "X"],["O", "X", "O"]]
	assert get_row(0, board) == ["X", "X", "O"]
	assert get_row(1, board) == ["O", "O", "X"]
	assert get_row(2, board) == ["O", "X", "O"]

def main():
	test_get_row()
	print("All tests passed")

main()