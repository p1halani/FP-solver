from __future__ import print_function
from ortools.linear_solver import pywraplp
from get_graph import (
    total_time,
    total_vertices
)
from objective_fn import get_objective
from constraint_1 import constraint_1
from constraint_2 import constraint_2
from constraint_3 import constraint_3
from constraint_4 import constraint_4
from constraint_5 import constraint_5
from constraint_6 import constraint_6

def main():
    solver, b, d = get_objective()
    constraint_1(solver, b, d)
    constraint_2(solver, b, d)
    constraint_3(solver, b, d)
    constraint_4(solver, b, d)
    constraint_5(solver, b, d)
    constraint_6(solver, b, d)
    
    # Solve!
    status = solver.Solve()

    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())
    if status == solver.OPTIMAL:
        print('Objective value =', solver.Objective().Value())
        print('Problem solved in %d iterations' % solver.iterations())
        print("===================burning matrix======================")
        for x in range(total_vertices):
            for t in range(total_time):
                print(b[x][t].name() + " = " + str(b[x][t].solution_value()), end = "\t")
            print()
        print("===================defending matrix======================")
        for x in range(total_vertices):
            for t in range(total_time):
                print(d[x][t].name() + " = " + str(d[x][t].solution_value()), end="\t")
            print()
    else:  # No optimal solution was found.
        if status == solver.FEASIBLE:
            print('A potentially suboptimal solution was found.')
        else:
            print('The solver could not solve the problem.')

if __name__ == '__main__':
    main()
