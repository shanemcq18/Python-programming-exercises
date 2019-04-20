# 100+ Python Programming Exercises

Adapted from [https://github.com/zhiwehu/Python-programming-exercises](https://github.com/zhiwehu/Python-programming-exercises).
Exercises have been updated to Python 3 and expanded.

The exercises are groupded into the following difficulty levels.

- **Beginner.**
For someone who has just gone through an introductory Python course.
He or she can solve some problems with 1 or 2 Python classes or functions.
Normally, the answers could directly be found in the textbooks.

- **Intermediate.**
For someone who has just learned Python, but already has a relatively strong programming background from before.
He or she should be able to solve problems which may involve 3 or 4 Python classes or functions.
The answers cannot be directly be found in the textbooks.

- **Advanced**.
For someone who has been using Python for some time.
He or she should use Python to solve more complex problem using more rich libraries functions and data structures and algorithms.
He or she should solve the problem using several Python standard packages and advanced techniques.

## Beginner Exercises

#### Exercise 1

Write a function that accepts integers `a`, `b`, `c`, and `d`.
Return the list of all integers `n` between `a` and `b` (inclusive) which are divisible by `c` but not by `d`.
Use your function to find integers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (inclusive).
Print the results in a comma-separated sequence on a single line.

_Hint_: Consider using the built-in `range()` function.

```python
def multiple_range(a, b, c, d) -> list:
    """Return the list of integers n with a ≤ n ≤ b, where n is divisible by c
    but not by b.
    """
    # Brute force option: check each number between a and b inclusive.
    return [i for i in range(a, b+1) if not i%c and i%d]

    # Better option: generate all multiples of c and filter out multiples of 5.
    return [n*7 for n in range(a//c +1, (b+1)//c +1) if n%d]

# Find integers between 2000 and 3200 which are divisible by 7 but not 5.
print('.'.join([n for n in multiple_range(2000, 3200, 7, 5)]))
```

#### Exercise 2

Write a function which computes the factorial of a given integer.
Use your function to find 14!.

_Hint_: make the function recursive.

```python
# Non-recursive solution: multiply 1 through n.
def factorial_iter(n) -> int:
    """Compute n!, the factorial of the integer n (iteratively)."""
    product = 1
    for i in range(2, n+1):
        product *= i
    return product

# Recursive solution. Base cases is 0! = 1.
def factorial(n) -> int:
    """Compute n!, the factorial of the integer n (recursively)."""
    return 1 if n == 0 else n * factorial(n - 1)

# Find 14!.
print(factorial(14))
```

#### Exercise 3

Write a function that accepts an integer `n`.
Return the dictionary containing key-value pairs `(i, i*i)` for all integers `1 ≤ i ≤ n`.
For example, `n = 8` should result in the dictionary
`{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}`.

```python
def squares_dict(n) -> dict:
    """Return the dictionary containing key-value pairs (i, i*i) for all
    integers 1 ≤ i ≤ n.
    """
    return {i:i**2 for i in range(1, n+1)}

squares_dict(8)
```

#### Exercise 4

Write a program which accepts a comma-separated sequence from the console.
Generate a list and a tuple which contains every sequence element.
For example, if the user types `34,67,55,33,12,98`, the output should be
```
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
```
_Hint_: use the built-in function `input()` to read console input from the user.

```python
values_list = input().split(',')
print(values_list)
print(tuple(values_list))
```

#### Exercise 5

Define a class with the following methods:

- `get_string()`: read a string from console input.
- `print_string()`: print the string in upper case.

Also include simple functions to test each class method.

```python
class InputOutString:
    """Simple class for reading console output and shouting it back."""
    def __init__(self):
        """Initialize `s`, the string attribute."""
        self.s = ""

    def get_string(self):
        """Read a string from console input."""
        self.s = input()

    def print_string(self):
        """Print the stored string in upper case."""
        print(self.s.upper())

def test_getter():
    ios = InputOutString()
    ios.getString()
    print(ios.s)                # Should be the same as the user input.

def test_printer():
    ios = InputOutString()
    ios.s = "hello, world!"
    ios.print_string()          # Should be "HELLO, WORLD!"
```

## Intermediate Exercises

#### Exercise 6

Write a function that accepts a list `D` of numbers and two numbers `C` and `H`.
For each value `d` in the list `D`, calculate `Q = Square root of [(2 * C * d)/H]`.
Set the default values of `C` and `H` to 50 and 30, respectively.
Round each output to the nearest integer and return the reslts as a list.

For example, if `D = [100, 150, 180]`, then the output (with the default values for `C` and `H`) should be `[18, 22, 24]`.

```python
from math import sqrt

def formula(D, C=50, H=30):
    return [int(round(sqrt(2*C*d/H))) for d in D]

formula([100, 150, 180])
```

#### Exercise 7

Write a function which accepts 2 integers `X`, `Y`.
Generates a 2-dimensional array with `X` rows and `Y` columns as a list of lists, where the element value in the `i`th row and `j`th column of the array is `i*j`, with `0 ≤ i ≤ X` and `0 ≤ j ≤ Y`.

For example, `X=3` and `Y=5` should result in the following array.
```python
[[0, 0, 0, 0, 0],
 [0, 1, 2, 3, 4],
 [0, 2, 4, 6, 8]]
```

```python
def grid_maker(X, Y):
    return [[i*j for j in range(Y)] for i in range(X)]

grid_maker(3, 5)
```

#### Exercise 8

Write a program that receives a comma-separated sequence of strings from the console, sorts the sequence alphabetically, and prints it again as a comma-separated sequence.

For example, the input `without,hello,bag,world` should result in `bag,hello,without,world` being printed.

```python
print(sorted(input().split(',')))
```

#### Exercise 9

Write a program that continually accepts lines of input from the console until encountering the input `STOP`.
Capitalize all of the inputs and join them into a single space-separated string.
Print the string.

For example, the input
```
Hello
World
Practice
makes
perfect
STOP
```
should result in the output `HELLO WORLD PRACTICE MAKES PERFECT STOP`.

```python
lines = []
While True:
    s = input()
    lines.append(s.upper())
    if s == "STOP":
        break

print(' '.join(lines))
```

#### Exercise 10

Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

_Hint_: case a sequence as a `set()` to remove duplicated data; use `sorted()` to create a new list of sorted data from a sequence.

```python
print(" ".join(sorted(set(input().split()))))
```

#### Exercise 11

Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

```python
value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))
```

#### Exercise 12

Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

```python
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))
```

#### Exercise 13

Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

```python
s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])
```

#### Exercise 14

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

```python
s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])
```

#### Exercise 15

Write a function that accepts two positive integers `a` and `n`.
Compute the value of `a` + `aa` + `aaa` + ... + `aaaaaaa` (n times), where `aa` indicates the two-digit number with both digits `a`, and so on.

For example, with `a=1` and `n=3`, the task is to compute `1 + 11 + 111 = 123`.

```python
def sum_repeat(a, n):
    sa = str(a)
    return sum(int(k*sa) for n in range(1,n+1))
```

#### Exercise 16
<!-- List Comprehension -->

Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
`1,2,3,4,5,6,7,8,9`
Then, the output should be:
`1,3,5,7,9`

```python
print(",".join([x for x in input().split(",") if int(x) % 2 != 0]))
```

#### Exercise 17

Consider a bank account with a transaction log from console output.
Transactions are listed as `D 100` or `W 200`, where `D` means deposit and `W` means withdrawal.
Write a function that accepts a starting balance, defaulting to zero, then continually reads transactions from the console until the input `STOP` is received.
If an invalid transaction (other than `STOP`) is provided, do nothing to the balance but do not terminate the program.
Note that any transaction that would create a negative balance is invalid.
After the `STOP` signal, return the end balance.

For example, the inputs
```
D 300
D 300
W 200
D 100
STOP
```
should result in an output of `500`.

```python
def transactions(starting_balance=0):
    balance = starting_balance
    while True:
        line = input().split()
        if len(line) != 2:
            if line[0] == "STOP":
                break
            continue
        dw, amount = line[0], int(line[1])
        if dw == "D":
            balance += amount
        elif dw == "W" and amount < balance:
            balance -= amount
    return balance
```

## Advanced Exercises

#### Exercise 18

A website requires the users to create a username and password to register.
The password must satisfy the following criteria:

1. Contains at least 1 lowercase letter
2. Contains at least 1 uppercase letter
3. Contains at least 1 number
4. Contains at least 1 special character (one of `!@#$%^&*()`)
5. Contains at least 6 characters
6. No more than 12 characters

Write a function that accepts a potential password and returns True if and only if is valid as a password.

```python
import re

def valid_password(word):
    n = len(word)
    if n < 6 or n > 12:
        return False
    elif not re.search(r"[a-z]", word):
        return False
    elif not re.search(r"[A-Z]", word):
        return False
    elif not re.search(r"[0-9]", word):
        return False
    elif not re.search(r"[!@#\$%\^&\*\(\)]", word):
        return False
    return True
```

#### Exercise 19

You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
```
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
```
Then, the output of the program should be:
```
[('John', '20', '90'),
 ('Jony', '17', '91'),
 ('Jony', '17', '93'),
 ('Json', '21', '85'),
 ('Tom', '19', '80')]
 ```

_Hint_: We use itemgetter to enable multiple sort keys.

```python
from operator import itemgetter, attrgetter

l = []
While True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(0,1,2)))
```

#### Exercise 20

Write a generator that yields the positive integers less than a given integer `n` which are divisible by a given integer `d`.
Use your generator to get the multiples of 7 that are less than 100.

```python
def multiples(d, n=100):
    i = d
    while i < n:
        yield i
        i += d

", ".join([str(n) for n in multiples(7, 100)])
```

#### Exercise 21

A robot moves in a plane starting from the origin (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
STOP­
The numbers after the direction are steps.
Write a program to compute the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.

Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

```python
import math
pos = [0,0]
While True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
```

#### Exercise 22

Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
`New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3`.
Then, the output should be:
```
2: 2
3.: 1
3?: 1
New: 1
Python: 5
Read: 1
and: 1
between: 1
choosing: 1
or: 2
to: 1
```

```python
freq = {}   # frequency of words in text
line = input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

Words = freq.keys()
Words.sort()

for w in words:
    print(f"{w}:{freq[w]}")
```

#### Exercise ?? (Strings and Numbers)

Define a function that can receives two numbers as strings and returns their sum as a string.
For example, the inputs `"12"` and `"3"` should give the output `"15"`.

Next, write a function that accepts two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print al l strings line by line.

```python
def add_strings(s1, s2):
    return int(s1) + int(s2)

def print_longer(s1,s2):
    s1l, s2l = len(s1), len(s2)
    print(s1 if s1l > s2l else s2 if s1l < s2l else f"{s1}\n{s2}")
```

#### Exercise ??

Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

_Hint_:
Use % operator to check if a number is even or odd.

```python
def checkValue(n):
    if n%2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")

checkValue(7)
```

#### Exercise ??

Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

_Hint_:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.

```python
def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    print(d)

printDict()
```

#### Exercise ??

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

_Hint_:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

```python
def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for (k,v) in d.items():
        print(v)

printDict()
```

#### Exercise ??

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

_Hint_:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

```python
def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for k in d.keys():
        print(k)

printDict()
```

#### Exercise ??

Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

_Hint_:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.

```python
def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li)

printList()
```

#### Exercise ??

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

_Hint_:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

```python
def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li[:5])

printList()
```

#### Exercise ??

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

_Hint_:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

```python
def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li[-5:])

printList()
```

#### Exercise ??

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

_Hint_:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

```python
def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li[5:])

printList()
```

#### Exercise ??

Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

_Hint_:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use tuple() to get a tuple from a list.

```python
def printTuple():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(tuple(li))

printTuple()
```

#### Exercise ??

With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

_Hint_:
Use [n1:n2] notation to get a slice from a tuple.

```python
tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print(tp1)
print(tp2)
```

#### Exercise ??

Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

_Hint_:
Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.

```python
tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
    if tp[i]%2==0:
        li.append(tp[i])

tp2=tuple(li)
print(tp2)
```

#### Exercise ??

Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

_Hint_:
Use if statement to judge condition.

```python
s= input()
if s=="yes" or s=="YES" or s=="Yes":
    print("Yes")
else:
    print("No")
```

#### Exercise ??

Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

_Hint_:
Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.

```python
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print(evenNumbers)
```

#### Exercise ??

Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

_Hint_:
Use map() to generate a list.
Use lambda to define anonymous functions.

```python
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print(squaredNumbers)
```

#### Exercise ??

Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

_Hint_:
Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.

```python
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print(evenNumbers)
```

#### Exercise ??

Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

_Hint_:
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.

```python
evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(evenNumbers)
```

#### Exercise ??

Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

_Hint_:
Use map() to generate a list.
Use lambda to define anonymous functions.

```python
squaredNumbers = map(lambda x: x**2, range(1,21))
print(squaredNumbers)
```

#### Exercise ??

Define a class named American which has a static method called printNationality.

_Hint_:
Use @staticmethod decorator to define class static method.

```python
class American(object):
    @staticmethod
    def printNationality():
        print("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()
```

#### Exercise ??

Define a class named American and its subclass NewYorker.

_Hint_:
Use class Subclass(ParentClass) to define a subclass.

```python
class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)
```

#### Exercise ?? (OOP)

Define a `Circle` class which can be constructed by a radius, and define methods for computing its area and circumference.
Next, define `Rectangle` class which can be constructed by a length and width, and define methods for computing its area and perimeter.
Finally, write a `Square` class that inherits from `Rectangle`.

```python
from math import pi

class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def diameter(self):
        return 2 * self.radius

    def area(self):
        return pi * self.radius**2

    def circumference(self):
        return pi * self.diameter


class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, l):
        super().__init__(l, l)
```

#### Exercise ??

Write a function to strip the username from an email address (the text before the @ sign).
For example,
`username@companyname.com` should result in `username`.

```python
def get_username(email):
    return email.partition('@')[0]
```

#### Exercise ??

Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example:
If the following words is given as input to the program:

2 cats and 3 dogs.

Then, the output of the program should be:

['2', '3']

_Hint_:
Use re.findall() to find all substring using regex.

```python
import re
s = input()
print(re.findall("\d+",s))
```

<!--
#### Exercise ??

Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

_Hint_:
Use unicode() function to convert.

s = input()
u = unicode( s ,"utf-8")
print(u) -->

#### Exercise ??

Write a program to compute 1/2 + 2/3 + 3/4 + ... + n/(n+1) with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

3.55

_Hint_: Use float() to convert an integer to a float

```python
n=int(input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(sum)
```

#### Exercise ??

Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

With a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

500

_Hint_: We can define recursive function in Python.

```python
def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(input())
print(f(n))
```

#### Exercise ??

The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0

f(n)=1 if n=1

f(n)=f(n-1)+f(n-2) if n>1

Write a program to compute the value of f(n) with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

13

_Hint_: We can define recursive function in Python.

```python
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
print(f(n))
```

#### Exercise ??

The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0

f(n)=1 if n=1

f(n)=f(n-1)+f(n-2) if n>1

Write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13

_Hint_: We can define recursive function in Python.
Use list comprehension to generate a list from an existing list.
Use string.join() to join a list of strings.

```python
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
values = [str(f(x)) for x in range(0, n+1)]
print(",".join(values))
```

#### Exercise ??

Write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

_Hint_: Use yield to produce the next value in generator.

```python
def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1

n=int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))
```

#### Exercise ??

Write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70

_Hint_: Use yield to produce the next value in generator.

```python
def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input())
values = []
for i in NumGenerator(n):
    values.append(str(i))

print(",".join(values))
```

#### Exercise ??

Write assert statements to verify that every number in the list [2,4,6,8] is even.

_Hint_: Use "assert expression" to make assertion.

```python
li = [2,4,6,8]
for i in li:
    assert i%2==0
```

#### Exercise ??

Write a program which accepts basic mathematic expression from console and print the evaluation result.

Example:
If the following string is given as input to the program:

35+3

Then, the output of the program should be:

38

_Hint_: Use eval() to evaluate an expression.

expression = input()
print(eval(expression))

Write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

_Hint_: Use if/elif to deal with conditions.

```python
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))
```

#### Exercise ??

Write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

_Hint_: Use if/elif to deal with conditions.

```python
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))
```

#### Exercise ??

Generate a random float where the value is between 10 and 100 using the `random` module.

_Hint_: Use random.random() to generate a random float in [0,1].

```python
import random
print(random.random()*100)
```

#### Exercise ??

Generate a random float where the value is between 5 and 95 using the `random` module.

_Hint_: Use random.random() to generate a random float in [0,1].

```python
import random
print(random.random()*100-5)
```

#### Exercise ??

Write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

_Hint_: Use random.choice() to a random element from a list.

```python
import random
print(random.choice([i for i in range(11) if i%2==0]))
```

#### Exercise ??

Write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.

_Hint_: Use random.choice() to a random element from a list.

```python
import random
print(random.choice([i for i in range(201) if i%5==0 and i%7==0]))
```

#### Exercise ??

Write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

_Hint_: Use random.sample() to generate a list of random values.

```python
import random
print(random.sample(range(100), 5))
```

#### Exercise ??

Write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

_Hint_: Use random.sample() to generate a list of random values.

```python
import random
print(random.sample([i for i in range(100,201) if i%2==0], 5))
```

#### Exercise ??

Write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

_Hint_: Use random.sample() to generate a list of random values.

```python
import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))
```

#### Exercise ??

Write a program to randomly print a integer number between 7 and 15 inclusive.

_Hint_: Use random.randrange() to a random integer in a given range.

```python
import random
print(random.randrange(7,16))
```

#### Exercise ??

Write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

_Hint_: Use zlib.compress() and zlib.decompress() to compress and decompress a string.

```python
import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))
```

#### Exercise ??

Write a program to print the running time of execution of "1+1" for 100 times.

_Hint_: Use timeit() function to measure the running time.

```python
from timeit import Timer
t = Timer("for i in range(100):1+1")
print(t.timeit())
```

#### Exercise ??

Write a program to shuffle and print the list [3,6,7,8].

_Hint_: Use shuffle() function to shuffle a list.

```python
from random import shuffle
li = [3,6,7,8]
shuffle(li)
print(li)
```

#### Exercise ??

Write a program to shuffle and print the list [3,6,7,8].

_Hint_: Use shuffle() function to shuffle a list.

```python
from random import shuffle
li = [3,6,7,8]
shuffle(li)
print(li)
```

#### Exercise ??

Write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

_Hint_: Use list[index] notation to get a element from a list.

```python
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print(sentence)
```

#### Exercise ??

Write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

_Hint_: Use list comprehension to delete a bunch of element from a list.

```python
li = [5,6,77,45,22,12,24]
li = [x for x in li if x%2!=0]
print(li)
```

#### Exercise ??

By using list comprehension, write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

_Hint_: Use list comprehension to delete a bunch of element from a list.

```python
li = [12,24,35,70,88,120,155]
li = [x for x in li if x%5!=0 and x%7!=0]
print(li)
```

#### Exercise ??

By using list comprehension, write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

_Hint_: Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

```python
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print(li)
```

#### Exercise ??

By using list comprehension, write a program generate a 3*5*8 3D array whose each element is 0.

_Hint_: Use list comprehension to make an array.

```python
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)
```

#### Exercise ??

By using list comprehension, write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

_Hint_: Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

```python
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print(li)
```

#### Exercise ??

By using list comprehension, write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

_Hint_: Use list's remove method to delete a value.

```python
li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print(li)
```

#### Exercise ??

With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

_Hint_: Use set() and "&=" to do set intersection operation.

```python
set1=set([1,3,6,78,35,55])
set2=set([12,24,35,24,88,120,155])
set1 &= set2
li=list(set1)
print(li)
```

#### Exercise ??

With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

_Hint_: Use set() to store a number of values without duplicate.

```python
def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(li))
```

#### Exercise ??

Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

_Hint_: Use Subclass(Parentclass) to define a child class.

```python
class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
print(aMale.getGender())
print(aFemale.getGender())
```

#### Exercise ??

Write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

_Hint_: Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.

```python
dic = {}
s=input()
for s in s:
    dic[s] = dic.get(s,0)+1
print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))
```

#### Exercise ??

Write a program which accepts a string from console and print it in reverse order.

Example:
If the following string is given as input to the program:

rise to vote sir

Then, the output of the program should be:

ris etov ot esir

_Hint_: Use list[::-1] to iterate a list in a reverse order.

```python
s=input()
s = s[::-1]
print(s)
```

#### Exercise ??

Write a program which accepts a string from console and print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

_Hint_: Use list[::2] to iterate a list by step 2.

```python
s=input()
s = s[::2]
print(s)
```

#### Exercise ??

Write a program which prints all permutations of [1,2,3]

_Hint_: Use itertools.permutations() to get permutations of list.

```python
import itertools
print(list(itertools.permutations([1,2,3])))
```

#### Exercise ??

Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.

```python
def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print(solutions)
```
