#mutable set (we can change data)
# fruits={"apple","orange","mango","watermelon"}
# vegetable={"carrot","potato","tomatoes","watermelon"}
# set=fruits.union(vegetable)
# inter=fruits.intersection(vegetable)
# print("set is",set)
# print("intersection is",inter)

#immutable set (we can't change set data)
# fruit=frozenset({"apple","orange","mango","watermelon"})
# print(fruit)

a=20
b=123
print(a>b)
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")