# Set data Type
# set no dupliction
#unordered
#explicit,

a={12,26,35,44,56}
b={12,54,24,55}
c = a.union(b)
d=a.intersection(b) # 1 way to use intersection othe r is 
e=a|b
f=a&b
# print ("the union is ",c)
print ("intersection is",d)
print("the pipe operator intersection is",e)
print("the ",f)
print(set(a))
print(type(set(a)))
