# python3 -m venv env
# source env/bin/activate
#
# - choose one of them
# python3 -m pip install --upgrade pip
#
# python3 -m pip install pygame

import pygame
import sys

pygame.init()

WIDTH  = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Tic-Tac-Toe')

clock = pygame.time.Clock()

def my_init():
	pass

def my_update(game):
	pass

def my_draw(game, screen):
	pass

def main():

	game = my_init()

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		my_update(game)
		my_draw(game, screen)

		pygame.display.update()
		clock.tick(60)


if __name__ == '__main__':
	main()
