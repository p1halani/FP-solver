from ortools.linear_solver import pywraplp
from get_graph import (
    total_time,
    total_vertices,
    neighbours_of_vertices
)


def constraint_3(solver, b, d):
    for t in range(1, total_time):
        for x in range(total_vertices):
            for idx, y in enumerate(neighbours_of_vertices[x]):
                solver.Add(b[y][t-1] - b[x][t] - d[x][t] <= 0)
