"""Please write a function named longest(strings: list), which
takes a list of strings as its argument. The function finds and
returns the longest string in the list. You may assume there is
always a single longest string in the list."""


def longest(strings: list[str]) -> str:
    longest: str = ""
    for item in strings:
        if len(item) > len(longest):
            longest = item
    return longest


def main():
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
    # Expected: howdydoody


if __name__ == "__main__":
    main()
