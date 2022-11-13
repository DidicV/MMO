matrix = [

[ 4,  0, -2, -1],
[ 1,  3,  4,  5],
[ 2,  3,  1,  1],
[-1,  1,  2,  3]

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

print("Min A result: ", max(min_a))
print("Max B result: ", min(max_b))
