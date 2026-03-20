"""Please write a function named length_of_longest, which
takes a list of strings as its argument. The function
returns the length of the longest string."""


def length_of_longest(words: list[str]) -> int:
    longest: int = 0
    for w in words:
        if len(w) > longest:
            longest = len(w)
    return longest


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)
