from pathfinder import *
import pygame

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Shortest Paths Visualiser")

main_func(WIN, WIDTH)
