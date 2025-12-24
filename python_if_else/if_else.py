email = input("enter email: ")
password = input("enter pass: ")

if email == "therash792@gmail.com" and password == 'rash':
    print("welcome")
elif email == "therash792@gmail.com" and password != 'rash':
    print('incorrect pass')
    password = input("enter pass again")
    if password == '1234':
        print('welcome, finally')
    else:
        print("try again")

else:
    print("not correct")
