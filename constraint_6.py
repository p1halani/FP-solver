from ortools.linear_solver import pywraplp
from get_graph import (
    total_time,
    total_vertices,
    total_defenders
)


def constraint_6(solver, b, d):
    constraint = ["" for t in range(total_time)]
    for t in range(1, total_time):
        s = d[0][t] - d[0][t-1]
        for x in range(1, total_vertices):
            s = s + d[x][t] - d[x][t-1]

        solver.Add(s <= total_defenders)
