from pulp import *

Sequence = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
Vals = Sequence
Rows = Sequence
Cols = Sequence

Boxes = []
for i in range(3):
    for j in range(3):
        Boxes += [[(Rows[3*i+k], Cols[3*j+l]) for k in range(3) for l in range(3)]]

prob = LpProblem("Sudoku Problem", LpMinimize)

choices = LpVariable.dicts("Choice", (Vals, Rows, Cols), 0, 1, LpInteger)

# This ensure that each value, row, column, and box contains each value from 1 to 9 exactly once.
for r in Rows:
    for c in Cols:
        prob += lpSum([choices[v][r][c] for v in Vals]) == 1, ""

for v in Vals:
    for r in Rows:
        prob += lpSum([choices[v][r][c] for c in Cols]) == 1, ""

    for c in Cols:
        prob += lpSum([choices[v][r][c] for r in Rows]) == 1, ""

    for b in Boxes:
        prob += lpSum([choices[v][r][c] for (r, c) in b]) == 1, ""

# adding conditions (starting positions of numbers)
prob += choices["5"]["1"]["1"] == 1, ""  # number 5 is in 1st row and 1st column
prob += choices["6"]["2"]["1"] == 1, ""  # number 6 is in 2nd row and 1st column
prob += choices["8"]["4"]["1"] == 1, ""
prob += choices["4"]["5"]["1"] == 1, ""
prob += choices["7"]["6"]["1"] == 1, ""
prob += choices["3"]["1"]["2"] == 1, ""  # number 3 is in 1st row and 2nd column
prob += choices["9"]["3"]["2"] == 1, ""
prob += choices["6"]["7"]["2"] == 1, ""
prob += choices["8"]["3"]["3"] == 1, ""
prob += choices["1"]["2"]["4"] == 1, ""
prob += choices["8"]["5"]["4"] == 1, ""
prob += choices["4"]["8"]["4"] == 1, ""
prob += choices["7"]["1"]["5"] == 1, ""
prob += choices["9"]["2"]["5"] == 1, ""
prob += choices["6"]["4"]["5"] == 1, ""
prob += choices["2"]["6"]["5"] == 1, ""
prob += choices["1"]["8"]["5"] == 1, ""
prob += choices["8"]["9"]["5"] == 1, ""
prob += choices["5"]["2"]["6"] == 1, ""
prob += choices["3"]["5"]["6"] == 1, ""
prob += choices["9"]["8"]["6"] == 1, ""
prob += choices["2"]["7"]["7"] == 1, ""
prob += choices["6"]["3"]["8"] == 1, ""
prob += choices["8"]["7"]["8"] == 1, ""
prob += choices["7"]["9"]["8"] == 1, ""
prob += choices["3"]["4"]["9"] == 1, ""
prob += choices["1"]["5"]["9"] == 1, ""
prob += choices["6"]["6"]["9"] == 1, ""
prob += choices["5"]["8"]["9"] == 1, ""

prob.solve()

# print status(Optimal, Infeasible, Unbounded)
print("Status:", LpStatus[prob.status])

# Print the solved Sudoku to the console
for r in Rows:
    if r == "1" or r == "4" or r == "7":
        print("+-------+-------+-------+")
    for c in Cols:
        for v in Vals:
            if value(choices[v][r][c]) == 1:

                if c == "1" or c == "4" or c == "7":
                    print("| ", end="")

                print(v + " ", end="")

                if c == "9":
                    print("|")
