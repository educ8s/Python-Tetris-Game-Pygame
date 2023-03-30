from gameGrid import GameGrid
from blockQueue import BlockQueue

class Game:
	def __init__(self):
		self.grid = GameGrid(20, 10)
		self.block_queue = BlockQueue()
		self.current_block = self.block_queue.get_block()
		self.game_over = False
		self.score = 0

	def block_fits(self):
		tiles = self.current_block.tile_positions()
		for position in tiles:
			if(self.grid.is_empty(position.row, position.column) == False):
				return False
		return True

	def rotate_block_cw(self):
		self.current_block.rotate()
		if self.block_fits() == False: 
			self.current_block.undo_rotate()

	def set_current_block(self):
		self.current_block = self.block_queue.get_block()
		self.current_block.reset()
		if self.block_fits() == False:
			self.game_over = True

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
			self.current_block.move(-1, 0)
			self.place_block()
			self.score += 4