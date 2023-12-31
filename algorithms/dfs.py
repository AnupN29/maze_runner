import pygame
from utils.reconstruct_path import *

__all__ = ['dfs']


def dfs(draw, grid, start, end):
    stack = [start]
    came_from = {}
    visited = {start}

    while stack:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = stack.pop()

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                came_from[neighbor] = current
                visited.add(neighbor)
                neighbor.make_open()
                

        draw()

        if current != start:
            current.make_closed()

    return False
