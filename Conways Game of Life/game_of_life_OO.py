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
		for j in range(self.size):
			for i in range(self.size):
				if self.board[j][i].alive == True:
					self.canvas.create_rectangle(self.cell_size*i, self.cell_size*j, self.cell_size*i+self.cell_size, self.cell_size*j+self.cell_size, fill="#220C65", outline="#DFF2A6", width=1)
				elif self.board[j][i].alive == False:
					self.canvas.create_rectangle(self.cell_size*i, self.cell_size*j, self.cell_size*i+self.cell_size, self.cell_size*j+self.cell_size, fill="#B7F3D5", outline="#DFF2A6", width=1)
		return
		
	def createGlider(self,y,x):
		self.board[y-1][x-1].alive=True
		self.board[y][x-1].alive=True
		self.board[y+1][x-1].alive=True
		self.board[y+1][x].alive=True
		self.board[y][x+1].alive=True
	

class cell:
	"""An object for the cells in Conway's Game of Life"""
	def __init__(self,y,x):
		self.x = x
		self.y = y
		self.alive = False
		
		
	def countNeighbors(self):
		self.num_of_neighbors = -1
		for j in [-1,0,1]:
			for i in [-1,0,1]:
				if (self.x+i)<0 or (self.y+i)<0:	#prevent negative indexing				#could move one of these out side the current for loop to be more efficient
					print("preventing negative indexing...")
					continue
				try:
					if my_game.board[self.y +j][self.x +i].alive==True:		##THIS ISN'T CLEAN - USES PROGRAMMERS KNOWLEDGE OF THE BOARD OBJECT'S NAME
						print("adding one")
						self.num_of_neighbors+=1
					else:
						print("pass")
				except IndexError:
					print("index error....")
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
			
my_game = game(5)

my_game.drawbox()

my_game.createGlider(2,2)

for _ in range(num_of_generations):
	
	for a in range(my_game.size):
		for b in range(my_game.size):
			my_game.board[b][a].countNeighbors()
			print(my_game.board[b][a].x,my_game.board[b][a].y)
			print(my_game.board[b][a].num_of_neighbors)
			print("*x*x*")
			
	
	
	for a in range(my_game.size):
		for b in range(my_game.size):
			#print(my_game.board[a][b].num_of_neighbors)
			if my_game.board[b][a].alive:
				my_game.board[b][a].cellLifeCheck()
			else:
				my_game.board[b][a].cellBornCheck()
			
	
	my_game.drawbox()
	input()
	

	