from blocks import *
import random

class BlockQueue:
	def __init__(self):
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		self.next_block = self.random_block()

	def random_block(self):
		return random.choice(self.blocks)

	def get_block(self):
		block = self.next_block
		self.next_block = self.random_block()
		while self.next_block.id == block.id:
			self.next_block = self.random_block()
		return self.next_block