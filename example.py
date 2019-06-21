import matrix

b = [[2,-2,4,2],[2,-1,6,3],[3,-2,12,12],[-1,3,-4,4]]

print matrix.determinant(b) # should be 120

for i in range(50):
    matrix.genExo(i,2)
