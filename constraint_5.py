from ortools.linear_solver import pywraplp
from get_graph import (
    total_time,
    total_vertices,
    neighbours_of_vertices,
    initial_burning_vertices
)


def constraint_5(solver, b, d):
    for t in range(1, total_time):
        for x in range(total_vertices):
            flag = True
            if t == 1 and x in initial_burning_vertices:
                flag = False
            if flag:
                neighbours = neighbours_of_vertices[x]
                s = 0
                for y in neighbours:
                    if b[y][t-1] == 0:
                        s = s + b[y][t-1]
                
                solver.Add(s - b[x][t] >= 0)
