#libraries
import pandas as pd
from pandas import read_csv
import numpy as np
from prettytable import PrettyTable

apple  = read_csv("Data/AAPL.csv")['Open']
adobe  = read_csv("Data/ADBE.csv")['Open']
ibm    = read_csv("Data/IBM.csv")['Open']
nike   = read_csv("Data/NKE.csv")['Open']
nvidia = read_csv("Data/NVDA.csv")['Open']
tesla  = read_csv("Data/TSLA.csv")['Open']

stocks = pd.concat([apple,adobe,ibm, nike, nvidia, tesla], axis = 1)

columns = ['Apple', 'Adobe', 'IBM', 'Nike', 'NVidia', 'Tesla']
stocks.columns = columns


mytable = PrettyTable(columns)

# print reversed data
print(stocks.iloc[::-1], end='\n\n\n')


# calculate returns
returns = stocks / stocks.shift(1)

#print reversed returns
print(returns.iloc[::-1], end = "\n\n\n")


logReturns = np.log(returns)

pBar = logReturns.mean()

Sigma = logReturns.cov()


print(Sigma, end='\n\n\n')

from scipy.optimize import minimize

rMin = 0.02

def risckFunction(w):
	return np.dot(w.T, np.dot(Sigma, w))

w0 = [0.1666666667, 0.1666666667, 0.1666666667, 0.1666666667, 0.1666666667, 0.1666666667]

bounds = ((0,1),(0,1),(0,1),(0,1),(0,1),(0,1))


def checkMinimumReturn(w):
	RHS = rMin - np.sum(pBar*w)
	return RHS

def checkSumToOne(w):
	return np.sum(w)-1

constraints = ({'type': 'eq', 'fun': checkMinimumReturn}, {'type': 'eq', 'fun': checkSumToOne})
w_opt = minimize(risckFunction, w0, method = 'SLSQP', bounds = bounds, constraints = constraints)


print(w_opt, end='\n\n\n')


result = []
for item in w_opt.x:
	result.append(round(item, 5))



mytable.add_row(result)

print(mytable)