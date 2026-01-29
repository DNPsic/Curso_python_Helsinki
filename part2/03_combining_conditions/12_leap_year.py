"""
Generally, any year that is divisible by four is a leap year.
However, if the year is additionally divisible by 100, it is a
leap year only if it also divisible by 400. Please write a program
which asks the user for a year, and then prints out whether that
year is a leap year or not.
"""

# My solution:
year = int(input("Please type in a year: "))

if year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print("That year is a leap year.")
    else:
        print("That year is not a leap year.")
elif year % 4 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

# Model's solution:
# First, we make assumption that a year is not a leap year
# leap_year = False
#
# if year % 100 == 0:
#     if year % 400 == 0:
#         leap_year = True
# elif year % 4 == 0:
#     leap_year = True
#
# if leap_year:
#     print("That year is a leap year.")
# else:
#     print("That year is not a leap year.")
"""
This solution uses some techniques that has not been reviewed in the course,
such as using boolean values in this way.
"""
