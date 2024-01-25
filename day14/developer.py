
class Developer:
    def __init__(self,name,address,salary,programminglang):
        self.name=name
        self.address=address
        self.salary=salary
        self.programminglang=programminglang
        

    def details(self):
        print(f"developer name{self.name}")
        print(f"developer address{self.address}")
        print(f"developer salary{self.salary}")
        print(f"developer programming lang{self.programminglang}")