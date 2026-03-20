"""Please write a program which asks the user which editor they are using.
The program should keep on asking until the user types in Visual Studio Code."""

while True:
    answer = input("Editor: ").lower()
    if answer == "visual studio code":
        print("an excellent choice!")
        break
    if answer == "emacs" or answer == "vim":
        print("not good")
        continue
    if answer == "word" or answer == "notepad" or answer == "atom":
        print("awful")
        continue

# # Model's solution
# while True:
#     editor = input("Editor: ").lower()
#     if editor == "visual studio code":
#         break
#     if editor == "word" or editor == "notepad":
#         print("awful")
#     else:
#         print("not good")
# print("an excellent choice!")
