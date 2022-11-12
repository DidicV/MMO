from pulp import *

from prettytable import PrettyTable



def Transport(warehouses, projects, demand, supply, costs):

    costs = makeDict([warehouses, projects], costs, 0)

    prob = LpProblem("", LpMinimize)

    Routes = [(w, b) for w in warehouses for b in projects]

    var = LpVariable.dicts("", (warehouses, projects), 0, None, LpInteger)



    prob += (
        lpSum([var[w][b] * costs[w][b] for (w, b) in Routes]),
        "",
    )

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
warehouses = ["Factory1", "Factory2", "Factory3"]

supply = {"Factory1": 100, "Factory2": 200, "Factory3":300}
# -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> ->
# OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA
# SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY 





projects = ["Customer1", "Customer2", "Customer3"]


demand = {
    "Customer1": 200,
    "Customer2": 200,
    "Customer3": 200,
}


costs = [  
    [40, 47, 80],
    [72, 36, 58],  
    [24, 61, 71]

]


# SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY 
# OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA
# -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> ->
warehouses = ["Bomba", "Maximum", "Enter","Smart","Darwin"]

supply = {  "Bomba": 1000, 
            "Maximum": 2000, 
            "Enter":4000, 
            "Smart":1500, 
            "Darwin":3000}
# -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> ->
# OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA OFERTA
# SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY SUPPLY 





projects = ["Chisinau", "Balti", "Soroca", "Cahul", "Ungheni", "Rezina"]


demand = {
    "Chisinau": 5000,
    "Balti": 1000,
    "Soroca": 700,
    "Cahul": 1500,
    "Ungheni": 2000,
    "Rezina": 700,
}


costs = [  
    [20, 40, 30, 15, 27, 23],
    [98, 54, 32, 64, 43, 97], 
    [43, 84, 36, 70, 75, 23],
    [13, 64, 68, 25, 95, 42],
    [38, 41, 84, 31, 42, 84]

]



Transport(warehouses, projects, demand, supply, costs)
