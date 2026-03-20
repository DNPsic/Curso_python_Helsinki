"""
Please write a program which asks the user to type in values
and adds them to a list. After each addition, the list
is printed out in two different ways:

in the order the items were added
ordered from smallest to greatest
The program exits when the user types in 0.
"""

items_list: list = []
while True:
    new_item: int = int(input("New item: "))
    if new_item == 0:
        break
    items_list.append(new_item)
    print(f"The list is now: {items_list}")
    print(f"The list in order: {sorted(items_list)}")
print("Bye!")
