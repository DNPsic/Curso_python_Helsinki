# More functions

<!--toc:start-->
- [More functions](#more-functions)
  - [Learning objectives](#learning-objectives)
  - [Parameters and arguments](#parameters-and-arguments)
  - [Functions calls inside functions](#functions-calls-inside-functions)
  - [Return value of functions](#return-value-of-functions)
    - [Return statement](#return-statement)
    - [Using return values](#using-return-values)
  - [Difference between return and print](#difference-between-return-and-print)
  - [Type of the argument](#type-of-the-argument)
    - [Type hints](#type-hints)
<!--toc:end-->

> [!IMPORTANT]
> From this lesson, the workflow to submit exercises to *test my
code* servers will be done via **Visual Studio Code**. If the lesson
do not explicitly tells to write a function, the special `if main`
block don't has to be included.

## Learning objectives

- Learn more about *parameters* and *arguments* of functions.
- Learn to return values from functions and use them in the code.
- Add type hints for parameters and return values.

## Parameters and arguments

As we saw previously, calling a function allow to pass one or more arguments,
which becomes data assigned to variables internally. In the other hand,
parameters are variables defined in the header of the function when it is
created.

```python
def greet(name): # one parameter
  print("Hello", name)

def sum(num1, num2): # two parameters
  print(f"The sum is: {num1 + num2}.")

greet("Vicente") # one argument
sum(1,2) # two arguments
```

> [!IMPORTANT]
> The parameters behave like any other variable, and can be use inside the function.

## Functions calls inside functions

We've already called functions inside functions like when we use the `print()`
function inside a `def function()` block:

```python
def greet(name:str):
  print("Hello!", name)
```

The functions we write are functionally the same, so we can call them inside:

```python
def greet(name):
    print("Hello there,", name)

def greet_many_times(name, times):
    while times > 0:
        greet(name)
        times -= 1

greet_many_times("Emily", 3)
#Hello there, Emily
#Hello there, Emily
#Hello there, Emily
```

## Return value of functions

Functions can **return** values, this values can be
stored in variables. We've using return values in
some calls to, for example, the `input()` function:

```python
name = input("Type in your name: ")
print(name)
```

In the example above, the function `input` returns a value
of type string, we store it in the `name` variable.

### Return statement

One can determine the `return` value of a function using the
statement:

```python
def my_sum(num1, num2):
  return num1 + num2
```

The `return` statement **finish** the execution of the function.
One example could be a comparison:

```python
def smallest(a, b):
  if a < b:
    return a
  return b
```

If a is smaller than b the function stops immediately, else, it
continues to the next line of code, returning b instead.

> [!IMPORTANT]
> A function **never** can execute two separate `return` statement
in a single call.

A `return` statement can be use even when the function does not
returns any value; this is useful to end the execution:

```python
def greet(name):
    if name == "":
        print("???")
        return
    print("Hello there,", name)
```

If the input is left empty, the function prints "???" and ends
it execution.

### Using return values

The value given by the `return` statement of a function works like
any other value, so it can be use without using variables:

```python
print("The sum is", my_sum(4, 6))
```

> [!NOTE]
> It's not necessary to store a return value in a variable.

This allows using a function call which has a return value to use
as argument in other functions:

```python
def my_sum(a, b):
    return a+b

def difference(a, b):
    return a-b

result = difference(my_sum(5, 2), my_sum(2, 3))
print("The result is", result)
```

The values returned from the function `my_sum()` are resolved
first, its values then are used as arguments to the outside
`difference()` function call. The value from this last function
gets stored in `result` variable.

## Difference between return and print

The fundamental difference of `return` and `print` statements, is
that information printed without without using a return value
**cannot be used** in other way than seeing it printed out. On
the other hand, returning a value allow to **store and use**
this information in the program, such as print, operate, compare,
etc.

## Type of the argument

Recap of data type we've using:

| Type | python data type | Example |
| --------------- | --------------- | --------------- |
| integer | `int` | `23` |
| floating point number | `float` | `5.7` |
| string | `str` | `"Peter Python"` |
| Boolean value | `bool` | `True` |

The arguments of a function use data types of any kind, however, if
the arguments are not of the necessary type in the function call, the
function won't work:

```python
def print_many_times(message, times):
    while times > 0:
        print(message)
        times -= 1

print_many_times("Hello there", "Emily") # The second argument expects an int value

# Output:
# TypeError: '>' not supported between instances of 'str' and 'int'
```

This happens because inside the function definition, the parameter `times` is
compared to an `int` number, this is not possible in python, at least not
this way. To avoid this unexpected behaviour and potential bugs, we can use
what are called **type hints**.

### Type hints

Type hints are very powerful and easy to use hacks, this makes our code more
declarative in means of what kind of data we need in the functions or variable
declarations.

```python
def print_many_times(message : str, times : int):
    while times > 0:
        print(message)
        times -= 1
```

With this modification we are telling the user of this function that, `message`
variable needs data type `str` and `times` needs `int`. This way we can reduce
unexpected behaviour and bugs.

Type hints apply to the return value of the function, we can tell the user the
data type out function returns:

```python
def ask_for_name() -> str:
    name = input("Mikä on nimesi? ")
    return name
```
