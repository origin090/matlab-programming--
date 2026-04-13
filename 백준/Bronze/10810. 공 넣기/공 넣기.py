N,M=map(int,input().split())
B=[]
n=0
m=0
while n<=N-1 :
    B.append(0)
    n=n+1
    
while m<=M-1 :
    i,j,k=map(int,input().split())
    while i<=j :
        B[i-1]=k
        i=i+1
    m=m+1
print(*B)