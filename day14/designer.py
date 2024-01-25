# import employee as emp

from employee import employee

# class Designer(emp.employee):
class Designer(employee):
    def __init__(self,name,address,salary,tool):
        self.name=name
        self.address=address
        self.salary=salary
        self.tool=tool

    def details(self):
        print(f"employee name{self.name}")
        print(f"employee address{self.address}")
        print(f"employee salary{self.salary}")
        print(f"employee tool{self.tool}")
