"""Please write a function named dict_of_numbers(), which returns a
new dictionary. The dictionary should have the numbers from 0 to 99
as its keys. The value attached to each key should be the number
spelled out in words."""


def dict_of_numbers() -> dict:
    spelled_out_numbers: dict = {}

    units_list: list = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
    ]
    tens_digits: list[str] = [
        "",
        "teen",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    for x in range(10):
        # print("Now in range of:", tens_digits[x] + "'s")
        for y in range(10):
            number: int = int(f"{x}{y}")
            unit: str = units_list[y]
            tens: str = tens_digits[x]
            name: str = f"{tens + '-' + unit}"
            if tens_digits[x] == "":
                name = unit
            if tens_digits[x] == "teen":
                name = f"{unit}{tens}"
            if tens_digits[x] != "" and unit == "zero":
                name = tens
            spelled_out_numbers[number] = name

    irregular_ones: list[str] = ["eleven", "twelve", "thirteen", "fifteen", "eighteen"]
    spelled_out_numbers[10] = units_list[10]
    spelled_out_numbers[11] = irregular_ones[0]
    spelled_out_numbers[12] = irregular_ones[1]
    spelled_out_numbers[13] = irregular_ones[2]
    spelled_out_numbers[15] = irregular_ones[3]
    spelled_out_numbers[18] = irregular_ones[4]

    # print(f"{number}: {name}")
    # print(spelled_out_numbers)
    return spelled_out_numbers


def main() -> None:
    numbers = dict_of_numbers()
    for number, name in numbers.items():
        print(f"Number: {number} | Name: {name}")


if __name__ == "__main__":
    main()
