"""
Please write a program which asks the user for a password.
The program should then ask the user to type in the password
again. If the user types in something else than the first
password, the program should keep on asking until the user
types the first password again correctly.
"""

# My solution:
password = input("Password: ")
while True:
    repeated = input("Repeat password: ")
    if repeated != password:
        print("They do not match!")
    else:
        break
print("User account created!")

# Model's solution:
# password = input("Password: ")
# while True:
#     password_again = input("Repeat password: ")
#     if password == password_again:
#         break
#     print("They do not match!")
#
# print("User account created!")
