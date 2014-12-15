from tkinter import *
import numpy

class game:
	"""An object to store the game"""
	
	def __init__(self,size):
		self.size = size
		self.cell_size = 25
		window = Tk()
		self.canvas = Canvas(window, width = size*self.cell_size, height = size*self.cell_size)

		self.canvas.pack()
		
		self.board = [[cell(i,j) for j in range(size)] for i in range(size)]
		
		return None
	
	def drawbox(self):
		for y in range(self.size):
			for x in range(self.size):
				if self.board[x][y].alive == True:
					self.canvas.create_rectangle(self.cell_size*x, self.cell_size*y, self.cell_size*x+self.cell_size, self.cell_size*y+self.cell_size, fill="#220C65", outline="#DFF2A6", width=1)
				elif self.board[y][x].alive == False:
					self.canvas.create_rectangle(self.cell_size*x, self.cell_size*y, self.cell_size*x+self.cell_size, self.cell_size*y+self.cell_size, fill="#B7F3D5", outline="#DFF2A6", width=1)
		return
		
	def createGlider(self,x,y):
		self.board[x-1][y-1].alive=True
		self.board[x][y-1].alive=True
		self.board[x+1][y-1].alive=True
		self.board[x+1][y].alive=True
		self.board[x][y+1].alive=True
	

class cell:
	"""An object for the cells in Conway's Game of Life"""
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.alive = False
		self.num_of_neighbors = 0
		
		
	def countNeighbors(self):
		self.num_of_neighbors = 0
		for i in [-1,0,1]:
			for j in [-1,0,1]:
				if i==0 and j==0:
					continue
				elif (self.x+i)<0 or (self.y+j)<0:	#prevent negative indexing
					continue
				try:
					if my_game.board[self.x+i][self.y+j].alive:		##THIS ISN'T CLEAN - USES PROGRAMMERS KNOWLEDGE OF THE BOARD OBJECT'S NAME
						self.num_of_neighbors+=1
				except IndexError:
					continue
	
	def cellLifeCheck(self):
		if self.num_of_neighbors==2 or self.num_of_neighbors==3:
			self.alive = True
		else:
			cell.alive = False
			
	
	def cellBornCheck(self):
		if self.num_of_neighbors == 3:
			self.alive = True
		else:
			self.alive = False
			
######################################################################################


num_of_generations = int(input("How many generations do you wish to simulate?\n"))
			
my_game = game(20)

my_game.drawbox()

my_game.createGlider(10,10)

for _ in range(num_of_generations):
	
	for a in range(my_game.size):
		for b in range(my_game.size):
			my_game.board[a][b].countNeighbors()
			

	
	for a in range(my_game.size):
		for b in range(my_game.size):
			print(my_game.board[a][b].num_of_neighbors)
			if my_game.board[a][b].alive:
				my_game.board[a][b].cellLifeCheck()
			else:
				my_game.board[a][b].cellBornCheck()
			
	print("****")
	print(my_game.board[10][11].num_of_neighbors)
	print("xxxxx")
	
	my_game.drawbox()
	input()
	

	