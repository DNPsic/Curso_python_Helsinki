"""Please write a program which asks the user to input a string.
The program then prints out different messages if the string contains
any of the vowels a, e or o."""

# My solution:

in_string = input("Please type in a string: ")
a, e, o = "a", "e", "o"
if a in in_string:
    print(a, "found")
else:
    print(a, "not found")
if e in in_string:
    print(e, "found")
else:
    print(e, "not found")
if o in in_string:
    print(o, "found")
else:
    print(o, "not found")

# Model's solution:
# string = input("Please type in a string: ")
# vowels = "aeo"
# index = 0
#
# while index < len(vowels):
#     vowel = vowels[index]
#     if vowel in string:
#         print(vowel, "found")
#     else:
#         print(vowel, "not found")
#     index += 1
