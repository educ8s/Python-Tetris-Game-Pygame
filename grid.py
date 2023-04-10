import pygame
from colors import Colors

class Grid:
	def __init__(self):
		self.num_rows = 20
		self.num_columns = 10
		self.cell_size = 30
		self.grid = [[0 for j in range(self.num_columns)] for i in range(self.num_rows)]
		self.colors = Colors.get_cell_colors()

	def print_grid(self):
		for row in range(self.num_rows):
			for column in range(self.num_columns):
				print(self.grid[row][column], end=' ')
			print()

	def is_inside(self, row, column):
		if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_columns:
			return True
		return False

	def is_empty(self, row, column):
		if self.grid[row][column] == 0:
			return True
		return False

	def is_row_full(self, row):
		for column in range(self.num_columns):
			if self.grid[row][column] == 0:
				return False
		return True

	def move_row_down(self, row, num_rows):
		for column in range(self.num_columns):
			self.grid[row+num_rows] [column] = self.grid[row][column]
			self.grid[row][column] = 0

	def clear_row(self, row):
		for column in range(self.num_columns):
			self.grid[row][column] = 0

	def clear_full_rows(self):
		completed = 0
		for row in range(self.num_rows-1, 0, -1):
			if self.is_row_full(row):
				self.clear_row(row)
				completed += 1
			elif completed > 0:
				self.move_row_down(row, completed)
		return completed
    
	def draw(self, screen):
		for row in range(self.num_rows):
			for column in range(self.num_columns):
				cell_value = self.grid[row][column]
				cell_rect = pygame.Rect(11 + column*self.cell_size, 11 + row*self.cell_size, self.cell_size -1 , self.cell_size - 1)
				pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

	def reset(self):
		for row in range(self.num_rows):
			for column in range(self.num_columns):
				self.grid[row][column] = 0