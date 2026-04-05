A=int(input())
x=1
while x<=A:
    B,C=map(int,input().split())
    print("Case "+"#"+str(x)+": "+str(B)+" + "+str(C)+" = "+str(B+C))
    x=x+1
