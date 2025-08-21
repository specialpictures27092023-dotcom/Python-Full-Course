class Employee:
    a=1
    company="ITC"
    name="Nikhil"
    salary=120000

    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    
    @property
    def name(self):
        return self.ename
    
    @name.setter
    def name(self,value):
        self.ename=value


e=Employee()

e.name="NIKHIL"
print(e.name)

e.show()