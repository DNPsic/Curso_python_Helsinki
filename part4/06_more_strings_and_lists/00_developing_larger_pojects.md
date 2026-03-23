# Developing a larger programming project

This forth part of the course culminates with one larger project
where you must put in practice the knowledge acquired until this
section.

> [!IMPORTANT]
> Resolving larger projects as this is, you should never try to
make a program as a unit at once, you must built it out of smaller
sections such as functions. Every component should be tested.

To try pieces of code outside the main function, is recommended to
define a `main()` function where the final program is structured.
Then you can try any helper function by commenting the `main()`
function and testing the others:

```python

def helper_func():
  """Make some functionality"""
  return result

def main():
  """Here goes the program"""

if __name__ == "__main__":
  #main()
  helper_variables = "Some data"
  helper_func(helper_variables)

```

## Passing data from one function to another

When a program contains multiple functions, the question arises:
how do you pass data from one function to another?

As we can see in the example below, when we give our program its
structure, we pass the data from the functions storing it in variables
which are passed as arguments to the functions that work with that data.
In other words, we *connect* our functions storing the data we need to
make them work properly.

> [!NOTE]
> The way we connect our functions in the `main()` function is achieved with
`return` data from other function and the **parameters** we define thinking
how the functions should communicate.

```python

def input_from_user(how_many: int):
    print(f"Please type in {how_many} numbers:")
    numbers = []

    for i in range(how_many):
        number = int(input(f"Number {i+1}: "))
        numbers.append(number)

    return numbers

def print_result(numbers: list):
    print("The numbers are: ")
    for number in numbers:
        print(number)

def analyze(numbers: list):
    mean = sum(numbers) / len(numbers)
    return f"There are altogether {len(numbers)} numbers, the mean is {mean}, the smallest is {min(numbers)} and the greatest is {max(numbers)}"

# the "main function" using these functions
inputs = input_from_user(5)
print_result(inputs)
analysis_result = analyze(inputs)
print(analysis_result)

```

Using the example above, we can declare explicitly a `main()` function:

```python

def main():
  inputs = input_from_user(5)
  print_result(inputs)
  analysis_result = analyze(inputs)
  print(analysis_result)

if __name__ == "__main__":
  main()

```
