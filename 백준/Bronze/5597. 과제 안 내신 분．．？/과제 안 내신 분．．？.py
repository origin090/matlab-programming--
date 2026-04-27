A = []
l = 0
k = 0
for l in range(1,31):
    A.append(l)
B = []
for k in range(1,29):
    n = int(input())
    B.append(n)
result = [x for x in A if x not in B]
print(result[0])
print(result[1])