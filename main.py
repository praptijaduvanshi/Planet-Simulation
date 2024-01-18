import pygame
from planet import Planet

pygame.init()

#Global values-- colors, font
WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
WHITE= (255, 255, 255)
ORANGE = (255, 165, 0)  # Added color for Jupiter