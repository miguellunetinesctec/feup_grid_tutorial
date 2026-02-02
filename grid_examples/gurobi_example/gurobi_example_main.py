import numpy as np
import gurobipy as GRB

# Create a new model
model = Model("simple_model")

# Create variables
x = model.addVar(vtype=GRB.CONTINUOUS, name="x")
y = model.addVar(vtype=GRB.CONTINUOUS, name="y")

# Set objective
model.setObjective(3 * x + 4 * y, GRB.MAXIMIZE)

# Add constraints
model.addConstr(x + 2 * y <= 14, "c0")
model.addConstr(3 * x - y >= 0, "c1")
model.addConstr(x - y <= 2, "c2")

# Optimize model
model.optimize()

# Store results in csv file
with open("output/gurobi_results.csv", "w") as f:
    f.write("Variable,Value\n")
    for v in model.getVars():
        f.write(f"{v.varName},{v.x}\n")
    f.write(f"Objective,{model.objVal}\n")

