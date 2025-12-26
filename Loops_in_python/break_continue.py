# for i in range(1, 11):
#     if i == 6:
#         continue
#     print(i, end=" ")

# for char in "GeeksforGeeks":
#     if char == "e":
#         continue
#     print(char, end=" ")


# i = 0
# while i < 10:
#     if i == 5:
#         i += 1  # ensure the loop variable is incremented to avoid infinite loop
#         continue
#     print(i)
#     i += 1


# Python break statement

# Example: Searching for an element in a list

# a = [1, 3, 5, 7, 9, 11]
# val = 7

# for i in a:
#     if i == val:
#         print(f"Found at {i}!")
#         break
# else:
#     print(f"not found")


# for i in range(10):
#     print(i)
#     if i == 6:
#         break


for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)
