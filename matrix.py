import random

def multiply(matrix_a,matrix_b):
    # check if each row has the same length
    for row in matrix_a:
        if len(row)!=len(matrix_a[0]):
            print "invalid matrix: matrix_A rows' length not consistent"
            return False
    for row in matrix_b:
        if len(row)!=len(matrix_b[0]):
            print "invalid matrix: matrix_B rows' length not consistent"
            return False
    # check if it's able to multiply
    if len(matrix_a[0])!=len(matrix_b):
        print "not able to multiply these matrix. rows of A and columns of B differ" 
        return False

    product=[]
    for m in range(len(matrix_a)):
        product_row = []
        for n in range(len(matrix_b[0])):
            somme = 0
            for ai, bi in zip(matrix_a[m],[row_b[n] for row_b in matrix_b]):
                somme += ai*bi
            product_row.append(somme)
        product.append(product_row)

    for p_row in product:
        print p_row
    return product


def randGenMatrix(m,n,absolute_max=9):
    return [[random.randrange(absolute_max*-1,absolute_max+1) for a in range(m)] for b in range(n)]


