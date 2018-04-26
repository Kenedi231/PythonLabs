import random

class Matrix:
    def __init__(self, s, p):
        self.string = s
        self.pillar = p
        self.matrix = []
        for i in range(self.string):
            self.matrix.append([])
            for j in range(self.pillar):
                self.matrix[i].append(random.randint(1, 101))

    def createMatrix(s, p):
        return Matrix(s, p).matrix

    def display(matrix):
        string = len(matrix)
        for i in range(string):
            print(matrix[i])
        print(" ")

    def add(p1, p2):
        string = len(p1)
        pillar = len(p1[0])
        matrix = []
        if string == len(p2) and pillar == len(p2[0]):
            for i in range(string):
                matrix.append([])
                for j in range(pillar):
                    matrix[i].append(p1[i][j] + p2[i][j])
        else:
            print("Can not added")
            return 1
        return matrix
    def sub(p1, p2):
        string = len(p1)
        pillar = len(p1[0])
        matrix = []
        if string == len(p2) and pillar == len(p2[0]):
            for i in range(string):
                matrix.append([])
                for j in range(pillar):
                    matrix[i].append(p1[i][j] - p2[i][j])
        else:
            print("Can not subbed")
            return 1
        return matrix
    def compOfNumber(matrix, n):
        result = []
        for i in range(len(matrix)):
            result.append([])
            for j in range(len(matrix[0])):
                result[i].append(matrix[i][j] * n)
        return result

    def compTwoMatrix(p1, p2):
        result = []
        resultS = len(p1)
        resultP = len(p2[0])
        pillar = len(p1[0])
        string = len(p2)
        if pillar == string:
            for i in range(resultS):
                result.append([])
                for j in range(resultP):
                    element = 0
                    for k in range(pillar):
                        element += p1[i][k]*p2[k][j]
                    result[i].append(element)
            return result
        else:
            print("Can not composition")
            return 1

    def transMatrix(matrix):
        result = []
        pillar = len(matrix[0])
        string = len(matrix)
        for j in range(pillar):
            result.append([])
            for i in range(string):
                result[j].append(matrix[i][j])
        return result

    def detMatrix(matrix):
        det = 0
        string = len(matrix)
        pillar = len(matrix[0])
        if string == pillar:
            if string == 1:
                det += matrix[0][0]
            elif string == 2:
                det += matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            elif string == 3:
                det += matrix[0][0]*matrix[1][1]*matrix[2][2] + matrix[1][0]*matrix[0][2]*matrix[2][1] + matrix[0][1]*matrix[1][2]*matrix[2][0]
                det -= (matrix[0][2]*matrix[1][1]*matrix[2][0] + matrix[0][0]*matrix[1][2]*matrix[2][1] + matrix[0][1]*matrix[2][2]*matrix[1][0])
            else:
                print("Can not DET")
                det += 1
            return det
        else:
            print("Can not det")
            return 1