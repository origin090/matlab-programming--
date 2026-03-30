X=int(input())
N=int(input())
M=0
while N!=0:
    a,b=map(int,input().split())
    M=M+a*b
    N=N-1
if M==X:
    print('Yes')
else:
    print('No')