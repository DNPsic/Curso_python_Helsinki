# Definite iteration

<!--toc:start-->
- [Definite iteration](#definite-iteration)
  - [Learning objectives](#learning-objectives)
  - [Introduction](#introduction)
  - [The for loop](#the-for-loop)
  - [The function range](#the-function-range)
  - [From a range to a list](#from-a-range-to-a-list)
  - [Finding the best or worst item](#finding-the-best-or-worst-item)
<!--toc:end-->

## Learning objectives

- Learn the difference between definite and indefinite iteration.
- Learn how a Python `for` loop  works (dunno what this is lol).
- Be able to use a `for` loop to iterate through lists and strings.

## Introduction

We've been using the `while` loop to iterate over lists and strings.
Other way to achieve this functionality is using the more intuitive
way: the `for` loop.

## The for loop

The `while` loop falls when the condition to break out of it is not
set correctly and it goes on and on indefinite times till we end its
execution by brute forcing the program —for example using `<Ctrl-c>`
on the console. This happens because the loop *does not know how many
iterations* needs to execute, it needs a condition to finalize and
break out. This is what is called a **indefinite iteration**.

In the other hand we have the `for` loop, which iterations are set up
by the *collection* we are looping over: it's determined when the loop
is set up. This is what we call a **definite iteration**.

> [!NOTE]
> We don't have to worry which item is been handled when, the `for` loop
guaranties to perform the *same actions on the same items* a limited
times.

The syntax is the following:

```python

for <item> in <collection>:
  <block>

```

The loop works this way:

1. First, takes an item in the collection and assigns it to the `variable`.
2. Second, process the `block` of code.
3. Last, goes to the next item and repeats 1 and 2.

One there are no items to process, the loop ends automatically and the program
continues.

A simple example of a program that prints the items of a list:

```python

numbers : int = [1, 2, 3, 4, 5]
for number in numbers:
  print(number) # 1\n 2\n 3\n ...

 ```

## The function range

The combination of `range()` function and `for` loop allow us to
repeat certain bit of code the number of times we specify. The
simplest way to call this function is with one argument which
specifies the *end point* of the range. The end point is excluded
like the string slices we saw in past lessons.

> [!NOTE]
> The `range()` function first argument is exclusive, which means
the real range of any given end point *n*  `range(n)` is read as
*zero to n -1*.

```python

for x in range(10):
  print(x) # 0\n 1\n 2\n ... 9

```

When we specify **two arguments**  to `range()` it will return a range
between the two numbers excluding the second:

```python

for i in range(2, 7):
  print(i) # 2\n 3\n ... 6

```

And finally with **three arguments** we can specify the *step* of
the range between each value. Calling the function as
`range(a, b, c)` will return a range starting at *a*, ending
in *b -1*, taking a step of *c*:

```python

for i in range(1, 11, 2):
  print(i)
# Output:
# 1
# 3
# 5
# 7
# 9

```

The value of the step argument can be negative, which will
reverse the range. To achieve this, the start and end parameters
has to be flipped as well:

```python

for i in range(9, 2, -1):
  print(i) # 9\n 8\n ... 3

```

> [!IMPORTANT]
> Reversing a range with a negative value as the step parameter
is still exclusive, the end point value wont be part of it.

## From a range to a list

The function `range()` returns a *range object* which is similar to
a list, but if we try to print the return value we will see the
information of the object itself:

```python

numbers = range(2, 6)
print(numbers) # range(2, 6)

```

We can use the function `list()` to automatically convert this
range object into a list:

```python

numbers = list(range(2, 7))
print(numbers) # [2, 3, 4, 5, 6]

```

## Finding the best or worst item

A very common programming task is *finding the best or worst item in a list*,
according to some criteria. A simple solution is using a helper variable to
"remember" which of the items processed so far was the most suitable. This
temporary best choice is then compared to each item in turn, and at the end
of the iteration the variable contains the best of the bunch.

A placeholder program looks like this but with real conditions:

```python

best = initial_value # The initial value depends on the situation
for item in my_list:
    if item is <condition>: # better than best
        best = item

```
