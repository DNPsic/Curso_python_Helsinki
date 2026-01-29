# Loops with conditions

<!--toc:start-->
- [Loops with conditions](#loops-with-conditions)
  - [Learning objectives](#learning-objectives)
  - [Forewords of this chapter](#forewords-of-this-chapter)
  - [Introduction](#introduction)
  - [Initialisation, condition and update](#initialisation-condition-and-update)
<!--toc:end-->

## Learning objectives

- Create a `while` loop with conditions.
- Learn what initialisation, condition and updating variables are.
- Create loops with different kind of conditions.

## Forewords of this chapter

Becoming a proficient programmer requires a lot of practice, sometimes even
quite mechanical practice. It also involves developing problem solving skills
and applying intuition. This is why there are a lot of exercises of different
kinds on this course. Some of them ask you to quite straightforwardly apply
what you have learnt in the material, but some of them are intentionally more
challenging and open-ended.

## Introduction

In the previous section we learnt to use the while True loop to repeat sections
of code. In that construction the condition of the loop is True, so the condition
is fulfilled every time. We needed to explicitly break out from the loop each time
to avoid an infinite loop. For example:

```python
# Print numbers until the variable a equals 5
a = 1
while True:
    print(a)
    a += 1
    if a == 5:
        break

```

What we'll see in this chapter is, essentially, that the condition *not always has
to be True*. The general structure of the while statement is as follows:

```python
while condition:
  block
```

Now, the program will execute the block if the condition is true. When the condition
turns false, the loop ends, and the program continues outside the block. For example:

```python
number = int(input("Please type in a number: "))

while number < 10:
    print(number)
    number += 1

print("Execution finished.")
```

This program ask for a number, if the condition `while number < 10`  the block will
continue it's execution until the condition is no longer met.

## Initialisation, condition and update

Creating a loop requires **three steps**: Initialisation, condition and updating
the iteration variables.

**Initialisation** refers to setting the initial value(s) of the variable(s) used
within the condition of the loop. These are often called the iteration or iterator
variables. This is performed before the loop is first entered.
The **Condition** defines for how long the loop is to be executed. It is set out
at the very beginning of the loop.
Finally, within each repetition of the loop the variables involved in the condition
are updated, so that each iteration brings the loop one step closer to its
conclusion.

> [!CAUTION]
> A typical error is omitting the **update** variable, causing an *infinite  loop*
which has to be cancel manually, often with the command `<Control + C>`.

One can combine any type of condition, for example a boolean, which will be
the criteria to execute and finish the loop:

```python
number = int(input("Please type in a number: "))

while number < 100 and number % 5 != 0:
    print(number)
    number += 3

```

> [!IMPORTANT]
> Whenever you write a loop you should make sure that the execution of the loop
will always end at some point.
