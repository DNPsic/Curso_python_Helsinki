"""
Please write a new version of the program in the previous exercise.
In addition to the result it should also print out the calculation
performed: Limit: 2 The consecutive sum: 1 + 2 = 3
"""

# My solution:

limit = int(input("Limit: "))
consecutives = 0
sum_nums = 0
calculation = ""

while limit > sum_nums:
    consecutives += 1
    sum_nums += consecutives
    if consecutives > 1:
        calculation += f" + {str(consecutives)}"
    else:
        calculation += str(consecutives)

print(f"The consecutive sum: {calculation} = {sum_nums}")

# Model's solution:
# limit = int(input("Limit: "))
# number = 1
# sum = 1
# numbers = "1"
# while sum < limit:
#     number += 1
#     sum += number
#     # note that f-string can also be used like this
#     numbers += f" + {number}"
# print(f"The consecutive sum: {numbers} = {sum}")
