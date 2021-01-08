from studio import stdarray

A = str(input())
n = len(A)
B = str(input())
m = len(B)
arr = stdarray.create2D(n+1,m+1,0)
for i in range(1,n+1):
    for j in range(1,m+1):
        if A[i-1] == B[j-1]:
            arr[i][j] = arr[i-1][j-1]+1
        else:
            arr[i][j] = max(arr[i-1][j],arr[i][j-1])
string=""
while n>0 and m>0:
    if A[n-1] == B[m-1]:
        string+=B[m-1]
        m -= 1
        n -= 1
    elif arr[m-1][n] == arr[m][n]:
        m -= 1
    else:
        n -= 1
string=string[::-1]
print(string)
