from .rtc_tuple import *
import numpy as np

class Matrix:
    def __init__(self, values):
        self.values = values
        self.rows = len(self.values)
        self.columns = len(self.values[0])

    def __str__(self):
        return "{}".format(self.values)

    def __getitem__(self, indices):
        if isinstance(indices, int):
            return self.values[indices]
        elif isinstance(indices, tuple):
            i, j = indices
            return self.values[i][j]
        else:
            raise TypeError("unsupported operand type(s) for []: '{}' and '{}'".format(self.__class__, type(indices)))

    def __setitem__(self, indices, value):
        if isinstance(indices, int):
            # set entire row with list value
            self.values[indices] = value
        elif isinstance(indices, tuple):
            row, col = indices
            # set single value in row, col
            self.values[row][col] = value
        else:
            raise TypeError("unsupported operand type(s) for setitem: '{}' and '{}'".format(self.__class__, type(indices)))


    def __eq__(self, matrix_b):
        # a = np.array([np.array(xi, dtype=float) for xi in self.values], dtype=float)
        # b = np.array([np.array(xi, dtype=float) for xi in matrix_b.values], dtype=float)

        # a = np.array(self.values, dtype=float)
        # b = np.array(matrix_b.values, dtype=float)
        a = self.values
        b = matrix_b.values
        for i in range(self.rows):
            for j in range(self.columns):
                print(i,j,float_equal(a[i][j] ,b[i][j]), abs(a[i][j] -b[i][j]))
                if not float_equal(a[i][j] ,b[i][j]):
                    return False
        return True

    def __mul__(self, other):
        if isinstance(other, Matrix):
            # make 0 array of MxN where M is rows of a and N is columns of b
            m = [[0 for i in range(self.rows)] for j in range(other.columns)]
            for i in range(self.rows):
                for j in range(other.columns):
                    val = 0
                    for k in range(self.columns):
                        val += self.values[i][k]*other.values[k][j]
                    m[i][j] = val
            return Matrix(m)
        elif isinstance(other, Tuple):
            # handle 1x1 matrix as scalar
            if self.rows == 1 and self.columns == 1:
                return self.value[0] * other
            
            m = [0 for i in range(self.rows)]
            tup = [other.x, other.y, other.z, other.w]
            for i in range(self.rows):
                val = 0
                for j in range(len(tup)):
                    val += self.values[i][j] * tup[j]
                m[i] = val
            return Tuple(m[0], m[1], m[2], m[3])

    def transpose(self):
        t = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.columns):
                new_row.append(self.values[j][i])
            t.append(new_row)
        return Matrix(t)

    def submatrix(self, r, c):
        # m = Matrix([[0 for i in range(self.rows - 1)] for j in range(self.columns- 1)])
        row_nums = [*range(self.rows)]
        col_nums =[*range(self.columns)]
        row_nums.pop(r)
        col_nums.pop(c)
        m = [[0 for i in range(len(row_nums))] for j in range(len(col_nums))]
        for i in range(len(row_nums)):
            for j in range(len(col_nums)):   
                m[i][j] = self.values[row_nums[i]][col_nums[j]]
        return Matrix(m)

    def determinant(self):
        if self.rows == 2 and self.columns == 2:
            return (self.values[0][0]*self.values[1][1] - self.values[0][1]*self.values[1][0])
        else:
            row = self.values[0]
            sum = 0
            for i in range(len(row)):
                sum += self.cofactor(0,i) * row[i]
            return sum

    def minor(self, r, c):
        return self.submatrix(r,c).determinant()

    def cofactor(self, r,c):
        if (r + c) % 2 == 0:
            return self.minor(r,c)
        return self.minor(r,c) * -1

    def is_invertible(self):
        return self.determinant() != 0

    def inverse(self):
        if not self.is_invertible():
            raise Exception("The matrix is not invertible. {}'".format(self.values))
        
        m = [[0 for i in range(self.rows)] for j in range(self.columns)]
        det = self.determinant()
        for row in range(len(m)):
            for col in range(len(m[0])):
                c = self.cofactor(row, col)
                m[col][row] = c/det
        return Matrix(m)




class IdentityMatrix(Matrix):
    def __init__(self, dims):
        pass
    
    def __new__(self, dims):
        m = [[0 for i in range(dims)] for j in range(dims)]
        for i in range(dims):
            for j in range(dims):
                if i == j:
                    m[i][j] = 1
                else:
                    m[i][j] = 0
        return Matrix(m)



                    

