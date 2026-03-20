"""Please write a function named palindromes, which
takes a string argument and returns True if the string
is a palindrome. Palindromes are words which are spelled
exactly the same backwards and forwards."""


def palindromes(word: str) -> bool:
    reversed: str = word[::-1]
    return word == reversed


while True:
    palindrome: str = input("Please type in a palindrome: ")
    if not palindromes(palindrome):
        print("that wasn't a palindrome")
        continue
    else:
        print(f"{palindrome} is a palindrome!")
        break


if __name__ == "__main__":
    print(palindromes("python"))
    print(palindromes("neveroddoreven"))
