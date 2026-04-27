N, M = map(int,input().split())
k = 0
l = 1
A = []
for l in range (1,N+1):
    A.append(l)
    l = l+1
while k < M:
    i, j = map(int,input().split())
    A[i-1], A[j-1] = A[j-1], A[i-1]
    k = k+1
print(*A)