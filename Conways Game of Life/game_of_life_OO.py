from tkinter import *
import numpy

class game:
	"""An object to store the game"""
	
	def __init__(self,size):
		self.size = size
		self.board = numpy.zeros((size,size))
		self.cell_size = 20
		window = Tk()
		self.canvas = Canvas(window, width = 1000, height = 1000)

		self.canvas.pack()
		return None
	
	def drawbox(self):
		self.cell_size = 20
		for y in range(len(self.board)):
			for x in range(len(self.board)):
				if self.board[y][x] == 1:
					self.canvas.create_rectangle(self.cell_size*x, self.cell_size*y, self.cell_size*x+self.cell_size, self.cell_size*y+self.cell_size, fill="#220C65", outline="#DFF2A6", width=1)
				elif self.board[y][x] == 0:
					self.canvas.create_rectangle(self.cell_size*x, self.cell_size*y, self.cell_size*x+self.cell_size, self.cell_size*y+self.cell_size, fill="#B7F3D5", outline="#DFF2A6", width=1)
		return
		
	def createGlider(self,x,y):
		self.board[x-1][y-1]=1
		self.board[x][y-1]=1
		self.board[x+1][y-1]=1
		self.board[x+1][y]=1
		self.board[x][y+1]=1
	

class cell:
	"""An object for the cells in Conway's Game of Life"""
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.num_of_neighbors = 0
		
		
	def numOfNeighbors(self):
		return
		
my_game = game(20)

my_game.drawbox()

input()