"""Please write a function named factorials(n: int), which returns
the factorials of the numbers 1 to n in a dictionary. The number
is the key, and the factorial of that number is the value mapped
to it.
A reminder: the factorial of the number n is written n! and is
calculated by multiplying the number by each integer smaller
than itself. For example, the factorial of
4 is 4 * 3 * 2 * 1 = 24."""


def factorials(n: int) -> dict:
    fact: dict = {}
    nums: list[int] = [1]
    for x in range(1, n + 1):
        fact[x] = nums[:]
        nums.append(x + 1)
        product: int = 1
        for y in range(len(fact[x])):
            product *= fact[x][y]
        fact[x] = product
    return fact


# Model's
# def factorials(n: int):
#     result = {}
#     result[1] = 1
#     for i in range(2, n + 1):
#         result[i] = result[i-1] * i
#     return result


def main() -> None:
    x: dict = factorials(7)
    print(x)
    print(x[1])
    print(x[3])
    print(x[5])


if __name__ == "__main__":
    main()
