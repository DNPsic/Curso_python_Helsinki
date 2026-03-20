"""Please write a function named most_common_character,
which takes a string argument. The function returns the
character which has the most occurrences within the string.
If there are many characters with equally many occurrences,
the one which appears first in the string should be returned."""


def most_common_character(string: str) -> str:
    count: int = 0
    character: str = ""
    for char in string:
        times = string.count(char)
        if times > count:
            count = times
            character = char
    # return f"Character: {character}\nTimes: {count}"
    return character


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
    # most_common_character(first_string)

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
    # most_common_character(second_string)

    third_string = "Vicentico"
    print(most_common_character(third_string))
