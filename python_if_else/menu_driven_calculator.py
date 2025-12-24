fnum = int(input("enter the 1st num: "))
snum = int(input("enter the 2nd num: "))

op = input("enter the operation")
if op == '+':
    print(fnum + snum)
elif op == '-':
    print(fnum - snum)
elif op == '*':
    print(fnum * snum)
else:
    print(fnum / snum)
