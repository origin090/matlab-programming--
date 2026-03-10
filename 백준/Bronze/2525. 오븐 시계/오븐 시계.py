a,b=map(int,input().split())
c=int(input())
d=60*a+b+c
if d//60 > 23:
    print((d//60)%24, d%60)
else:
    print(d//60, d%60)