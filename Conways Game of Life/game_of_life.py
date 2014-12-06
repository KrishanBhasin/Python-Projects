from tkinter import *
import numpy

window = Tk()
canvas = Canvas(window, width = 800, height = 800)

#create the board
def create_board(size):
	board = numpy.identity(size,int)
	return board
	
#seed across the board
	#random?
def generate_seeds():
	"""
	need 2 "True"s in a row to return True - makes a false 2x as likely
	"""
	while 1:
		rand1 = numpy.random.rand()
		if rand1 > 0.5:
			rand2 = numpy.random.rand()
			if rand2>0.5:
				return 1
			else:
				return 0
		else:
			return 0

def populate_board(board):
	for i in range(len(board)):
		for j in range(len(board[i])):
			board[i][j] = generate_seeds()
			
	return(board)

#copy over to second board

#apply rules to second board

#loop back and forth between the two boards

board = create_board(30)
board = populate_board(board)