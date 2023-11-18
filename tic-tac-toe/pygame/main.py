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

class TicTacToe(pygame.sprite.Sprite):
	
	def __init__(self):
		super().__init__()

	def update(self):
		pass

	def draw(self, surface):
		pass

game = TicTacToe()

def main():

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		game.update()
		game.draw(screen)

		pygame.display.update()
		clock.tick(60)


if __name__ == '__main__':
	main()
