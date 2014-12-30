#TODO - automate the generation cyling
#TODO - generate more templates (gun, oscillator,LWSS etc)
#TODO - allow rotation of templates
#TODO - replace self.alive usage with a check on self.age instead - age makes alive redundant.

from tkinter import *


class game:
	"""An object to store the board for Conway's Game of Life"""

	def __init__(self, number_of_cells):
		self.number_of_cells = number_of_cells
		self.cell_size = 25
		window = Tk()
		self.canvas = Canvas(window, width=number_of_cells * self.cell_size, height=number_of_cells * self.cell_size)
		self.canvas.pack()

		self.board = [[cell(i, j) for i in range(number_of_cells)] for j in range(number_of_cells)]

		return None

	def drawbox(self):
		"""A method to draw the canvas on screen, to show the cells"""
		for j in range(self.number_of_cells):
			for i in range(self.number_of_cells):
				self.box_colour = self.board[i][j].colour
					
				self.canvas.create_rectangle(self.cell_size * i, self.cell_size * j,self.cell_size * i + self.cell_size,
				self.cell_size * j + self.cell_size, fill=self.box_colour, outline="#FFFFFF",width=2)

		return
		
	def countNeighbors(self,x,y):
		"""A method to count the neighbours of a 'cell' object stored inside the 'game' object"""
		self.board[x][y].num_of_neighbors = 0
		for j in [-1, 0, 1]:
			for i in [-1, 0, 1]:
				if i == 0 and j == 0:	#avoid counting self
					continue
				elif (self.board[x][y].x + i) < 0 or (self.board[x][y].y + j < 0):	#avoid negative indexing
					continue
				try:
					if self.board[self.board[x][y].x + i][self.board[x][y].y + j].alive:	#increase count if living cell is found
						self.board[x][y].num_of_neighbors += 1
						continue
					else:	#ignore blank squares
						continue
				except IndexError:	#avoid IndexError from index too large
					continue

	def createGlider(self, x, y):
		"""Method to create a Glider on the game board"""
		if x<1 or y<1 or x>self.number_of_cells-1 or y>self.number_of_cells-1:
			return None		#rudimentary index error/negative indexing protection
		self.board[x - 1][y - 1].alive = True
		self.board[x][y - 1].alive = True
		self.board[x + 1][y - 1].alive = True
		self.board[x + 1][y].alive = True
		self.board[x][y + 1].alive = True
		
	def createGun(self,x,y):
		#TODO create a glider gun
		return None
		
	def create2PeriodOscillator(self,x,y):
		"""creates a vertical 2 period oscillator"""
		if x<1 or y<1 or x>self.number_of_cells-1 or y>self.number_of_cells-1:
			return None		#rudimentary index error/negative indexing protection
		self.board[x][y - 1].alive = True
		self.board[x][y].alive = True
		self.board[x][y + 1].alive = True

class cell:
	"""An object for the cells in Conway's Game of Life"""
	#TODO make the cells change colour based on how many generations they've been alive
	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.alive = False
		self.age = 0	#use this age to manipulate a hex number, which will choose the colour of the living cell
		self.colour = "#B7F3D5"
		
	def updateColour(self):
		if self.age == 0:
			self.colour = "#B7F3D5"
		else:
			self.colour = "#%06x".upper() % (self.age*10)
		print(self.colour)
		

	def livingCellCheck(self):
		"""Method to check if a cell STAYS alive"""
		if self.num_of_neighbors in [2,3]:
			self.alive = True
			self.age+=1
		else:
			self.alive = False
			self.age = 0


	def deadCellCheck(self):
		"""Method to check if a cell comes to life from DEAD"""
		if self.num_of_neighbors == 3:
			self.alive = True
			self.age = 1
		else:
			self.alive = False
	
def main():	
	num_of_generations = int(input("How many generations do you wish to simulate?\n"))

	#create a game object
	my_game = game(20)

	#create a still life on the board...
	my_game.board[1][1].alive = True
	my_game.board[1][2].alive = True
	my_game.board[2][2].alive = True

	my_game.createGlider(5, 18)
	
	my_game.createGlider(10,10)
	
	my_game.create2PeriodOscillator(12,2)
	
	#draw the game on screen
	my_game.drawbox()
	
	for _ in range(num_of_generations):
		for a in range(my_game.number_of_cells):
			for b in range(my_game.number_of_cells):
				my_game.countNeighbors(a,b)

		for a in range(my_game.number_of_cells):
			for b in range(my_game.number_of_cells):
				#print(my_game.board[a][b].num_of_neighbors)
				if my_game.board[a][b].alive:
					my_game.board[a][b].livingCellCheck()
				else:
					my_game.board[a][b].deadCellCheck()
				my_game.board[a][b].updateColour()
		input()
		
		my_game.drawbox()

######################################################################################

if __name__ == "__main__":
	main()


