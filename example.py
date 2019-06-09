import matrix


a=[[6,0,3],[7,1,4]]
b=[[7,6,4],[1,2,2],[5,3,1]]
print "{} * {} = ".format(a,b)
matrix.multiply(a,b)

c = matrix.randGenMatrix(3,3)
print c
