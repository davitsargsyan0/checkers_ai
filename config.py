import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

RED = (180, 0, 0)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)
GREY = (210, 180, 140)
CREME = (245, 245, 220)

CROWN = pygame.transform.scale(pygame.image.load('images/king.png'), (44, 44))

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))