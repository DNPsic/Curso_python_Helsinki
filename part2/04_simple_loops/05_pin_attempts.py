"""
Please write a program which keeps asking the user for a PIN
code until they type in the correct one, which is 4321.
The program should then print out the number of times the user
tried different codes.
"""

# My solution:
attempts = 0
while True:
    pin = input("PIN: ")
    attempts += 1
    if pin == "4321" and attempts == 1:
        print("Correct! It only took you one single attempt!")
        break
    elif pin == "4321":
        print(f"Correct! It took you {attempts} attempts")
        break
    print("Wrong!")

# Model's solution:
# attempts = 1
# while True:
#     pin = input("PIN: ")
#     if pin == "4321":
#         break
#     print("Wrong")
#     attempts += 1
#
# if attempts == 1:
#     print("Correct! It only took you one single attempt!")
# else:
#     print(f"Correct! It took you {attempts} attempts")
