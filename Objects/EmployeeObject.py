class Employee:
    company_name = 'code'  #class Based Variable

    def __init__(self,name,age,desig):
        self.name = name
        self.age = age
        self.desig = desig
    
    def login(self,time):
        print(f'{self.name} logged in at {time}')
    
    def logout(self,time):
        print(f'{self.name} loggedout at {time}')

    def work(self,hours):
        print(f'{self.name} worked for {hours}')
    
    def getDetails(self):
        print('Employee Name: ',self.name)
        print('Employee Age: ',self.age)
        print('Employee Designation: ',self.desig)


#Creating Objects: 
e1 = Employee('Ak',24,'SDE')
e2 = Employee('Pk',25,'Manager')
e3 = Employee('Rk',26,'Developer')

e1.getDetails()
e2.getDetails()
e3.getDetails()


