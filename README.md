# Python-Fundamentals-Assignment

Question 1: What is Python ? Explain any five important features of Python and mention why Python is considered beginner-friendly.

Answer: 

Python is a high-level, interpreted, gernal-purpose programming language known for its simple and readable syntax.
Created by Guido van Rossum in 1991. It is widely used in web development, Data science, AI, and Automation.

Five Imp features of Python

Easy to learn – Python has simple and readable syntax.
Interpreted – Python code is executed by the python interpreter without requiring traditional compilation first.
Dynamically typed – We don’t need to explicitly declare the type of a variable.
Large library ecosystem – Python provides libraries such as NumPy, Pandas, Scikit-learn, TensorFlow and Pytorch.
Platform Independent and open source – Python is an open source language and its code can run on any platform like- Windows, Linux and Mac without any change.

Why Python is beginner-Friendly
 
Because its syntax is simple, it requires less code, errors are easy to find, and it has a very large              community for help.

Question 2: What is a variable in Python? Explain dynamic typing and describe the following Python data types with one example each: int, float, str, bool, list, tuple, dict, set.

Answer : 

 A variable is like a box or container where we store data. It is a name given to a memory location. We use = to put value inside a variable. We don’t need to tell what type of data it is, python will understand.
Example : 

Name = “Ansh”
Age = 21

Here, name and age are variables.
Explain Dynamic Typing 

Dynamic typing means we do not need to declare the data type. Python automatically checks the type when the program is running. The best part is the same variable can store different types of data at different times.
Example: 

X = 10                     # x is integer now
X = “Hello”              # now same x is string,  no error

Data type with Example:

Int:   It stores full numbers without a decimal point. Like - 10, 0, 25, 100. Used for counting.

            Example:-   Students = 50

Float:  It stores numbers with a decimal point. Like 3.14, 99.99 used for price, height.

Example:-    price = 99.99

Str:  It stores text and words. It is always written inside double quotes “ “.

           Example:-   city = “Meerut”

Bool:  It stores only True or False. Used for Yes/No questions.

            Example:-    is_pass  =  True

List:  It is a collection of many values. It can be changed and allows duplicate values. It uses[].

            Example:-   fruits  =  [“apple”, “mango”, “banana”]

Tuple:  It is also a collection of many values like list, but it cannot be changed after creation. It uses (). It is faster than list.

            Example:-    numbers  =  (10, 20, 30)

Dict:  It stores data in key and value pairs. Like a real dictionary. It uses {}.

            Example:-   student  =  {“name” :  “Ansh”, “age”: 21}

Set:  It stores only unique values. It does not allow duplicate values. It also uses {}.

Example:-   my_set  =  { 1, 2, 3, 3}                     -> Output will be {1,2,3}
Question 3:  Explain the following types of operators in Python with suitable examples for Arithmetic operators, Comparison operators, Logical operators, Assignment operators, Membership operators, Identity operators. Also explain the difference between implicit and                                                                                             explicit type conversion.

Answer:  

An operator in python is a symbol or keyword that is used to perform an operation on one or more values or variables. Python provides different types of operators for performing mathematical, calculations, comparison, logical operations, assignments, membership testing, checking object identify.

Arithmetic Operators:
            Arithmetic operators are used to perform mathematical operations on numbers.

            Operators:-   +, -, /, %, //, **

            Example:- 

a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333
print(a % b)   # 1
print(a // b)  # 3
print(a ** b)  # 1000 

Comparison Operators:

             Comparison operators are used to compare two values. They return either True or False.
              Operators:-  ==, !=, >, <, >=, <=

              Example:-  

              a = 10
      b = 20

      print(a == b)  # False
      print(a != b)  # True
      print(a < b)   # True
      print(a > b)   # False 
Logical Operators

Logical operators are used to combine two or more conditions.
Operators:-  and, or, not

Example:- 

a = 10

print(a > 5 and a < 20)  # True
print(a < 5 or a > 8)    # True
print(not(a > 5))        # False


Assignment Operators:

Assignment operators are used to assign values to variables and update their values.
Operators:-   =, +=, -=, *=, /=, %=, //=, **=

Example:

x = 10

x += 5
print(x)   # 15

x -= 3
print(x)   # 12

x *= 2
print(x)   # 24

Membership Operators:

Membership operators are used to check whether a value is present in a sequence such as a list, tuple, set, or string.
Operators:-   in, not in

Example:

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)        # True
print("Orange" not in fruits)  # True 

