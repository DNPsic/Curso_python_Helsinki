"""
Please write a program which asks the user for a year, and
prints out the next leap year.
If the user inputs a year which is a leap year (such as 2024),
the program should print out the following leap year:
"""

# My solution:
og_year = int(input("Year: "))
year = og_year
leap_year = False
next_leap = 0

while True:
    print("Loop starts")
    print("Initial leap:", next_leap)
    print("Initial condition:", leap_year)
    print("")

    if not leap_year:
        print("Incrementing leap by 1")
        year += 1
        print("Current year:", year)
        print("")

    if year % 100 == 0:
        print("First test:")
        if year % 400 == 0:
            leap_year = True
            next_leap = year
            print("Is leap?", leap_year)
            print("Leap:", next_leap, "\n")
            break
    elif year % 4 == 0:
        print("Second test:")
        leap_year = True
        next_leap = year
        print("Is leap?", leap_year)
        print("Leap:", next_leap, "\n")
        break


print(f"The next leap year after {og_year} is {next_leap}")

# Model's solution:
# start_year = int(input("Year: "))
# year = start_year + 1
# while True:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             break
#     elif year % 4 == 0:
#         break
#
#     year += 1
#
# print(f"The next leap year after {start_year} is {year}")
