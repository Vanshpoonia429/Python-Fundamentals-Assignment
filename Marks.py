# Python Fundamental Assighment

Question 6: Write a Python program that accepts two numbers from the user and performs:

● Addition 
● Subtraction 
● Multiplication 
● Division 
● Remainder 

Display all results clearly 

Answer:

a = int(input(“Entert first number: “))
b = int(input(“Enter second number:”))

print(“Addition =”, a+b)
print(“Subtraction =”, a-b)
print(“Multiplication =”, a*b)
print(“Division =” a/b)
print(“Remainder =”, a%b)

Question 7: Write a Python program that accepts a sentence from the user and displays: 

1. The sentence in uppercase. 
2. The sentence in lowercase. 
3. The total number of characters. 
4. The first five characters. 
5. The reversed sentence. 
6. The number of words in the sentence.. 

Answer:

Sentence = input(“Enter a sentence: “)

print(“Uppercase =”, sentence.upper())
print(“Lowercase =”, sentence.lover())
print(“Total characters =”, len(sentence))
print(“First five characters =”, sentence [ :5 ])
print(“Reversed sentence =”, sentence [ ::-1])
print(“Number of words =”, len(sentence.split())

Question 8: Create the following list: 

marks = [72, 85, 60, 91, 78] 

Write a Python program to: 
 1. Add 88 to the list.
 2. Remove 60.
 3. Sort the list.
 4. Display the highest mark. 
 5. Display the lowest mark.
 6. Calculate the average mark. 

Answer:

Marks = [ 72, 85, 60, 91, 78 ]

marks.append(88)
marks.remove(60)
marks.sort()

print( “List =”, Marks)
print(“Highest mark =”, max(marks))
print(“Lowest marks =”, min(marks))
print(“Average marks =”, sum(marks) / len(marks))

Question 9: Consider the following string:

 "Python Java C C++ Python Java Python"

 Write a Python program to: 
1. Convert the string into a list of programming languages. 
2. Display the list. 
3. Count how many times "Python" appears. 
4. Remove duplicate language names. 
5. Join the unique language names using " | ". 

Answer:

text  = “Python java c c++ Python Java Python”

languages = text.split()

print(“List =”, languages)
print(“Python appears =”, language.count(“Python”), “times”)

unique = list(set(languages))

print( “Unique languages =”, unique)
print( “Joined =”, “ | “.join(unique))


Question 10: Write a Python program to store the following student information: 

● Student name
● Course name 
● Marks in three subjects 

The program should: 
1. Store the three marks in a list. 
2. Calculate the total marks. 
3. Calculate the average. 
4. Display the highest mark. 
5. Display all student details using an f-string. 

Answer:

name = input(“Enter student name: “)
course = input(“Enter course name: “)
marks = [
        int(input(“Enter marks of subject 1: “)),
        int(input(“Enter marks of subject 2: “)),
        int(input(“Enter marks of subject 3: “))
]

total = sum(marks)
Average = total / 3
highest = max(marks)

print( f”Student name: {name}”)
print( f.”Course name:  {course}”)
print( f.”Marks: {marks}”)
print( f”Total Marks: {total}”)
print( f”Average: {average}”)
print( f”Highest Marks: {highest}”)

