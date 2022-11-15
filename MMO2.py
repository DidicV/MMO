from pulp import *
from prettytable import PrettyTable

def Transport(warehouses, projects, demand, supply, costs):

    print(sum(demand.values()))

    print(sum(supply.values()))

    costs = makeDict([warehouses, projects], costs, 0)

    prob = LpProblem("", LpMinimize)

    Routes = [(w, b) for w in warehouses for b in projects]

    var = LpVariable.dicts("", (warehouses, projects), 0, None, LpInteger)

    prob += (
        lpSum([var[w][b] * costs[w][b] for (w, b) in Routes]),
        "",
    )


    if sum(demand.values()) <= sum(supply.values()):

        for w in warehouses:
            prob += (
                lpSum([var[w][b] for b in projects]) <= supply[w],
                "%s" % w,
            )

        for b in projects:
            prob += (
                lpSum([var[w][b] for w in warehouses]) >= demand[b],
                "%s" % b,
            )

    else:

        for w in warehouses:
            prob += (
                lpSum([var[w][b] for b in projects]) == supply[w],
                "%s" % w,
            )

        for b in projects:
            prob += (
                lpSum([var[w][b] for w in warehouses]) <= demand[b],
                "%s" % b,
            )     

    prob.solve()

    coloana = []
    rand = []

    for i in range(0, len(projects)):
        coloana.append(str(prob.variables()[i]).split("_")[2])

    for v in prob.variables():
        rand.append(v.name.split("_")[1])
    rand = list(dict.fromkeys(rand))


    coloana.insert(0,"")
    mytable = PrettyTable(coloana)


    data = []
    col = len(projects)
    
    for v in prob.variables():
        data.append(round(v.varValue))

    matrix = [data[i:i+col] for i in range(0, len(data), col)]

    
    inndex = -1
    for row in matrix:
        inndex +=1

        row.insert(0, rand[inndex])

        mytable.add_row(row)


    print(mytable)
    print("Objective function value", round(value(prob.objective),1))




# SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY 
# OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA
# -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> ->
warehouses = ["Alabama", "Florida", "Idaho", "Kansas", "Oregon", "Texas"]

supply = {"Alabama": 1100, "Florida": 1400, "Idaho":600, "Kansas":1200, "Oregon":1300, "Texas":400}
# -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> ->
# OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA
# SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY 


projects = ["Adobe", "IBM", "Nike", "Nvidia", "Tesla"]

demand = {
    "Adobe": 750,
    "IBM": 2000,
    "Nike": 1500,
    "Nvidia": 750,
    "Tesla": 1000,
}

costs = [  
    [41, 45, 80, 76, 48],
    [27, 66, 32, 12, 45],
    [12, 43, 64, 12, 63],
    [28, 12, 65, 38, 76],
    [76, 34, 76, 36, 54],
    [45, 45, 37, 12, 54]
]


Transport(warehouses, projects, demand, supply, costs)




#DEMAND > SUPPLY

# SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY 
# OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA
# -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> ->
warehouses = ["Alabama", "Florida", "Idaho", "Kansas", "Oregon", "Texas"]

supply = {"Alabama": 1100, "Florida": 1400, "Idaho":600, "Kansas":1200, "Oregon":1300, "Texas":400}
# -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> ->
# OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA
# SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY 


projects = ["Adobe", "IBM", "Nike", "Nvidia", "Tesla"]

demand = {
    "Adobe": 950,
    "IBM": 2100,
    "Nike": 1500,
    "Nvidia": 800,
    "Tesla": 1000
}

costs = [  
    [41, 45, 80, 76, 48],
    [27, 66, 32, 12, 45],
    [12, 43, 64, 12, 63],
    [28, 12, 65, 38, 76],
    [76, 34, 76, 36, 54],
    [45, 45, 37, 12, 54]
]


Transport(warehouses, projects, demand, supply, costs)






#DEMAND < SUPPLY

# SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY 
# OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA
# -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> ->
warehouses = ["Alabama", "Florida", "Idaho", "Kansas", "Oregon", "Texas"]

supply = {"Alabama": 1150, "Florida": 1500, "Idaho":600, "Kansas":1200, "Oregon":1350, "Texas":450}
# -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> ->
# OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA
# SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY 


projects = ["Adobe", "IBM", "Nike", "Nvidia", "Tesla"]

demand = {
    "Adobe": 750,
    "IBM": 2000,
    "Nike": 1500,
    "Nvidia": 750,
    "Tesla": 1000
}

costs = [  
    [41, 45, 80, 76, 48],
    [27, 66, 32, 12, 45],
    [12, 43, 64, 12, 63],
    [28, 12, 65, 38, 76],
    [76, 34, 76, 36, 54],
    [45, 45, 37, 12, 54]
]


Transport(warehouses, projects, demand, supply, costs)
