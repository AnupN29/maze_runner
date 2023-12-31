import pygame
from queue import Queue
from utils.reconstruct_path import *

__all__ = ['bfs']

def bfs(draw, grid, start, end):
    open_set = Queue()
    open_set.put(start)
    came_from = {}
    visited = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                came_from[neighbor] = current
                open_set.put(neighbor)
                visited.add(neighbor)
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False
