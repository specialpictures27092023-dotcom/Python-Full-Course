class Employee:
    company="ITC"
    name="Nikhil"
    salary=120000
    
    def shows(self):
        print(f"The salary is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company="ITC INFOTECH"
    language="Python"
        
    def showlanguage(self):
        print(f"The name is {self.name} and the language is {self.language}")

a=Employee()
b=Programmer()

print(a.company,"\n",b.company)