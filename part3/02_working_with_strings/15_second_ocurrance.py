"""Please write a program which finds the second occurrence of a substring.
If there is no second (or first) occurrence, the program should print out
a message accordingly."""

# TODO break loop when substring occur once

word = input("Word: ")
substring = input("Search: ")
position = word.find(substring)
index = 0
found = 0

if position != -1:  # substring exists in string
    sliced_word = word[position + len(substring) :]
    position_2 = sliced_word.find(substring)
    if position_2 != -1:  # substring exists in the sliced word
        while index <= index + len(substring):
            if substring == word[index : index + len(substring)]:
                # print(">", word[index : index + len(substring)], index)
                found += 1
                if found >= 2:
                    print(
                        f"The second occurrence of the substring is at index {index}."
                    )
                    break
                index += len(substring)
            else:
                index += 1
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")

# Model's soulution
# string = input("Please type in a string: ")
# substring = input("Please type in a substring: ")
#
# index1 = string.find(substring)
# index2 = -1
# if index1 != -1:
#     string = string[index1+len(substring):]
#     index2 = string.find(substring)
#
# if index2 == -1:
#     print("The substring does not occur twice in the string.")
# else:
#     print("The second occurrence of the substring is at index " + str(index1+len(substring)+index2) +  ".")
#
