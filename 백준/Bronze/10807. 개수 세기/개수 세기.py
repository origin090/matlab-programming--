N=int(input())
A=list(map(int,input().split()))
v=int(input())
i=0
j=0
while i<=N-1 :
    if A[i] == v :
        j=j+1
        i=i+1
    else :
        i=i+1
print(j)