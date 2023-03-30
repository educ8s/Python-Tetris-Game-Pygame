import pygame, sys
from game import Game

pygame.init()

score_font = pygame.font.Font(None, 40)

screen = pygame.display.set_mode((400,520))

game_rect = pygame.Rect(10, 10, 250, 500)
score_rect = pygame.Rect(270, 50, 120, 60)
score_rect = pygame.Rect(270, 50, 120, 60)
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200) 

game = Game()

while True:
	for event in pygame.event.get():
		if event.type == GAME_UPDATE and game.game_over == False:
			game.move_down()

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				game.rotate_block_cw()
			elif event.key == pygame.K_LEFT:
				game.move_left()
			elif event.key == pygame.K_RIGHT:
				game.move_right()
			elif event.key == pygame.K_DOWN:
				game.move_down()
	#Drawing
	screen.fill((44,44,127))
	pygame.draw.rect(screen, (15,15,15), game_rect)
	pygame.draw.rect(screen, (59, 85, 162), score_rect, 0, 10)
	score_title_surface = score_font.render("Score", True, (255, 255, 255))
	screen.blit(score_title_surface, (290, 20, 50, 50))

	score_surface = score_font.render(str(game.score), True, (255, 255, 255))
	text_rect = score_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery)
	screen.blit(score_surface, text_rect)

	game.grid.draw(screen)
	game.current_block.draw(screen)

	pygame.display.update()
	clock.tick(60)