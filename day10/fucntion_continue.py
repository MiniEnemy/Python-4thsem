# # # ! functional argument
# # # ! postional argument
# # # ! default argument
# # # ! arbitary argument 
# # # ? Key word arbitary(argument)
# # print("hi")
# def perform_maths(num_1,num_2,operation) :
#     if (operation == "+") :
#         print(num_1+num_2)
#     elif (operation == "-") :
#         print(num_1-num_2)
#     elif (operation == "*") :
#         print(num_1*num_2)
#     elif (operation == "%") :
#         print(num_1%num_2)
#     else :
#         print("invalid number")
# num_1= int(input("Enter your number"))
# num_2= int(input("Enter your number"))
# operation= input("Enter yout operator:")
# perform_maths(num_1,num_2,operation)

# # Default argumnent 
def total_marks(math,english,**kwargs):
        total=math+english
        for subject,mark in kwargs.items():
            print("Total marks=",total)
total_marks(math=23,english=12,opt_math=123,account=21)