import sympy as sy
import numpy as np
from numpy import linalg as la
#1
a=np.matrix([
    [1, -2, 2, 3],
    [2, -3, 3, 3],
    [-1, 8, 1, -10],
    [2, 0, 3, -4]])
print(la.det(a))
#2
k=sy.symbols("k", real=True)
M=sy.Matrix([
    [-1-k, 3, 2],
    [4, -k, 4],
    [1, 2, 3-k]])
s=sy.solve(M.det())
print("k is", s[0])
print("k is", s[1])
print("k is", s[2])
#3
M=np.array([
    [7, 3, 2],
    [-1, 4, 5],
    [2, 1, 1]])
ResM=2*(np.dot(M,M))-6*M+7
print("Initial matrix:\n", M)
print("Result matrix:\n", ResM)  
#4
A=np.matrix([
    [1, 1, -1],
    [2, 1, 0],
    [1, -1, 1]])
B=np.matrix([
    [1,-1, 3],
    [4, 3, 2],
    [1, -2, 5]])
X=A*B.transpose()
print("X is:\n", X)
#5.1
A=np.matrix([
    [2, -2, 13],
    [0, -1, 4],
    [2, -2, 1]])
print("A**(-1) is:\n", A.transpose())
#5.2
A=np.matrix([
    [1, 1, 1, 1, 4],
    [-2, 1, 2, 1, 0],
    [2, 0, -1, 1, 2],
    [1, 0, 2, 3, 6]])
print("rank A is: ", la.matrix_rank(A))
#5.3
M1 = np.array([[2, 3, 1],
                 [5, -2, -3],
                 [3, 1, 1]]) 
v1 = np.array([1, 5, 7]) 
print("Result is: ", np.linalg.solve(M1, v1))