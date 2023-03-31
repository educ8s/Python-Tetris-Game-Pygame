from game_grid import GameGrid
import random
from blocks import *

class Game:
	def __init__(self):
		self.grid = GameGrid(20, 10)
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.game_over = False
		self.score = 0

	def block_fits(self):
		tiles = self.current_block.tile_positions()
		for position in tiles:
			if self.grid.is_empty(position.row, position.column) == False :
				return False
		return True

	def rotate_block_cw(self):
		self.current_block.rotate()
		if self.block_fits() == False: 
			self.current_block.undo_rotate()

	def set_current_block(self):
		self.current_block = self.next_block
		self.current_block.reset()
		self.next_block = self.get_random_block()
		self.next_block.reset()

	def move_left(self):
		self.current_block.move(0, -1)
		if self.block_fits() == False:
			self.current_block.move(0, 1)

	def move_right(self):
		self.current_block.move(0, 1)
		if self.block_fits() == False:
			self.current_block.move(0, -1)

	def place_block(self):
		tiles = self.current_block.tile_positions()
		for position in tiles:
			self.grid.grid[position.row][position.column] = self.current_block.id
		cleared_rows = self.grid.clear_full_rows()

		if cleared_rows == 1:
			self.score += 40
		elif cleared_rows == 2:
			self.score += 100
		elif cleared_rows == 3:
			self.score += 300
		elif cleared_rows == 4:
			self.score += 1200
			
		self.set_current_block()

	def move_down(self):
		self.current_block.move(1,0)
		if self.block_fits() == False:
			for tile in self.current_block.tile_positions():
				if tile.row == 1:
					self.game_over = True
			self.current_block.move(-1, 0)
			self.place_block()
			self.score += 4

	def reset(self):
		self.grid.reset()
		self.set_current_block()
		self.score = 0
		self.game_over = False
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()

	def get_random_block(self):
		if len(self.blocks) != 0:
			return self.blocks.pop(random.randrange(len(self.blocks)))
		else:
			self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
			return self.blocks.pop(random.randrange(len(self.blocks)))