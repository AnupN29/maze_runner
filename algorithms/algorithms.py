from algorithms.a_star import a_star
from algorithms.dijkstra import dijkstra
from algorithms.dfs import dfs
from algorithms.bfs import bfs

__all__ = ['algorithm']


def algorithm(draw, grid, start, end):
    algo = int(input("Enter the number corresponding the algorithm to be used \n 1. DFS \n 2. BFS \n 3. Dijkstra \n 4. A_star \n"))

    if algo == 1: 
        dfs(draw, grid, start, end)

    elif algo == 2: 
        bfs(draw, grid, start, end)
    
    elif algo == 3: 
        dijkstra(draw, grid, start, end)
    
    elif algo == 4: 
        a_star(draw, grid, start, end)
    
    else: 
        print("Invalid Algorithm \n")