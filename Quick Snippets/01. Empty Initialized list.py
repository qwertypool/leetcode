You cannot assign to a list like lst[i] = something,
unless the list already is initialized with at least i+1 elements.
You need to use append to add elements to the end of the list. lst.append(something).

(You could use the assignment notation if you were using a dictionary).

Creating an empty list:

>>> l = [None] * 10
>>> l
[None, None, None, None, None, None, None, None, None, None]
Assigning a value to an existing element of the above list:

>>> l[1] = 5
>>> l
[None, 5, None, None, None, None, None, None, None, None]
Keep in mind that something like l[15] = 5 would still fail, as our list has only 10 elements.

range(x) creates a list from [0, 1, 2, ... x-1]

# 2.X only. Use list(range(10)) in 3.X.
>>> l = range(10)
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Using a function to create a list:
  >>> def display():
...     s1 = []
...     for i in range(9): # This is just to tell you how to create a list.
...         s1.append(i)
...     return s1
... 
>>> print display()
[0, 1, 2, 3, 4, 5, 6, 7, 8]
List comprehension (Using the squares because for range you don't need to do all this, you can just return range(0,9) ):

>>> def display():
...     return [x**2 for x in range(9)]
... 
>>> print display()
[0, 1, 4, 9, 16, 25, 36, 49, 64]
