# no=10

# while True:
#     print(no)
#     if no>5:
#         break
#     no=no+1
# no=[4,45,55,6,42,41]
# search_number=41
# for no in no:
#     if no==search_number:
#         print("Number Found")
#         break
# else:
#     print("Number not found")

# ! BREAK STATMENT EXAMPLE BELOW

# while True:
#     number=input("ENter a  number")
    
#     if(number.isdigit()):
#         print(f"the Entetred number is",number)
#         break
#     else:
#         print("invaid input")


# ? continue Statement Example

no=[5,4,8,9,63]
for no in no:
    if no%2==0:
        continue
    print(no)
        