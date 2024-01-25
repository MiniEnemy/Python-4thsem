class Employee:
    def __init__(self, name, address, salary, tool):
        self.name = name
        self.address = address
        self.salary = salary
        self.tool = tool

    def details(self):
        print(f"Employee name: {self.name}")
        print(f"Employee address: {self.address}")
        print(f"Employee salary: {self.salary}")
        print(f"Employee tool: {self.tool}")
