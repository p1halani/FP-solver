from ortools.linear_solver import pywraplp
from get_graph import *

def get_objective():
    solver = pywraplp.Solver.CreateSolver('SCIP')
    b = [["" for t in range(total_time)] for v in range(total_vertices)]
    d = [["" for t in range(total_time)] for v in range(total_vertices)]
    for x in range(total_vertices):
        d[x][0] = solver.IntVar(0, 0, f"d({x},0)")
        val = 1 if x in initial_burning_vertices else 0
        b[x][0] = solver.IntVar(val, val, f"b({x},0)")
    for x in range(total_vertices):
        for t in range(1, total_time):
            d[x][t] = solver.IntVar(0, 1, f"d({x},{t})")
            b[x][t] = solver.IntVar(0, 1, f"b({x},{t})")

    objective = solver.Objective()
    for x in range(total_vertices):
        objective.SetCoefficient(b[x][total_time-1], 1)
    objective.SetMinimization()

    return (solver, b, d)
