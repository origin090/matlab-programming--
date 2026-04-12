N=int(input())
A=list(map(int,input().split()))
B=[]
B.append(min(A))
B.append(max(A))
print(*B)