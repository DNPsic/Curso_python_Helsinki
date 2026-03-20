"""Please write a program which asks the user to choose
between addition and removal. Depending on the choice,
the program adds an item to or removes an item from the
end of a list. The item that is added must always be one
greater than the last item in the list. The first item to
be added must be 1.
"""

my_list: list = []

while True:
    print("The list is now", my_list)
    operation: str = input("a(d)d, (r)emove, or e(x)it: ")
    if operation == "x":
        break
    elif operation == "d" and len(my_list) == 0:
        my_list.append(1)
    elif operation == "d":
        my_list.append(my_list[-1] + 1)
    elif operation == "r":
        my_list.pop()
print("Bye!")

# Model's solution:
# list = []
# while True:
#     print(f"The list is now {list}")
#     selection = input("a(d)d, (r)emove or e(x)it:")
#     if selection == "d":
#         # Value of item is length of the list + 1
#         item = len(list) + 1
#         list.append(item)
#     elif selection == "r":
#         list.pop(len(list) - 1)
#     elif selection == "x":
#         break
#
# print("Bye!")
