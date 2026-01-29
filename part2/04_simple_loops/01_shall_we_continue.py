"""
Let's create a program along the lines of the example above.
This program should print out the message "hi" and then ask
"Shall we continue?" until the user inputs "no". Then the
program should print out "okay then" and finish. Please have
a look at the example below.
"""

# My solution:
while True:
    print("hi")
    shall_we = input("Shall we continue?: ")
    if shall_we == "no":
        break
print("okay then")
