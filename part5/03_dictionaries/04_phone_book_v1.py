"""Please write a phone book application. It should work as follows:
Sample output
command (1 search, 2 add, 3 quit): 2
name: peter
number: 040-5466745
ok!"""

# NOTE:
# This exercise explicitly does no require a "if __name__" block.

phone_book: dict = {}


def add_contact(phone_book: dict) -> None:
    name: str = input("name: ")
    num: str = input("number: ")
    # if name not in phone_book:
    #     phone_book[name] = num
    phone_book[name] = num
    print("ok!")


def search_contact(phone_book: dict) -> None:
    name: str = input("name: ")
    if name not in phone_book:
        print("no number")
    else:
        print(phone_book[name])


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
