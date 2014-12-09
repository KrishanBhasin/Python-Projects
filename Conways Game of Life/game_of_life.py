from tkinter import *
import numpy


#create the board
def create_board(size):
	board = numpy.zeros((size,size))
	#board = numpy.identity(size,int)
	return board
	
#seed across the board
	#random?
def generate_seeds():
	while 1:
		rand1 = numpy.random.rand()
		if rand1 > 0.15:
			return 1
		else:
			return 0

def populate_board(board):
	for i in range(len(board)):
		for j in range(len(board[i])):
			board[i][j] = generate_seeds()
			
	return(board)

def check_if_dead(x,y, board1, board2):
	#this function is only called on LIVING cells
	cells_around_me = 0
	for i in [-1,0,1]:
		for j in [-1,0,1]:
			if i==0 and j==0:
				continue
			elif (x+i)<0 or (y+j)<0:	#prevent negative indexing
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
	cell_size = 20
	for y in range(len(board1)):
		for x in range(len(board1)):
			if board1[y][x] == 1:
				canvas.create_rectangle(cell_size*x, cell_size*y, cell_size*x+cell_size, cell_size*y+cell_size, fill="#220C65", outline="#DFF2A6", width=1)
			elif board1[y][x] == 0:
				canvas.create_rectangle(cell_size*x, cell_size*y, cell_size*x+cell_size, cell_size*y+cell_size, fill="#B7F3D5", outline="#DFF2A6", width=1)
	return
	
def create_glider(x,y,board):
	board[x-1][y-1]=1
	board[x][y-1]=1
	board[x+1][y-1]=1
	board[x+1][y]=1
	board[x][y+1]=1
	return


window = Tk()
canvas = Canvas(window, width = 1000, height = 1000)

canvas.pack()

board1,board2 = create_board(50), create_board(50)
create_glider(5,5,board1)
#board1 = populate_board(board1)
#board1[0][1] = 1
#board1[1][0] = 1

while 1==1:

	for i in range(len(board1)):
		for j in range(len(board1[i])):
			check_if_dead(i,j,board1,board2)


	drawbox(board1)

	board1 = board2
	canvas.update()
	#input()					#allow the user to step through generations
