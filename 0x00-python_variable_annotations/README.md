At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

Type annotations in Python 3
How you can use type annotations to specify function signatures and variable types
Duck typing
How to validate your code with mypy

0. Basic annotations - add
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.

bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./0-main.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
