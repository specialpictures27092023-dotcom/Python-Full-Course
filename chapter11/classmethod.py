class Employee:
    company="ITC"
    name="Nikhil"
    salary=120000
    
    @classmethod
    def show(self):
        print(f"The name of employee  is {self.name} and the salary is {self.salary}")

e=Employee()
e.name="NIKU"
e.show()