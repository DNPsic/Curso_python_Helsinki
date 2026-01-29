# Simple loops

<!--toc:start-->
- [Simple loops](#simple-loops)
  - [Exercises of loops](#exercises-of-loops)
  - [Debugging in loops](#debugging-in-loops)
<!--toc:end-->

In this section we will learn what a **loop** is and its relevance in
programming basics. Conditional structures and Loops are called *control
structures* because gives you the possibility to chose which lines of code
are executed when. In the case of loops or *iterations* structures, you
are able to **repeat** sections of the code. The process of repeat once
it's called *an iteration* of the loop.

A simple program using the basic `while` loop looks like this:

```python
while True:
  number = int(input("Please type in a number, -1 to quit: "))

  if number == -1:
    break

  print(number ** 2)

print("Ok, goodbye!")

```

In this simple program, the user inputs a number and gets its squared form.
When the user inputs -1, the condition to execute the `break` command is
met and the loop ends.

## Exercises of loops

[Shall we continue?](./01_shall_we_continue.py)

## Debugging in loops

Using `print` statements inside the programs to obtain certain information
when the code is executing it's crucial. Using loops brings more
complexity to the program's structure. In the following example there's a
simple bug, and using this debugging-in-loops style is helpful.

```python
while True:
    print("beginning of the while block:")
    code = input("Please type in your PIN: ")
    attempts += 1

    print("attempts:", attempts)
    print("condition1:", attempts == 3)
    if attempts == 3:
        success = False
        break

    print("code:", code)
    print("condition2:", code == "1234")
    if code == "1234":
        success = True
        break

    print("Incorrect...try again")

```

The bug can be found in the fact that the third iteration never completes.
If we see what the output is with these debugging print statements, we'll be
able to get the idea:

```txt
beginning of the while block:
Please type in your PIN: 2233
attempts: 1
condition1: False
code: 2233
condition2: False
Incorrect...try again
beginning of the while block:
Please type in your PIN: 4545
attempts: 2
condition1: False
code: 4545
condition2: False
Incorrect...try again
beginning of the while block:
Please type in your PIN: 1234
attempts: 3
condition1: True
```

As we can see, *the order of conditional statements* is a very common
cause of bugs.

## Using `+` to concatenate strings

As we've seen, we can modify a variable reassigning it's value anywhere
in the program. To this point we have been doing this with integers and
booleans:

```python
condition1 = True
value = 0

value += 1
condition1 = False
```

The same thing can be done with strings:

```python
codes = ""
attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1
    codes += code + ", " # increments the code variable
    # ...

```
