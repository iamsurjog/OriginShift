import sys

import pygame
from maze import Maze

pygame.init()

screen = pygame.display.set_mode((600, 600))

maze = Maze()
maze.fully_random()
tick_counter = 0
clock = pygame.time.Clock()
n = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                n += 20
            if event.key == pygame.K_j:
                n = max(1, n-20)
    print(n)
    screen.fill((0, 0, 0))
    const = min(screen.get_width() / 2, screen.get_height() / 2) / min(*maze.size)
    cell_size = 20
    for i in range(5):
        for j in range(5):
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(const * i, const * j, cell_size, cell_size))
            if maze.maze[j][i].directions[0][0]:
                pygame.draw.rect(screen, (255, 255, 0),
                                 pygame.Rect(const * i - (const - cell_size), const * j, const - cell_size, cell_size))
            if maze.maze[j][i].directions[0][1]:
                pygame.draw.rect(screen, (255, 255, 0),
                                 pygame.Rect(const * i + cell_size, const * j, const - cell_size, cell_size))
            if maze.maze[j][i].directions[1][0]:
                pygame.draw.rect(screen, (255, 255, 0),
                                 pygame.Rect(const * i, const * j - (const - cell_size), cell_size, const - cell_size))
            if maze.maze[j][i].directions[1][1]:
                pygame.draw.rect(screen, (255, 255, 0),
                                 pygame.Rect(const * i, const * j + cell_size, cell_size, const - cell_size))

    pygame.draw.rect(screen, (255, 0, 0),
                     pygame.Rect(const * maze.origin[0], const * maze.origin[1], cell_size, cell_size))

    if tick_counter % n == 0:
        tick_counter = 1
        maze.change()
    tick_counter += 1

    pygame.display.update()

    clock.tick(1000)