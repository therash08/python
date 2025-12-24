num = int(input("enter 3 number: "))
# print(num)
a = num % 10
num = num // 10

b = num % 10
num = num // 10

c = num % 10
num = num // 10

print(a + b + c)
