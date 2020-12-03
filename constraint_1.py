from ortools.linear_solver import pywraplp
from get_graph import (
    total_time,
    total_vertices
)

def constraint_1(solver, b, d):
    for t in range(1, total_time):
        for x in range(total_vertices):
            solver.Add(b[x][t]-b[x][t-1] >= 0)
