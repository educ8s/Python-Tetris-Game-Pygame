import pygame
from position import Position
from colors import Colors

class Block():
	def __init__(self, start_offset, id ):
		self.start_off_x  = start_offset.row
		self.start_off_y = start_offset.column
		self.offset = start_offset
		self.tiles = {}
		self.id = id
		self.rotation_state = 0
		self.colors = Colors.get_tile_colors()

	def tile_positions(self):
		tiles = self.tiles[self.rotation_state]
		new_tiles = []
		for position in tiles:
			position = Position(position.row + self.offset.row, position.column + self.offset.column)
			new_tiles.append(position)
		return new_tiles

	def rotate(self):
		self.rotation_state = (self.rotation_state + 1) % len(self.tiles)

	def undo_rotate(self):
		self.rotation_state = (self.rotation_state -1) % len(self.tiles)

	def move(self, rows, columns):
		self.offset.row += rows
		self.offset.column += columns

	def reset(self):
		self.rotation_state = 0
		self.offset.row = self.start_off_x
		self.offset.column = self.start_off_y

	def draw(self, screen):
		tiles = self.tile_positions()
		for tile in tiles:
			tile_rect = pygame.Rect(10 + (tile.column) * 25 + 1, 10 + tile.row* 25 +1, 24, 24)
			pygame.draw.rect(screen, self.colors[self.id], tile_rect)

	def draw_small_icon(self, screen):
		tiles = self.tile_positions()
		for tile in tiles:
			offset_x = 0
			offset_y = 0
			if self.id == 2:
				offset_y = 15
				offset_x = -8
			elif self.id == 4:
				offset_x = -10
			tile_rect = pygame.Rect(offset_x + 240 + (tile.column) * 20 , offset_y + 230 + tile.row* 20, 19, 19)
			pygame.draw.rect(screen, self.colors[self.id], tile_rect)