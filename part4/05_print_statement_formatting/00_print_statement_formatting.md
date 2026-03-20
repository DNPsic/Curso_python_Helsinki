# Print statement formatting

<!--toc:start-->
- [Print statement formatting](#print-statement-formatting)
  - [Learning objectives](#learning-objectives)
  - [Introduction](#introduction)
  - [F-strings](#f-strings)
    - [Floating point numbers](#floating-point-numbers)
    - [White spaces](#white-spaces)
<!--toc:end-->

## Learning objectives

- Learn how to use arguments to format the results of the `print()` command.
- Be able to use **f-strings** to format printouts.

## Introduction

We've already seen a printing argument, the `sep=` *keyword* argument. It
stablish what character has to be use as separator for the other arguments
in that printing statement. It can be any string, as we saw with the
empty `sep=""` or the special `sep="\n"`.

## F-strings

The other method to format strings when we print information with `print()` can
be the **f-strings**. This method is more flexible and has a lot of uses.

### Floating point numbers

F-strings allow us to display numbers with specific values after a floating point.
To achieve this we need to use special formatting syntax:

```python

number:float = 1/3
print(f"The number is: {number}") # The number is: 0.3333333
# Applying the special syntax:
print(f"The number is: {number:.2f}") # The number is: 0.33

```

This special syntax stands for *display n decimals as float number*.

### White spaces

We also can specify any amount of white spaces for the variable in the
printouts. This is very handy to arrange and prettify the outputs.

```python

names:list[str] = ["Jane", "Dany", "Jinja", "Pedro"]
for n in names:
  print(f"{name:15} centre {name:>15}")
# Output:
# Jane           centre           Jane
# Dany           centre           Dany
# Jinja          centre          Jinja
# Pedro          centre          Pedro

```

Lastly a reminder: f-strings are not restricted to print commands, they
can be store in variables and get combined with other strings.

```python

name = "Larry"
age = 48
city = "Palo Alto"
greeting = f"Hi {name}, you are {age} years of age"
print(greeting + f", and you live in {city}")
# Output:
# Hi Larry, you are 48 years of age, and you live in Palo Alto

```
