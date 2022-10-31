from scipy.optimize import linprog

def LP(objective, variables, constranins, text):

	result = linprog(c=objective, A_ub=variables, b_ub=constranins, method="highs")

	print(text, round( (abs(result.fun)) ,5))
	print("X = ", end="")
	for x in result.x:
		print(round(x,5), end=",   ")
	print("\n"*3)


####################################################################################


objective =     [-75, -85, -140, -70, -80]


variables 	  = [
					[60, 65, 110, 65, 75],  
		            [40, 70,  90, 50, 45],  
		            [20, 10,  50, 30, 25],
		            [20, 30,  20, 15, 20],
		            [ 4,  6,   9,  4,  5]
	            ]  

constranins = 	[ 
					15000, 
		            13000,  
		            5600,
		            6000,
		            1200
           		]  

LP(objective, variables, constranins, "Maximization = ")

##################################################################################

objective =     [10, 7, 7, 8.5, 10, 13]

variables = [
				[-260, -210, -270, -260, -320, -250],  
	            [ -20,  -25,  -28,  -23,  -27,  -11],  
	            [ -24,  -58,  -16,  -30,  -31,  -48],
	            [ -10,  -19,  -13,  -17,  -26,  -15],
	            [-1.8, -0.5, -0.5, -1.2,   -1,   -3]
            ]

constranins = [ 
				-8000, 
        		-800,  
        		-750,
        		-400,
        		-50
           	  ]  

LP(objective, variables, constranins, "Minimization = ")
