class Employee:
    company="ITC"
    name="Nikhil"
    salary=120000
    
    def show(self):
        print(f"The name of the employee is  {self.name} and the salary is {self.salary}")

class coder:
    language="Python"

    def printlanguages(self):
        print(f"Out of all languages here is your language {self.language} ")

class Programmer(Employee,coder):
    company="ITC INFOTECH"
        
    def showlanguage(self):
        print(f"The name is {self.name} and the language is {self.language}")

a=Employee()
b=Programmer()

b.show()
b.printlanguages()
b.showlanguage()