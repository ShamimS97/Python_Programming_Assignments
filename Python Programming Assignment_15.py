#!/usr/bin/env python
# coding: utf-8
Question 1:
Please write a program using generator to print the numbers which can be divisible by 5 and
7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
# In[1]:


def divisible_by_5_and_7(n):
    for i in range(n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

# Example usage
n = int(input("Enter a value for n: "))

result = divisible_by_5_and_7(n)
output = ','.join(str(num) for num in result)
print(output)

Question 2:
Please write a program using generator to print the even numbers between 0 and n in comma
separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
# In[2]:


def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Example usage
n = int(input("Enter a value for n: "))

result = even_numbers(n)
output = ','.join(str(num) for num in result)
print(output)

Question 3:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma
separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7

Then, the output of the program should be:
0,1,1,2,3,5,8,13
# In[3]:


def fibonacci_sequence(n):
    sequence = [0, 1]

    for i in range(2, n+1):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)

    return sequence[:n+1]

# Example usage
n = int(input("Enter a value for n: "))

fib_sequence = fibonacci_sequence(n)
output = ','.join(str(num) for num in fib_sequence)
print(output)

Question 4:
Assuming that we have some email addresses in the 'username@companyname.com' format,
please write program to print the user name of a given email address. Both user names and
company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john
# In[4]:


def get_username(email):
    username = email.split('@')[0]
    return username

# Example usage
email = input("Enter an email address: ")

username = get_username(email)
print(username)

Question 5:
Define a class named Shape and its subclass Square. The Square class has an init function
which takes a length as argument. Both classes have a area function which can print the area
of the shape where Shape's area is 0 by default.
# In[5]:


class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


# Example usage
shape = Shape()
print("Shape area:", shape.area())  # Output: 0

square = Square(5)
print("Square area:", square.area())  # Output: 25

