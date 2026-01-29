"""
The table below outlines the grade boundaries on a certain
university course. Please write a program which asks for
value in iterable: pass the amount of points received and
then prints out the grade attained according to the table.
"""

# My solution:
points = int(input("How many points [0-100]: "))
# < 0 or > 100 = impossible!
if points < 0 or points > 100:
    print("impossible!")
# 0 - 49 = fail
elif points >= 0 and points <= 49:
    print("fail")
# 50 - 59 = 1
elif points >= 50 and points <= 59:
    print("Grade: 1")
# 60 - 69 = 2
elif points >= 60 and points <= 69:
    print("Grade: 2")
# 70 - 79 = 3
elif points >= 70 and points <= 79:
    print("Grade: 3")
# 80 - 89 = 4
elif points >= 80 and points <= 89:
    print("Grade: 4")
# 90 - 100 = 5
elif points >= 90 and points <= 100:
    print("Grade: 5")

# Model's solution:

# points = int(input("How many points [0-100]: "))
#
# if points < 0 or points > 100:
#     grade = "impossible!"
# elif points < 50:
#     grade = "fail"
# elif points < 60:
#     grade = "1"
# elif points < 70:
#     grade = "2"
# elif points < 80:
#     grade = "3"
# elif points < 90:
#     grade = "4"
# else:
#     grade = "5"
#
# print(f"Grade: {grade}")
"""
The Model's solution it's more compact and do not compares
every range, instead it just filters.
"""
