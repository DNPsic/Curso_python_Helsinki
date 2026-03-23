# More strings and lists

## Learning objectives

- Be familiar with more methods for slicing strings and lists.
- Learn what is **immutability**.
- Use the methods `.count()` and `.replace()`.

## More slices

> [!NOTE]
> The slicing syntax with *step* uses 3 arguments and must have **two colons**:
*[a:b:c]* where *a* is the start, *b* is the exclusive end, and *c* specify
the step.

Slicing strings and indexing lists, as we saw in previous lessons, is
achieved using the `[]` syntax, where we can specify the start and end. This
works just like a range, and of course we can use the *step* argument as well:

```python

my_string = "exemplary"
print(my_string[0:7:2]) # eepa
my_list = [1,2,3,4,5,6,7,8]
print(my_list[6:2:-1]) # [7, 6, 5, 4, 3]

```

> [!NOTE]
> The last argument used in the square brackets is the step, this works only
when 3 arguments are given to the slicing. This is why we have to use the
*colons* to indicate the number or arguments the slicing is receiving.

Omitting the first two arguments —but using the colons— the operator defaults
to «*include everything*», allowing shortcuts to slicing, such as reversing:

```python

my_string = input("Please type in a string: ")
print(my_string[::-1]) # yralpmexe

```

## Strings are immutable

Strings cannot be change, that why if we want to modify a character or a slice,
python will return an error:

```python

my_cat = "Vicentito bebé"
my_cat[0:9] = "Nubesita"
# TypeError: 'str' object does not support item assignment

```

The only way to «*modify*» a string is by replacing it:

```python

greet = "Hello, how r u, i'm under the water"
greet = greet + "Ohhhh!!"
print(greet) # Hello, how r u, i'm under the water Ohhhh!!

```

## More methods for strings and lists

The method `.count()` works with both strings and lists, it —as its name
suggest— counts the *number of times* the specified item or substring
appears:

```python

my_string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
print(my_string.count("ch")) # 5

my_list = [1,2,3,1,4,5,1,6]
print(my_list.count(1)) # 3

```

> [!NOTE]
> The method `.count()` does not count **overlapping** occurrences, specially visible
when working with substrings. For example, in the string `"aaaa"` the `.count("aa")`
counts only two occurrences.

The other method is `.replace()`, which will create a new string by replacing *a*
with *b*: `<string>.replace(a, b)`. Let's see in action:

```python

my_string = "Hi there"
new_string = my_string.replace("Hi", "Hey")
print(new_string) # "Hey there"

```

> [!IMPORTANT]
> The method `.replace()` when used with strings, will replace **all occurrences**
of the specified substring.

```python

sentence = "sheila sells seashells on the seashore"
print(sentence.replace("she", "SHE"))
# Output:
# SHEila sells seaSHElls on the seashore

```

Using the `.replace()` method could lead to unexpected behaviours if we forget
*it creates new string* but does not *modifies it*. To correctly work this way,
we have to remember to store the new string:

```python

my_string = "Python is fun"
# Replaces the substring but doesn't store the result...
my_string.replace("Python", "Java")
print(my_string)
# Python is fun

```

If we don't longer need to use in any way the original string, we can store
the new string in the *same variable*:

```python

my_string = "Python is fun"
# Replaces the substring and stores the result in the same variable
my_string = my_string.replace("Python", "Java")
print(my_string)
# Java is fun

```
