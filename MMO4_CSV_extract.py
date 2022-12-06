from pandas import read_csv

data  = read_csv("Data/AAPL.csv")['Date'].tolist()

apple  = read_csv("Data/AAPL.csv")['Open'].tolist()

adobe  = read_csv("Data/ADBE.csv")['Open'].tolist()
 
ibm    = read_csv("Data/IBM.csv")['Open'].tolist()

nike   = read_csv("Data/NKE.csv")['Open'].tolist()

nvidia = read_csv("Data/NVDA.csv")['Open'].tolist()

tesla  = read_csv("Data/TSLA.csv")['Open'].tolist()


for item in data[::-1]:
	print(item)

for i in reversed(range(0,len(apple))):

	print(apple[i],"\t",adobe[i],"\t",ibm[i],"\t",nike[i],"\t",nvidia[i],"\t",tesla[i])