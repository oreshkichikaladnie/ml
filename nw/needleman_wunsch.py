import random
import numpy as np

A, B = "", ""
nr = ["A", "G", "C", "T","U"]
for i in range(5):
    A += nr[random.randint(0, 4)]
    B += nr[random.randint(0, 4)]
print(A)
print(B)
ii = len(B)
jj = len(A)


def d(a,b):
    match=1
    mismatch=-1
    if a == b:
        return match
    if a != b:
        return mismatch

def f(i, j):
    global matrix, A, B
    s1 = matrix[i-1][j-1] + d(A[i-1], B[j-1])
    s2 = matrix[i-1][j] - 1
    s3 = matrix[i][j-1] - 1
    a=max(s1,s2,s3)
    return a


matrix = np.zeros((ii+1, jj+1), dtype="O")
for i in range(1,ii+1):
    matrix[i][0] = matrix[i-1][0] -1
for j in range(1,jj+1):
    matrix[0][j] = matrix[0][j-1] -1
    for i in range(1,ii+1):
        for j in range(1,jj+1):
            matrix[i][j] = f(i,j)
print(matrix)
s1 = s2 = ""
i = len(A)
j = len(B)
while i>1 or j>1:
    if matrix[i][j]==matrix[i-1][j-1] + d(A[i-1],B[j-1]):
        s1 += A[i-1]
        s2 += B[j-1]
        i -= 1
        j -= 1
    elif matrix[i][j]==matrix[i-1][j] -1:
        s1 += A[i-1]
        s2 += "-"
        i -= 1
    elif matrix[i][j]==matrix[i][j-1] -1:
        s2 += B[j-1]
        s1 += "-"
        j -= 1

while i>1:
    s1 += A[i-1]
    s2 += "-"
    i-=1
while j>1:
    s1 += "-"
    s2 += B[j-1]
    j-=1

s1=s1[::-1]
s2=s2[::-1]
print(s1,s2)