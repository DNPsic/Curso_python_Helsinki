# Defining functions

## Learning objectives

- Learn how to write and call my own functions.
- Understand what **argument** and **parameter** are in
a function.
- Be able to define parameters in my own functions.

## Definition

A function must be define in order to call it. Every definition
starts with the word `def`, followed by the name itself of the
function, parenthesis and a colon.
What the function actually does needs to be indented.

```python
def name(): # header
  print("My function") # body
```

> [!NOTE]
> The `def` line it's called the **header** of the functions, and
it's content the **body**.

The function only is executed when it's called, otherwise it will
not get executed. To call a function we have to mention its name in
the program.

```python
def name(): # header
  print("My function") # body

name() # calling the function
```

One a function has been defined, it can be called multiple times.
> [!NOTE]
> From this point in the course, the majority of exercises will ask to
write functions.

Python treats the files as a kind of *main function* when they are
executed or evaluated. That's why we need to call our functions, so
python knows what needs to be executed. To achieve this we use a
special `if` block at the end of our program:

```python
def my_function():
  print("Hello from my function!")

if __name__ == "__main__":
  my_function()
```

> [!IMPORTANT]
> In this course no commands should be left in the main function
of your solution, any code —including testing— should be contained
in the special `if` block.

## Function arguments

Functions can take *arguments* to affect it's action. At this point we've
been using arguments in `print` and `input` functions:

```python
name = input("Please give me your name: ") # Displayed text is the parameter.
print(name) # variable name is the parameter for print function.
```

Another concept related to argument is *parameter*. Both are often used as
synonyms, but a distinction can be made: *arguments* are given when the
function *is called*, in the other hand, *parameter* is a variable inside
the function when we *define* it.

```python
def greetings(name): # parameter name.
  print("Hello", name)

if __name__ == "__main__":
  greetings("Vicente") # argument passed to the function.
```

> [!NOTE]
> *Parameters* are defined in the function's header, when the function is
called, the *data* passed becomes the *argument*.

## Using global variables inside functions

> [!WARNING]
> Global variables inside functions can produce bugs hard to track and
fix. This is not recommended.

We can define variables inside a function, but it also can read variables
*outside* its body. This variables which are in the *main* function, are
called **global** variables.

```python
name = "Nube"
def cat_greeet(cat_name):
  print(name, "says Miau to you!") # Using global 'name' variable.

if __name__ == "__main__":
  cat_greeet("Jinja")
# Output:
# Nube says Miau to you!
```

