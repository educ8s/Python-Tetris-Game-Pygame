import pygame, sys
from game import Game
from colors import Colors

pygame.init()

score_font = pygame.font.Font(None, 40)
gameover_font = pygame.font.Font(None, 25)

score_title_surface = score_font.render("Score", True, Colors.white)
next_title_surface = score_font.render("Next", True, Colors.white)
gameover_title_surface = gameover_font.render("GAME OVER", True, Colors.white)

screen = pygame.display.set_mode((400,520))
game_rect = pygame.Rect(10, 10, 250, 500)
score_rect = pygame.Rect(270, 50, 120, 60)
next_rect = pygame.Rect(270, 180, 120, 140)
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 150) 

game = Game()

while True:
	for event in pygame.event.get():
		if event.type == GAME_UPDATE and game.game_over == False:
			game.move_down()

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if game.game_over == True:
				game.reset()
			if event.key == pygame.K_UP and game.game_over == False:
				game.rotate_block_cw()
			elif event.key == pygame.K_LEFT and game.game_over == False:
				game.move_left()
			elif event.key == pygame.K_RIGHT and game.game_over == False:
				game.move_right()
			elif event.key == pygame.K_DOWN and game.game_over == False:
				game.move_down()
	#Drawing
	screen.fill(Colors.dark_blue)
	pygame.draw.rect(screen, Colors.grey, game_rect)
	pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
	pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
	screen.blit(score_title_surface, (295, 20, 50, 50))
	screen.blit(next_title_surface, (300, 150, 50, 50))

	score_surface = score_font.render(str(game.score), True, (255, 255, 255))
	text_rect = score_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery)
	screen.blit(score_surface, text_rect)
	game.grid.draw(screen)
	if game.game_over:
		screen.blit(gameover_title_surface, (275, 380, 50, 50))

	game.current_block.draw(screen)
	game.next_block.draw_small_icon(screen)

	pygame.display.update()
	clock.tick(60)