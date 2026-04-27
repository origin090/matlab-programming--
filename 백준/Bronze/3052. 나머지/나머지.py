remainders = []

for _ in range(10):
    n = int(input())
    remainders.append(n % 42)

answer = len(set(remainders))
print(answer)