Identify Operators

Identify operators are used to check whether two variable refer to the same object.
Operators:-    is, is not

Example:

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True
print(a is not c)  # True 

Difference Between Implicit and Explicit Type Conversion

The main difference between implicit and explicit type conversion is that implicit type conversion 

Implicit Type Conversion                                               Explicit Type Conversion

It is performed automatically by python.                             It is performed manually by the programmer.

No conversion function is required.                                   Conversion function such as int(), float(), and
                                                                                           str() are used.
It generally occurs automatically during compatible          It is used when the programmer wants to
operations.                                                                         Convert a value into a specific data type.

Example:  10 + 2.5                                                             Example:  int(“25”)

It is also called automatic type conversion.                        It is also called manual type conversion.
           

Question 4  :What is a string in Python? Explain string indexing, slicing, concatenation, repetition and formatting with suitable examples 

Answer: 

A string in python is a sequence of characters enclosed within single quotes(‘ ‘). Double quotes(“ “), or triple quotes(‘’’ ‘’’ / “”” “””).
String are used to store text such as names, words, sentences, etc.
Example:

Name = “Rahul”
Message = ‘Hello python’

print(name)
print(message) 

Output:        Rahul
                    Hello Python


String Indexing:

String indexing is used to access individual characters of a string. In python, indexing starts from 0.
For Example:

Text = “Python”

print(text[0])
print(text[1])
print(text[5])

Output:    P
                y
                n

String Slicing:

Starting slicing is used to extract a specific part of a string using start and end indexes.

Example:

Text = “python”
print(text [0:3 ])

Output:     pyt

String Concatenation

String concatenation means joining two or more strings together. 
The + operator is used for concatenation.

Example:  
a =  “hello”
b = “python”
print(a + “ “ + b)

Output:      hello python


String Repetition

String repetition means repeating a string multiple times. The * operators is used for repetition.

Example:

Text = “Hi”
Print( text * 3)

Output:     Hi Hi Hi

String Formating

String formatting is used to insert variable values into a string in a readable way. An f-string is a simple method of formatting strings in python.

Example:

Name = “Rahul”
age  = 20
print( f “ My name is {name} and I am {age} years old.”)

Output:    My name is Rahul and I am 20 years old.


Question 5: What is a list in Python? Explain why lists are called mutable. Describe any five commonly used list methods with examples. 

Answer:

A list is a collection of multiple items stored in a single variable. Lists are ordered, changeable (mutable), and are written using square brackets [ ].
Example:  

Fruits = [ “Apple”, “Banana”, “Mango” ]
print(fruits)

Output:   [ ‘Apple’, ‘Banana’, ‘Mango’ ]

Why are lists called mutable 

Lists are called mutable because their elements can be changed, added, or removed after the list is created.
Example:

Fruits = [ “Apple”, “Banana”, “Mango” ]
Fruits[1]  = “Orange”
print(fruits)

Output:     [ ‘Apple’, ‘Orange’, ‘Mango’ ]

Here, “Banana” is changed to “Orange”, which shows that lists are mutable.

Five Commonly Used list methods  

append()

The append() method is used to add an item at the end of a list.

fruits = [ “Apple”, “Banana” ]
fruits.append(“Mango”)
print(fruits)

Output:   [ ‘Apple’, ‘Banana’, ‘Mango’ ]

insert() 

The insert() method is used to add an item at a specific position in a list.

Fruits = [“Apple”, “Mango”]
fruits.insert(1, “Banana”)
print(fruits)

Output:    [‘Apple’, ‘Banana’, ‘Mango’]

remove()

The remove() method is used to remove a specific item from a list.

Fruits = [“Apple”, “Banana”, “Mango”]
fruits.remove(“Banana”)
print(fruits)
Output:     [‘Apple’, ‘Mango’]

pop() 

The pop() method is used to remove an item from a list. By default, it removes the last item.

fruits =  [“Apple”, “Banana”, “Mango”]
fruits.pop()
print(fruits)

Output:     [‘Apple’, ‘Banana’]

sort()

The sort() method is used to arrange the elements of a list in ascending order.

Numbers = [5,2,8,1]
numbers.sort()
print(numbers)

Output:    [1,2,5,8]


