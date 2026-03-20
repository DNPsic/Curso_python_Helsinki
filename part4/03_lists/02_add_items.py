"""
Please write a program which first asks the user for the
number of items to be added. Then the program should
ask for the given number of values, one by one, and
add them to a list in the order they were typed in.
Finally, the list is printed out.
"""

items = int(input("How many items: "))
i = 1
my_list = []
while i <= items:
    new_items = int(input(f"Item {i}: "))
    my_list.append(new_items)
    i += 1
print(my_list)

# Model's solution:
#
# numbers = int(input("How many items: "))
# list = []
#
# while len(list) < numbers:
#     number = int(input(f"Item {len(list) + 1}: "))
#     list.append(number)
#
# print(list)
