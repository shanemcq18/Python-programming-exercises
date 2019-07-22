# 100+ Python Programming Exercises

Adapted from [https://github.com/zhiwehu/Python-programming-exercises](https://github.com/zhiwehu/Python-programming-exercises).
Exercises have been updated to Python 3 and expanded (or completely changed).

The exercises are grouped into the following difficulty levels.

- **Beginner.**
For someone who has just gone through an introductory Python course.
Problem solutions may involve one or two Python classes or functions, but nothing beyond built-in functions.

- **Intermediate.**
For someone who has just learned Python, but who already has a programming background.
Problem solutions may involve three or four Python classes or functions, including some tools from the standard library.

- **Advanced**.
For someone who has been using Python for some time.
Problem solutions may require several classes or functions, including tools from scientific computing libraries such as `numpy`.

## Beginner Exercises

#### Exercise ??

Write a function that accepts positive integers `a`, `b`, `c`, and `d`.
Return the list of all integers `n` between `a` and `b` (inclusive) which are divisible by `c` but not by `d`.
Use your function to find integers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (inclusive).
Print the results in a comma-separated sequence on a single line.

_Hint_: Recall the `%` operator calculates the remainder of a division (e.g., `10 % 3` returns `1`).

#### Exercise ??

Write a function which computes the factorial of a given integer (e.g., `5! = 5*4*3*2*1 = 120`).
Use your function to find `14!`.

_Hint_: make the function recursive.

#### Exercise ??

Write a function that accepts an integer `n`.
Return the dictionary containing key-value pairs `(i, i*i)` for all even integers `1 ≤ i ≤ n`.
For example, `n = 8` should result in the dictionary
`{2: 4, 4: 16, 6: 36, 8: 64}`.

#### Exercise ??

Write a program which accepts a comma-separated sequence from the console.
Generate a list and a tuple which contains every sequence element.
For example, if the user types `34,67,55,33,12,98`, the output should be
```
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
```
_Hint_: use the built-in function `input()` to read console input from the user.

#### Exercise ??

Define a class with the following methods:

- `get_string()`: read (and store) a string from console input.
- `print_string()`: print the string in upper case.

Also include simple functions to test each class method.

#### Exercise ??

Write a function which accepts 2 integers `X`, `Y`.
Generates a 2-dimensional array with `X` rows and `Y` columns as a list of lists, where the element value in the `i`th row and `j`th column of the array is `i*j`, with `0 ≤ i ≤ X` and `0 ≤ j ≤ Y`.

For example, `X=3` and `Y=5` should result in the following array.
#### Exercise ??

Write a program that receives a comma-separated sequence of strings from the console, sorts the sequence alphabetically, and prints it again as a comma-separated sequence.

For example, the input `without,hello,bag,world` should result in `bag,hello,without,world` being printed.

#### Exercise ??

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

#### Exercise ??

Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

_Hint_: case a sequence as a `set()` to remove duplicated data; use `sorted()` to create a new list of sorted data from a sequence.

#### Exercise ??

Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

#### Exercise ??

Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

#### Exercise ??

Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

#### Exercise ??

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

#### Exercise ??

Write a function that accepts two positive integers `a` and `n`.
Compute the value of `a` + `aa` + `aaa` + ... + `aaaaaaa` (n times), where `aa` indicates the two-digit number with both digits `a`, and so on.

For example, with `a=1` and `n=3`, the task is to compute `1 + 11 + 111 = 123`.

#### Exercise ??
<!-- List Comprehension -->

Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
`1,2,3,4,5,6,7,8,9`
Then, the output should be:
`1,3,5,7,9`

#### Exercise ??

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

#### Exercise ??

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

#### Exercise ??

Write a generator that yields the positive integers less than a given integer `n` which are divisible by a given integer `d`.
Use your generator to get the multiples of 7 that are less than 100.

#### Exercise ??

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

#### Exercise ??

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

#### Exercise ?? (Strings and Numbers)

Define a function that can receives two numbers as strings and returns their sum as a string.
For example, the inputs `"12"` and `"3"` should give the output `"15"`.

Next, write a function that accepts two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print al l strings line by line.

#### Exercise ??

Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

_Hint_:
Use % operator to check if a number is even or odd.

#### Exercise ??

Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

_Hint_:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.

#### Exercise ??

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

_Hint_:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

#### Exercise ??

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

_Hint_:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

#### Exercise ??

Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

_Hint_:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.

#### Exercise ??

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

_Hint_:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

#### Exercise ??

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

_Hint_:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

#### Exercise ??

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

_Hint_:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

#### Exercise ??

Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

_Hint_:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use tuple() to get a tuple from a list.

#### Exercise ??

With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

_Hint_:
Use [n1:n2] notation to get a slice from a tuple.

#### Exercise ??

Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

_Hint_:
Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.

#### Exercise ??

Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

_Hint_:
Use if statement to judge condition.

#### Exercise ??

Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

_Hint_:
Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.

#### Exercise ??

Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

_Hint_:
Use map() to generate a list.
Use lambda to define anonymous functions.

#### Exercise ??

Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

_Hint_:
Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.

#### Exercise ??

Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

_Hint_:
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.

#### Exercise ??

Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

_Hint_:
Use map() to generate a list.
Use lambda to define anonymous functions.

#### Exercise ??

Define a class named American which has a static method called printNationality.

_Hint_:
Use @staticmethod decorator to define class static method.

#### Exercise ??

Define a class named American and its subclass NewYorker.

_Hint_:
Use class Subclass(ParentClass) to define a subclass.

#### Exercise ?? (OOP)

Define a `Circle` class which can be constructed by a radius, and define methods for computing its area and circumference.
Next, define `Rectangle` class which can be constructed by a length and width, and define methods for computing its area and perimeter.
Finally, write a `Square` class that inherits from `Rectangle`.

#### Exercise ??

Write a function to strip the username from an email address (the text before the @ sign).
For example,
`username@companyname.com` should result in `username`.

#### Exercise ??

Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example:
If the following words is given as input to the program:

2 cats and 3 dogs.

Then, the output of the program should be:

['2', '3']

_Hint_:
Use re.findall() to find all substring using regex.

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

#### Exercise ??

Write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

_Hint_: Use yield to produce the next value in generator.

#### Exercise ??

Write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70

_Hint_: Use yield to produce the next value in generator.

#### Exercise ??

Write assert statements to verify that every number in the list [2,4,6,8] is even.

_Hint_: Use "assert expression" to make assertion.

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

#### Exercise ??

Write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

_Hint_: Use if/elif to deal with conditions.

#### Exercise ??

Generate a random float where the value is between 10 and 100 using the `random` module.

_Hint_: Use random.random() to generate a random float in [0,1].

#### Exercise ??

Generate a random float where the value is between 5 and 95 using the `random` module.

_Hint_: Use random.random() to generate a random float in [0,1].

#### Exercise ??

Write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

_Hint_: Use random.choice() to a random element from a list.

#### Exercise ??

Write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.

_Hint_: Use random.choice() to a random element from a list.

#### Exercise ??

Write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

_Hint_: Use random.sample() to generate a list of random values.

#### Exercise ??

Write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

_Hint_: Use random.sample() to generate a list of random values.

#### Exercise ??

Write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

_Hint_: Use random.sample() to generate a list of random values.

#### Exercise ??

Write a program to randomly print a integer number between 7 and 15 inclusive.

_Hint_: Use random.randrange() to a random integer in a given range.

#### Exercise ??

Write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

_Hint_: Use zlib.compress() and zlib.decompress() to compress and decompress a string.

#### Exercise ??

Write a program to print the running time of execution of "1+1" for 100 times.

_Hint_: Use timeit() function to measure the running time.

#### Exercise ??

Write a program to shuffle and print the list [3,6,7,8].

_Hint_: Use shuffle() function to shuffle a list.

#### Exercise ??

Write a program to shuffle and print the list [3,6,7,8].

_Hint_: Use shuffle() function to shuffle a list.

#### Exercise ??

Write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

_Hint_: Use list[index] notation to get a element from a list.

#### Exercise ??

Write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

_Hint_: Use list comprehension to delete a bunch of element from a list.

#### Exercise ??

By using list comprehension, write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

_Hint_: Use list comprehension to delete a bunch of element from a list.

#### Exercise ??

By using list comprehension, write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

_Hint_: Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

#### Exercise ??

By using list comprehension, write a program generate a 3*5*8 3D array whose each element is 0.

_Hint_: Use list comprehension to make an array.

#### Exercise ??

By using list comprehension, write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

_Hint_: Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

#### Exercise ??

By using list comprehension, write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

_Hint_: Use list's remove method to delete a value.

#### Exercise ??

With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

_Hint_: Use set() and "&=" to do set intersection operation.

#### Exercise ??

With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

_Hint_: Use set() to store a number of values without duplicate.

#### Exercise ??

Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

_Hint_: Use Subclass(Parentclass) to define a child class.

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

#### Exercise ??

Write a program which accepts a string from console and print it in reverse order.

Example:
If the following string is given as input to the program:

rise to vote sir

Then, the output of the program should be:

ris etov ot esir

_Hint_: Use list[::-1] to iterate a list in a reverse order.

#### Exercise ??

Write a program which accepts a string from console and print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

_Hint_: Use list[::2] to iterate a list by step 2.

#### Exercise ??

Write a program which prints all permutations of [1,2,3]

_Hint_: Use itertools.permutations().

#### Exercise ??

Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.
