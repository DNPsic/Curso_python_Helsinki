# Dictionaries

<!--toc:start-->
- [Dictionaries](#dictionaries)
  - [Learning objectives](#learning-objectives)
  - [Introduction](#introduction)
  - [Using a dictionary](#using-a-dictionary)
  - [About keys and values](#about-keys-and-values)
  - [Traversing a dictionary](#traversing-a-dictionary)
  - [Advanced dictionaries](#advanced-dictionaries)
<!--toc:end-->

## Learning objectives

- Familiarize with the **dictionary** data structure.
- Learn how to use a dictionary with different types
of *keys* and *values*.
- Learn how to traverse through the contents of a
dictionary.
- Be able to name some typical use cases for dictionaries.

## Introduction

The **dictionary** data type in python indexes items by **keys**, which points to
the **values**. With a dictionary we can access and change items by knowing
its key.

## Using a dictionary

Here is a simple dictionary from Finnish to English:

```python

my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"
print(len(my_dictionary))
print(my_dictionary)
print(my_dictionary["apina"])

# Output:
# 3
# {'apina': 'monkey', 'banaani': 'banana', 'cembalo': 'harpsichord'}
# monkey

```

The notation `{}` creates an empty dictionary,
to which we can now add content. Three key-value pairs
are added:"apina" maps to "monkey", "banaani"
maps to "banana", and "cembalo" maps to "harpsichord".
Finally, the number of key-value pairs in the dictionary
is printed, along with the entire dictionary,
and the value mapped to the key "apina".

We can use the `input()` and logic operators with dictionaries:

```python

word = input("Please type in a word: ")
if word in my_dictionary:
    print("Translation: ", my_dictionary[word])
else:
    print("Word not found")

```

Using the `in` operator with dictionaries what happens is, first,
it searches the *key*: `if <key> in <dictionary>`.

> [!NOTE]
> A dictionary can store many data types, but  not only as
> values, the keys also can be a variety of data types.

```python

# Different data types as keys and values.
es_en: dict = {}
es_en["Gatito"] = "Kitty"
es_en["Nube"] = "Cloud"

num_name: dict = {}
num_name[98] = "Ninety eight"
num_name[69] = "Nice ;p"

int_list: dict = {}
int_list[0] = ["zero","cero"]
int_list[1] 0 ["one", "uno"]

```

## About keys and values

> [!IMPORTANT]
> Each key can appear **only once**  in the dictionary.
> If you add an entry using a key that already exists in the
> dictionary, the original value mapped to that key is
> replaced with the new value.

```python

my_dictionary["suuri"] = "big"
my_dictionary["suuri"] = "large"
print(my_dictionary["suuri"]) # large

```

> [!IMPORTANT]
> All the keys in a dictionary must be of type ***immutable***,
> which means a **list** cannot be a key.

Unlike keys as we just saw, the values of a dictionary *can change*,
which means any type of data is acceptable as a value. A value can also be mapped
to more than one key in the same dictionary.

## Traversing a dictionary

When a `for` loop is used with dictionaries, it iterates through all the keys stored.
We can print the keys and values with this method:

```python

my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

for key in my_dictionary:
    print("key:", key)
    print("value:", my_dictionary[key])

```

There is the dictionary method `.items()` which return all values and keys,
one pair at a time:

```python

for key, value in my_dictionary.items():
    print("key:", key)
    print("value:", value)

```

## Advanced dictionaries

We can use dictionaries for several things, it's very useful to manage certain
types of information;
for example, counting and classification:

```python
# Counting words in a list of strings
word_list: list[str] = ["michi", "gatito", "nubecita", "michi", "nubecita"]

def counts(my_list):
    words = {}
    for word in my_list:
        # if the word is not yet in the dictionary, initialize the value to zero
        if word not in words:
            words[word] = 0
        # increment the value
        words[word] += 1
    return words

# call the function
print(counts(word_list))

# Classification of words by initials
word_list: list[str] = ["michi", "gatito", "nubecita", "michi", "nubecita"]

def categorize_by_initial(my_list):
    groups = {}
    for word in my_list:
        initial = word[0]
        # initialize a new list when the letter is first encountered
        if initial not in groups:
            groups[initial] = []
        # add the word to the appropriate list
        groups[initial].append(word)
    return groups

groups = categorize_by_initial(word_list)

for key, value in groups.items():
    print(f"words beginning with {key}:")
    for word in value:
        print(word)

```

## Removing keys and values from dictionaries

There are two ways to remove key-value pairs in dictionaries.
One is the command `del`:

```python

staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
del staff["David"]
print(staff)
# {'Alan': 'lecturer', 'Emily': 'professor'}


```

> [!NOTE]
> Trying to delete a key which does not exist will cause an error.
> A good practice would be to check first if it exists.

Checking if a key exists in a dictionary:

```python

staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
if "Paul" in staff:
  del staff["Paul"]
  print("Deleted")
else:
  print("This person is not a staff member")

```

The other way to delete an entry in the dictionary is via `.pop()` method:

```python

staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
deleted = staff.pop("David")
print(staff)
print(deleted, "deleted")
# {'Alan': 'lecturer', 'Emily': 'professor'}
# lecturer deleted

```

> [!NOTE]
> The `.pop()` method **returns** the value of the **deleted entry**.
> This method also cause an error trying to remove a nonexistent entry.

The `.pop()` method can receive a second argument which contains a default
return value. This value is returned in case the key is not found in the dictionary.

```python

staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
deleted = staff.pop("Paul", None)
if deleted == None:
  print("This person is not a staff member")
else:
  print(deleted, "deleted")
# This person is not a staff member

```

### Deleting entire dictionary

> [!NOTE]
> Why would I try to erase an entire dictionary? I don't know. But in the case
> it is needed, trying to do so with a for loop will result in an error.

```python

staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
for key in staff:
  del staff[key]

# Output error:
# RuntimeError: dictionary changed size during iteration

```

To achieve this, the method `.clear()` will do.

## Structured data with dictionaries

If you are working with data than can or need to be organized, dictionaries may
be the best option in python. Here is an example of a person:

```python

person = {"name": "Pippa Python", "height": 154, "weight": 61, "age": 44}

```

This means that we have here a person named Pippa Python, whose height is 154,
weight 61, and age 44. The same information could just as well be stored in
variables:

```python

name = "Pippa Python"
height = 154
weight = 61
age = 44

```

Why don't use lists instead of dictionaries? In lists there is no easy way to
know exactly where is what. On a dictionary this problem is avoided
as each bit of data is accessed through a named key.

Assuming we have defined multiple people using the same format, we can access
their data in the following manner:

```python

person1 = {"name": "Pippa Python", "height": 154, "weight": 61, "age": 44}
person2 = {"name": "Peter Pythons", "height": 174, "weight": 103, "age": 31}
person3 = {"name": "Pedro Python", "height": 191, "weight": 71, "age": 14}

people = [person1, person2, person3]

for person in people:
    print(person["name"])

combined_height = 0
for person in people:
    combined_height += person["height"]

print("The average height is", combined_height / len(people))

```
