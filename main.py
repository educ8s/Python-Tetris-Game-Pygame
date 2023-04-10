import pygame, sys
from game import Game
from colors import Colors

pygame.init()


screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Python Tetris")

title_font = pygame.font.Font(None, 40)
score_title_surface = title_font.render("Score", True, Colors.white)
next_title_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)


score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)


while True:
	for event in pygame.event.get():

		if event.type == GAME_UPDATE and game.game_over == False:
			game.move_down()

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if game.game_over == True:
				game.game_over = False
				game.reset()
			if event.key == pygame.K_LEFT and game.game_over == False:
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over == False:
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over == False:
				game.move_down()
				game.update_score(0, 1)
			if event.key == pygame.K_UP and game.game_over == False:
				game.rotate()
		
	screen.fill(Colors.dark_blue)

	score_surface = title_font.render(str(game.score), True, Colors.white)

	screen.blit(score_title_surface, (365, 20, 50, 50))
	screen.blit(next_title_surface, (375, 180, 50, 50))

	if game.game_over:
		screen.blit(game_over_surface, (320, 450, 50, 50))

	pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
	pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
	screen.blit(score_surface, score_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))

	game.draw(screen)

	pygame.display.update()
	clock.tick(60)