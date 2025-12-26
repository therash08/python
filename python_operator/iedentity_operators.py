# IN Operator

#  list1 = [1, 2, 3, 4, 5]
# str1 = "Hello World"
# dict1 = {1: "Geeks", 2: "for", 3: "geeks"}

# print(2 in list1)      # checking integer in a list
# print('O' in str1)     # checking character in a string
# print(3 in dict1)      # checking key in a dictionary


# NOT IN Operator
# list1 = [1, 2, 3, 4, 5]
# str1 = "Hello World"
# dict1 = {1: "Geeks", 2: "for", 3: "geeks"}

# print(2 not in list1)    # integer check in list
# print('O' not in str1)   # character check in string
# print(3 not in dict1)    # key check in dictionary


# import operator

# print(operator.contains([1, 2, 3, 4, 5], 2))         # list
# print(operator.contains("Hello World", 'o'))         # string
# print(operator.contains({1, 2, 3, 4, 5}, 6))         # set
# print(operator.contains({1: "Geeks", 2: "for"}, 3))   # dictionary key
# print(operator.contains((1, 2, 3, 4, 5), 9))         # tuple

# IS Operator

num1 = 5
num2 = 5

a = [1, 2, 3]
b = [1, 2, 3]
c = a

s1 = "hello world"
s2 = "hello world"

print(num1 is num2)  # integers
print(a is b)        # lists
print(a is c)        # reference
print(s1 is s2)      # strings
