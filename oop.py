
class Person:

    counter = 0

    def __init__(self,name):
        self.name = name
        Person.counter+=1
        

    def smile(self):
        print(f'i am {self.name} cheese') 

    def all():
        return 
    
    

sam = Person('sam')
# sam.smile()
print(Person.counter)

