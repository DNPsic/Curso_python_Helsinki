"""
Please write a program which asks the user to type in a limit.
The program then calculates the sum of consecutive numbers
(1 + 2 + 3 + ...) until the sum is at least equal to the limit
set by the user.
"""

# My solution:

limit = int(input("Limit: "))
consecutives = 0
sum_nums = 0

while limit > sum_nums:
    consecutives += 1
    sum_nums += consecutives

print(sum_nums)

# # Model's solution:
# limit = int(input("Limit: "))
# number = 1
# sum = 1
# while sum < limit:
#     number += 1
#     sum += number
# print(sum)
