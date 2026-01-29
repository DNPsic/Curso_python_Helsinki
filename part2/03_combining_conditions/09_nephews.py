"""Please write a program which asks for the user's name.
If the name is Huey, Dewey or Louie, the program should recognise
the user as one of Donald Duck's nephews.
In a similar fashion, if the name is Morty or Ferdie, the program
should recognise the user as one of Mickey Mouse's nephews."""

# My solution:
name = input("Please type in your name: ")
donald = ["Huey", "Dewey", "Louie"]
mickey = ["Morty", "Ferdie"]
if name in donald:
    print("I think you might be one of Donald Duck's nephews.")
elif name in mickey:
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")

# Model's:
#
# name = input("Please type in your name: ")
#
# if name == "Huey" or name == "Dewey" or name == "Louie":
#     print("I think you might be one of Donald Duck's nephews.")
# elif name == "Morty" or name == "Ferdie":
#     print("I think you might be one of Mickey Mouse's nephews.")
# else:
#     print("You're not a nephew of any character I know of.")
"""The excercise was about combinig conditions, so I give it to
the model's solution
"""
