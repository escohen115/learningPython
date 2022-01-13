
print("hello world")

# x = "awesome"

# print("python is " + x)


# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


class Person: 
    def __init__(self, age=0, name='blank'):
        self.age = age
        self.name = name

    def happy(self):
        print(f"you are {self.age}")


    def greet(self):
        print(f"hello {self.name}")
    
simcha = Person(26, "simcha")


simcha.happy()
simcha.greet()


i = 0
for i in range(6):
    if i % 2 == 0:
        print(f"{i} is even")
    if i % 2 != 0:
        print(f"{i} is odd")

import random

print(random.randrange(1, 10))


a = """this
and 
that"""

print (a)

a = "Hello, World!"
print(a[1])


