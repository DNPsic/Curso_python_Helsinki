"""Please write an improved version of the phone book application.
Each entry should now accommodate multiple phone numbers.
The application should work otherwise exactly as above,
but this time all numbers attached to a name should be
printed."""

# NOTE:
# This exercise explicitly does no require a "if __name__" block.

phone_book: dict = {}


def add_contact(phone_book: dict) -> None:
    name: str = input("name: ")
    num: str = input("number: ")
    if name not in phone_book:
        phone_book[name] = [num]
    else:
        phone_book[name].append(num)
    print("ok!")


# Model's:
# def add(persons):
#     name = input("name: ")
#     number = input("number: ")
#     if name not in persons:
#         persons[name] = []
#     persons[name].append(number)
#     print("ok!")


def search_contact(phone_book: dict) -> None:
    name: str = input("name: ")
    if name not in phone_book:
        print("no number")
    else:
        for contact in range(len(phone_book[name])):
            print(phone_book[name][contact])


# Model's:
# def search(persons):
#     name = input("name: ")
#     if name in persons:
#         for number in persons[name]:
#             print(number)
#     else:
#         print("no number")


def main():
    while True:
        command: str = input("command (1 search, 2 add, 3 quit): ")
        if command == "3":
            print("quitting...")
            break
        elif command == "1":
            search_contact(phone_book=phone_book)
        elif command == "2":
            add_contact(phone_book=phone_book)


main()
