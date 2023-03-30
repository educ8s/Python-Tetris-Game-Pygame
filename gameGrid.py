import pygame
from colors import Colors

class GameGrid:
	def __init__(self, rows, columns):
		self.grid = [[0 for j in range(columns)] for i in range(rows)]
		self.num_rows = rows
		self.num_cols = columns
		self.colors = Colors.get_colors()

	def is_inside(self, row, column):
		if row >=0 and row < self.num_rows and column >= 0 and column < self.num_cols:
			return True
		return False

	def is_empty(self, row, column):
		if self.is_inside(row, column) and self.grid[row] [column] == 0:
			return True
		return False

	def is_row_full(self, row):
		for column in range(self.num_cols):
			if self.grid[row][column] == 0:
				return False;
		return True

	def is_row_empty(self, row):
		for column in range(self.num_cols):
			if self.grid[row][column] != 0:
				return False
		return True

	def clear_row(self, row):
		for column in range(self.num_cols):
			self.grid[row] [column] = 0

	def move_row_down(self, row, numRows):
		for column in range(self.num_cols):
			self.grid[row+numRows] [column] = self.grid[row][column]
			self.grid[row][column] = 0

	def clear_full_rows(self):
		cleared = 0
		for row in range(self.num_rows-1, 0, -1):
			if self.is_row_full(row):
				self.clear_row(row)
				cleared += 1
			elif cleared > 0:
				self.move_row_down(row, cleared)
		return cleared

	def draw(self, screen):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				tile_value = int(self.grid[row][column])
				tile_rect = pygame.Rect(10 + column * 25 + 1, 10 + row * 25 + 1, 24, 24)
				#screen.blit(self.textures[tile_value], tile_rect)
				pygame.draw.rect(screen, self.colors[tile_value], tile_rect)