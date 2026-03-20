"""Please write a function named `all_the_longest`, which
takes a list of strings as its argument. The function
should return a new list containing the longest string
in the original list. If more than one are equally long,
the function should return all of the longest strings.
The order of the strings in the returned list should be
the same as in the original."""


def all_the_longest(words: list[str]) -> list[str]:
    longest: list[str] = []
    max_value: int = 0
    for w in words:
        if len(w) > max_value:
            max_value = len(w)
    for w in words:
        if len(w) >= max_value:
            longest.append(w)
    return longest


# Model's solution
# def all_the_longest(names: list):
#     result = []
#
#     for name in names:
#         if result == [] or len(name) > len(result[0]):
#             result = [name]
#         elif len(name) == len(result[0]):
#             result.append(name)
#
#     return result

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)  # ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)  # ['dorothy', 'richard']
