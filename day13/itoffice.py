class Designer:
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

designer1 = Designer(
    name="aryan",
    address="ktm",      
    salary=2800,
    tool="Figma"
)

developer1=Developer(
    name="jatin",
    address="tahachal",
    salary=28000,
    programminglang="python"
)
designer1.details()
developer1.details()