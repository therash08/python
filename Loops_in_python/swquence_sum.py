n = int(input("enter n "))
res = 0
fact = 1

for i in range(1, n+1):
    fact = fact * i
    res = res + i/fact
print(res)
