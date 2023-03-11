from unittest import TestCase
from ray_tracing_challenge import *
import numpy as np

class TestMatrices(TestCase):
    def test_matrix_setitem(self):
        mat = Matrix([[1,2,3,4], [5.5,6.5,7.5,8.5],[9,10,11,12],[13.5,14.5,15.5,16.5]])
        mat[1] = [5,6,7,8]
        self.assertTrue(mat == Matrix([[1,2,3,4], [5,6,7,8],[9,10,11,12],[13.5,14.5,15.5,16.5]]))
        mat[0,2] = 3.5
        self.assertTrue(mat == Matrix([[1,2,3.5,4], [5,6,7,8],[9,10,11,12],[13.5,14.5,15.5,16.5]]))

    def test_matrix_4x4(self):
        mat = Matrix([[1,2,3,4], [5.5,6.5,7.5,8.5],[9,10,11,12],[13.5,14.5,15.5,16.5]])
        self.assertEqual(mat[0,0], 1)
        self.assertEqual(mat[0,3], 4)
        self.assertEqual(mat[1,0], 5.5)
        self.assertEqual(mat[1,2], 7.5)
        self.assertEqual(mat[2,2], 11)
        self.assertEqual(mat[3,0], 13.5)
        self.assertEqual(mat[3,2], 15.5)

    def test_matrix_2x2(self):
        mat = Matrix([[-3,5],[1,-2]])
        self.assertEqual(mat[0,0], -3)
        self.assertEqual(mat[0,1], 5)
        self.assertEqual(mat[1,0], 1)
        self.assertEqual(mat[1,1], -2)

    def test_matrix_3x3(self):
        mat = Matrix([[-3,5,0],[1,-2, -7], [0,1,1]])
        self.assertEqual(mat[0,0], -3)
        self.assertEqual(mat[1,1], -2)
        self.assertEqual(mat[2,2], 1)
        
    def test_matrix_equality(self):
        a = Matrix([[1,2,3,4], [5,6,7,8],[9,8,7,6],[5,4,3,2]])
        b = Matrix([[1,2,3,4], [5,6,7,8],[9,8,7,6],[5,4,3,2]])
        c = Matrix([[2,3,4,5], [6,7,8],9,[8,7,6,5],[4,3,2,1]])
        self.assertTrue(a == b)
        self.assertFalse(a == c)

    def test_matrix_multiply(self):
        a = Matrix([[1,2,3,4], [5,6,7,8],[9,8,7,6],[5,4,3,2]])
        b = Matrix([[-2,1,2,3], [3,2,1,-1],[4,3,6,5],[1,2,7,8]])
        exp_mat = Matrix([[20, 22, 50,48], [44,54,114,108],[40,58,110,102],[16,26,46,42]])
        actual = a*b

        a = Matrix([[1,2,3,4], [2,4,4,2],[8,6,4,1],[0,0,0,1]])
        tup = Tuple(1,2,3,1)
        exp_tup = Tuple(18,24,33,1)
        actual_tup = a*tup
        self.assertTrue(actual == exp_mat)
        self.assertTrue(actual_tup == exp_tup)

    def test_matrix_identity_matrix(self):
        a = Matrix([[0,1,2,4], [1,2,4,8],[2,4,8,16],[4,8,16,32]])
        id_matrix = IdentityMatrix(4)
        self.assertTrue(a*id_matrix == a)
     

    def test_identity_matrix_tuple(self):
        tup = Tuple(1,2,3,4)
        id_matrix = IdentityMatrix(4)
        self.assertTrue(id_matrix*tup == tup)

    def test_transpose_matrix(self):
        a = Matrix([[0,9,3,0],[9,8,0,8],[1,8,5,3],[0,0,5,8]])
        expected = Matrix([[0,9,1,0],[9,8,8,0],[3,0,5,5],[0,8,3,8]])
        actual = a.transpose()
        self.assertTrue(a.transpose() == expected)

        i = IdentityMatrix(4)
        self.assertTrue(i.transpose() == IdentityMatrix(4))

    def test_calculate_determinant(self):
        a = Matrix([[1,5],[-3,2]])
        self.assertEqual(a.determinant(), 17)

    def test_submatrix(self):
        a = Matrix([[1,5,0], [-3,2,7],[0,6,-3]])
        exp_a = Matrix([[-3,2],[0,6]])
        self.assertEqual(a.submatrix(0,2), exp_a)

        b = Matrix([[-6,1,1,6],[-8,5,8,6],[-1,0,8,2],[-7,1,-1,1]])
        exp_b = Matrix([[-6,1,6],[-8,8,6],[-7,-1,1]])
        self.assertEqual(b.submatrix(2,1), exp_b)

    def test_minor(self):
        a = Matrix([[3,5,0],[2,-1,-7],[6,-1, 5]])
        self.assertEqual(a.submatrix(1,0).determinant() , a.minor(1,0) )

    def test_cofactor(self):
        a = Matrix([[3,5,0],[2,-1,-7],[6,-1, 5]])
        self.assertEqual(a.minor(0,0), -12)
        self.assertEqual(a.minor(0,0), a.cofactor(0,0))
        self.assertEqual(a.minor(1,0), 25)
        self.assertEqual(a.minor(1,0), -1*a.cofactor(1,0))

    def test_determinant_large(self):
        a = Matrix([[1,2,6],[-5,8,-4],[2,6,4]])
        self.assertEqual(a.cofactor(0, 0) , 56)
        self.assertEqual(a.cofactor(0, 1) , 12)
        self.assertEqual(a.cofactor(0, 2) , -46)
        self.assertEqual(a.determinant() , -196)

        b = Matrix([[-2,-8,3,5],[-3,1,7,3],[1,2,-9,6],[-6,7,7,-9]])
        self.assertEqual(b.cofactor(0, 0) , 690)
        self.assertEqual(b.cofactor(0, 1) , 447)
        self.assertEqual(b.cofactor(0, 2) , 210)
        self.assertEqual(b.cofactor(0, 3) , 51)
        self.assertEqual(b.determinant() , -4071)

    def test_matrix_invertibility(self):
        a = Matrix([[6,4,4,4],[5,5,7,6],[4,-9,3,-7],[9,1,7,-6]])
        b = Matrix([[-4,2,-2,-3],[9,6,2,6],[0,-5,1,-5],[0,0,0,0]])
        self.assertTrue(a.is_invertible())
        self.assertFalse(b.is_invertible())

    def test_matrix_inverse(self):
       a = Matrix([[-5 , 2,  6 , -8 ],[ 1 , -5 ,  1 ,  8],[  7 ,  7 , -6 , -7],[  1 , -3 ,  7 ,  4]])   
       aI = a.inverse()

       self.assertEqual(a.determinant(),532 )
       self.assertEqual(a.cofactor(2,3), -160)
       self.assertEqual(aI[3,2] , -160/532)
       self.assertEqual(a.cofactor( 3, 2) , 105)
       self.assertEqual(aI[2,3],105/532)

       exp = Matrix([[0.21805 ,  0.45113 ,  0.24060 , -0.04511],
       [-0.80827, -1.45677, -0.44361,  0.52068],
       [-0.07895 , -0.22368 , -0.05263 ,  0.19737 ],
       [ -0.52256, -0.81391, -0.30075 ,  0.30639 ]])
       self.assertTrue(aI == exp )

    def test_more_matrix_inverse(self):
        a = Matrix([[8 , -5 ,  9 ,  2 ],
        [7 ,  5 ,  6 ,  1],
        [-6 ,  0 ,  9 ,  6],
        [ -3,  0, -9, -4]
        ])
        aI = Matrix([[ -0.15385, -0.15385, -0.28205, -0.53846],
        [-0.07692,  0.12308,  0.02564,  0.03077],
        [0.35897,  0.35897,  0.43590,  0.92308],
        [-0.69231, -0.69231, -0.76923, -1.92308]
        ])
    
        b = Matrix([[9,  3,  0,  9],
        [-5, -2, -6, -3],
        [-4,  9,  6,  4],
        [-7,  6,  6,  2]
        ])
        bI = Matrix([[-0.04074, -0.07778,  0.14444, -0.22222],
        [-0.07778,  0.03333,  0.36667, -0.33333],
        [-0.02901, -0.14630, -0.10926,  0.12963],
        [0.17778,  0.06667, -0.26667,  0.33333]
        ])

        self.assertTrue(aI == a.inverse() )
        self.assertTrue(bI == b.inverse() )
   
    def test_matrix_use_inverse(self):
        a = Matrix([[3, -9,  7,  3],
        [3, -8,  2, -9],
        [-4,  4,  4,  1],
        [-6,  5, -1,  1]])

        b = Matrix([[8,  2,  2,  2],
        [3, -1,  7,  0],
        [7,  0,  5,  4],
        [6, -2,  0,  5]])

        c = a * b
        self.assertTrue(c * b.inverse() == a)
    
     