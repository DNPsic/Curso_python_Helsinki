"""
Please write a program which asks the user for three letters.
The program should then print out whichever of the three letters
would be in the middle if the letters were in alphabetical order.
You may assume the letters will be either all uppercase, or all lowercase.
"""

# My solution:
first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

# b a c
if third > first > second:
    print(f"The letter in the middle is {first}")
# b c a
elif third < first < second:
    print(f"The letter in the middle is {first}")
# a b c
elif first < second < third:
    print(f"The letter in the middle is {second}")
# c b a
elif first > second > third:
    print(f"The letter in the middle is {second}")
# a c b
elif first < third < second:
    print(f"The letter in the middle is {third}")
# c a b
elif first > third > second:
    print(f"The letter in the middle is {third}")

# Model's solution
# letter1 = input("1st letter: ")
# letter2 = input("2nd letter: ")
# letter3 = input("3rd letter: ")
#
# if letter1 > letter2 and letter1 > letter3:
#     if letter2 > letter3:
#         middle = letter2
#     else:
#         middle = letter3
# elif letter2 > letter3:
#     if letter3 > letter1:
#         middle = letter3
#     else:
#         middle = letter1
# else:
#     if letter2 > letter1:
#         middle = letter2
#     else:
#         middle = letter1
#
# print("The letter in the middle is " + middle)
"""
Model's solution it's more efficient and less confuse. At first and less confuse. At first
I didn't understand what it was doing, but I think that saves a lot of print function calls,
also it's more readable.
In addition, the use of a variable —middle in this case— which is changing every if block
seems very clever.
I must say, even if I accept the model's solution is better in general, at this point
we haven't reviewed the use of nesting if statements inside elif blocks.
"""
