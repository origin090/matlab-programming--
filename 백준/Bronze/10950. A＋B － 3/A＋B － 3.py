x=int(input())
A=[]
B=[]
while x!=0:
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)
    x=x-1
i=0
while i<len(A):
    print(A[i]+B[i])
    i=i+1