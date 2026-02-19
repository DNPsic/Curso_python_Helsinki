"""Please write a program which asks the user to type in a string and a single character.
The program then prints the first three character slice which begins with the character
specified by the user. You may assume the input string is at least three characters long.
The program must print out three characters, or else nothing."""

string_in = input("Please type in a word: ")
character = input("Please type in a character: ")
string_out = ""

if character in string_in:
    index = string_in.find(character)
    if len(string_in) - index > 2:
        while len(string_out) < 3:
            string_out += string_in[index]
            index += 1
        print(string_out)

# Model's solution:
# word = input("Please type in a word: ")
# character = input("Please type in a character: ")
#
# index = word.find(character)
# if index!=-1 and len(word)>=index+3:
#     print(word[index:index+3])
