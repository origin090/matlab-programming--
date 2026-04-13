i=0
A=[]
while i<=8 :
    B=int(input())
    A.append(B)
    i=i+1
print(max(A))
print(A.index(max(A))+1)