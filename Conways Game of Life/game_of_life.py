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
def check_if_dead(x,y, board1, board2):
	#this function is only called on LIVING cells
	cells_around_me = 0
	for i in [-1,0,1]:
		for j in [-1,0,1]:
			if i==0 and j==0:
				continue
			if (x+i)<0 or (y+j)<0:	#prevent negative indexing
				continue
			try:
				cells_around_me += board1[x+i][y+j]
			except IndexError:
				continue
	if cells_around_me ==3:
		board2[x][y] = 1
	else:
		board2[x][y] = 0
	return


#apply rules to second board

#loop back and forth between the two boards

board1,board2 = create_board(30), create_board(30)
#board1 = populate_board(board1)
board1[0][1] = 1
board1[1][0] = 1

for i in range(len(board1)):
	for j in range(len(board1[i])):
		check_if_dead(i,j,board1,board2)

print(board1)
print("****")
print(board2)