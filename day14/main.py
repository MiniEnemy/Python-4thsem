from developer import Developer
from designer  import Designer

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