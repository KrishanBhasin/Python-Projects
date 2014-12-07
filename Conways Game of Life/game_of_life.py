from tkinter import *
import numpy

window = Tk()
canvas = Canvas(window, width = 1000, height = 1000)

canvas.pack()

#create the board
def create_board(size):
	board = numpy.zeros((size,size))
	return board
	
#seed across the board
	#random?
def generate_seeds():
	"""
	need 2 "True"s in a row to return True - makes a false 2x as likely
	"""
	while 1:
		rand1 = numpy.random.rand()
		if rand1 > 0.95:
			return 1
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
	if cells_around_me ==3 or cells_around_me==2:
		board2[x][y] = 1
	else:
		board2[x][y] = 0
	return
	
def drawbox(board1):				# draws a blue box for 'alive', a green box for 'dead'
	for y in range(len(board1)):
		for x in range(len(board1)):
			if board1[y][x] == 1:
				canvas.create_rectangle(5*x, 5*y, 5*x+5, 5*y+5, fill="#220C65", outline="#DFF2A6", width=1)
			elif board1[y][x] == 0:
				canvas.create_rectangle(5*x, 5*y, 5*x+5, 5*y+5, fill="#B7F3D5", outline="#DFF2A6", width=1)


#apply rules to second board

#loop back and forth between the two boards

board1,board2 = create_board(100), create_board(100)
board1 = populate_board(board1)
board1[0][1] = 1
board1[1][0] = 1

while 1==1:

	for i in range(len(board1)):
		for j in range(len(board1[i])):
			check_if_dead(i,j,board1,board2)


	drawbox(board1)

	board1 = board2
	canvas.update()
