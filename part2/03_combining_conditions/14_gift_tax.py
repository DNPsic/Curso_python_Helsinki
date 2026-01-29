"""
Please write a program which calculates the correct amount of tax
for a gift from a close relative. Have a look at the examples below
to see what is expected. Notice the lack of thousands separators in
the input values - you may assume there will be no spaces or other
thousands separators in the numbers in the input, as we haven't yet
covered dealing with these.
"""

# My solution:

value = int(input("Value of gift: "))
if value < 5000:
    tax = "No tax!"
elif value < 25001:
    tax = 100 + (value - 5000) * 0.08
    print(f"Amount of tax: {tax} euros")
elif value < 55001:
    tax = 1700 + (value - 25000) * 0.10
    print(f"Amount of tax: {tax} euros")
elif value < 200001:
    tax = 4700 + (value - 55000) * 0.12
    print(f"Amount of tax: {tax} euros")
elif value < 1000001:
    tax = 22100 + (value - 200000) * 0.15
    print(f"Amount of tax: {tax} euros")
elif value > 1000000:
    tax = 142100 + (value - 1000000) * 0.17
    print(f"Amount of tax: {tax} euros")

# Model's solution:

# value = int(input("Value of gift: "))
#
# if value < 5000:
#     tax = 0
# elif value <= 25000:
#     tax = 100 + (value - 5000) * 0.08
# elif value <= 55000:
#     tax = 1700 + (value - 25000) * 0.10
# elif value <= 200000:
#     tax = 4700 + (value - 55000) * 0.12
# elif value <= 1000000:
#     tax = 22100 + (value - 200000) * 0.15
# else:
#     tax = 142100 + (value - 1000000) * 0.17
#
# if tax == 0:
#     print("No tax!")
# else:
#     print(f"Amount of tax: {tax} euros")
