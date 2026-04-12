N,X=map(int,input().split())
A=list(map(int,input().split()))
B=[]
i=0
while i<=len(A)-1 :
    if A[i]<X :
        B.append(A[i])
        i=i+1
    else:
        i=i+1
print(*B)