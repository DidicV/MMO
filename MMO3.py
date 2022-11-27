matrix = [

[ 3,  5,  4,  2],
[ 5,  6,  2,  2],
[ 2,  1,  4,  0],
[ 3,  3,  5,  2]

]

max_b = []
min_a = []

for line in matrix:
    min_a.append(min(line))

# transpose matrix
trans_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

for item in trans_matrix:
    print("->",item)

for column in trans_matrix:
    max_b.append(max(column))

print("Min A: ",min_a)
print("Max B: ",max_b)

print("Max A result: ", max(min_a))
print("Min B result: ", min(max_b))


if max(min_a) == min(max_b):
	print("Pure strategy")



from scipy.optimize import linprog

def LP(objective, variables, constranins, text, is_maximixation):

	if is_maximixation:

		for i in range(0, len(objective)):
			objective[i] *=-1
	else:

		variables = [[variables[j][i] for j in range(len(variables))] for i in range(len(variables[0]))]

		for i in range(0,len(variables)):
			for j in range(0, len(variables[i])):
				variables[i][j] *=-1

		for i in range(0, len(constranins)):
			constranins[i] *=-1

	result = linprog(c=objective, A_ub=variables, b_ub=constranins, method="revised simplex")

	print(text, round( (abs(result.fun)) ,5))
	print("X = ", end="")
	for x in result.x:
		print(round(x,5), end=",   ")
	print("\n"*3)






print("\n\n")
####################################################################################

objective =     [1, 1, 1, 1]


variables 	  = [
					[ 3,  5,  4,  2],
					[ 5,  6,  2,  4],
					[ 2,  1,  4,  0],
					[ 3,  3,  5,  2]
	            ]  

constranins = 	[ 
					1, 
		            1,  
		            1,
		            1
           		]

LP(objective, variables, constranins, "Maximization = ", True)

objective =     [1, 1, 1, 1]

variables 	  = [
					[ 3,  5,  4,  2],
					[ 5,  6,  2,  4],
					[ 2,  1,  4,  0],
					[ 3,  3,  5,  2]
	            ] 

constranins = 	[ 
					1, 
		            1,  
		            1,
		            1
           		]

LP(objective, variables, constranins, "Minimization = ", False)