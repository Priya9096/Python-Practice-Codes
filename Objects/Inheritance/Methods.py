class Student:
    def cook(self):
        print('Student is cooking')
    def play(self):
        print('Playing cricket')

class Employee(Student):
    def work(self):
        print('Employee is working')  
    def cook(self):
        print('Employee is cooking')
e = Employee()
e.play()


'''
work():Specialized Method: Only in child class
play():Inherited: Used as it is in child class
cook():Overridden Method: Change Implementation in child
'''
