import random

class Matrix:
    def __init__(self, s, p):
        self.rows = s
        self.columns = p
        self.matrix = []
        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.columns):
                self.matrix[i].append(random.randint(0, 1))
    def display(self):
        for i in range(self.rows):
            print(self.matrix[i])
        print("\n")

    def __add__(self, other):
        if (self.rows == other.rows) and (self.columns == other.columns):
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return result
        else:
            print("Can not be folded!")
            return 1

    def __sub__(self, other):
        if (self.rows == other.rows) and (self.columns == other.columns):
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return result
        else:
            print("Can not be folded!")
            return 1

    def __mul__(self, other):
        if type(other).__name__ == 'int':
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.matrix[i][j] = self.matrix[i][j]*other
            return result
        elif self.columns == other.rows:
            result = Matrix(self.rows, other.columns)
            for i in range(self.rows):
                for j in range(other.columns):
                    element = 0
                    for k in range(self.columns):
                        element += self.matrix[i][k]*other.matrix[k][j]
                    result.matrix[i][j] = element
            return result
        else:
            print("Can not composition")
            return 1

    def trans(self):
        result = Matrix(self.rows, self.columns)
        for j in range(self.columns):
            for i in range(self.rows):
                result.matrix[j][i] = self.matrix[i][j]
        self.matrix = result.matrix

    def getmatrix(self, r):
        result = Matrix(self.rows - 1, self.columns - 1)
        k = 0
        for i in range(self.rows):
            result.matrix[k] = []
            if i != r:
                for j in range(self.columns):
                    k += 1
                    if j != 0:
                        result.matrix[k].append(self.matrix[i][j])
        return result

    def det(self):
        if self.rows == self.columns:
            if self.rows == 3:
                det = 0
                det += self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2] + self.matrix[1][0] * self.matrix[0][2] * self.matrix[2][1] + \
                       self.matrix[0][1] * self.matrix[1][2] * self.matrix[2][0]
                det -= (self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0] + self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1] +
                        self.matrix[0][1] * self.matrix[2][2] * self.matrix[1][0])
                return det
            else:
                det = 0
                for i in range(self.rows):
                    if i % 2 == 0:
                        det += self.matrix[i][0] * self.getmatrix(i).det()
                    else:
                        det += (-self.matrix[i][0] * self.getmatrix(i).det())
                return det
        else:
            print("Can not det")
            return 'string'
