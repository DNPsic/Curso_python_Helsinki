"""Please write a program which asks the user for a string and then
prints out a frame of * characters with the word in the centre. The
width of the frame should be 30 characters. You may assume the input
string will always fit inside the frame."""

# My solution:

word = input("Word: ")
format = (28 - len(word)) // 2
aligned = "*" + " " * format + word + " " * format + "*"
if len(aligned) < 30:
    aligned = "* " + " " * format + word + " " * format + "*"
    # print("String is less than 30")
# print("String lenght: ", len(word))
# print(28, "-", len(word), "/ 2", "=", format)
print("*" * 30)
print(aligned)
print("*" * 30)

# Model's solution:
# word = input("Word: ")
#
# print("*" * 30)
# spaces_at_start = (28 - len(word)) // 2
# spaces_at_end = spaces_at_start
#
# # If the word length is odd, one is added to the spaces at the end of the word
# # to get all 30 characters filled
# if len(word) % 2 != 0:
#     spaces_at_end += 1
#
# print("*" + spaces_at_start * " " + word + spaces_at_end * " " + "*")
# print("*" * 30)
