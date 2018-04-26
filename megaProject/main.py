from module import Matrix
A = Matrix.createMatrix(3, 3)
B = Matrix.createMatrix(3, 3)
print("A")
Matrix.display(A)
print("B")
Matrix.display(B)
print("Add")
matrixAdd = Matrix.add(A, B)
if matrixAdd != 1:
    Matrix.display(matrixAdd)
print("Sub")
matrixSub = Matrix.sub(A, B)
if matrixSub != 1:
    Matrix.display(matrixSub)
n = 4
print("A * " + str(n))
matrixComp = Matrix.compOfNumber(A, n)
if matrixComp != 1:
    Matrix.display(matrixComp)
print("A * B")
matrixTwoComp = Matrix.compTwoMatrix(A, B)
if matrixTwoComp != 1:
    Matrix.display(matrixTwoComp)
print("Trans B")
transMatrix = Matrix.transMatrix(B)
Matrix.display(transMatrix)
print("Det B")
detMatrix = Matrix.detMatrix(B)
if detMatrix != 1:
    print(detMatrix)



