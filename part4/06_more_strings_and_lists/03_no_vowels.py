"""Please write a function named no_vowels, which takes
a string argument. The function returns a new string,
which should be the same as the original but with all
vowels removed."""


def no_vowels(word: str) -> str:
    vowels: str = "aeiou"
    for char in word:
        if char in vowels:
            word = word.replace(char, "")
    return word


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
    print(no_vowels("Gatito bebesito bonito que se llama Vicentito UwU"))
