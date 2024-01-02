# class bike :
#     def __init__(self,name:str,cc:int):
#         self.name=name;
#         self.cc=cc;


#     def print_details(self):
#       print(f"Bike name {self.name} and c is {self.cc}");
#     # print(f"Bike name",self.name ,"c is",self.cc);


# bike_1=bike(name="yamha",cc=123);
# bike_1.print_details();
# bike_1.name="BMW";
# print(bike_1.name)

# * Acces modifier
#* Types: public,private,protected
# protected is identified by _ and private is idenified by __(double undersocore)
# class Bankacc:
#     def __init__(self,name:str,address:str,accno:int,balance:int):
#         self.name=name
#         self.address=address
#         self.accno=accno
#         self.balance=0
    
#     def details(self):
#         print(f"account holder name is{self.name}")
#         print(f"holder address is {self.address}")
#         print(f" holderaccno.is{self.accno}")
#         print(f" holderbalance is{self.balance}")

#     # def withdraw(self,amount,accname,accno):
#     #     print(f"enter the accname{self.accname} enter the accno")
        
#     def deposit(self):
#         deposit=int(input("enter the bal u want to add"))
#         self.balance=deposit+self.balance
#         print(f"yourbalanceis{self.balance}")

#     def withdraw(self):
#         balsub=int(input("Enter the amount u want to withdraw:"))
#         if self.balance >= balsub-self.balance:
#           self.balance=balsub-self.balance
#           print(f"your remaining balance is {self.balance}")
#         else:
#             print("invalid ur balance is lower")
#     def summary(self):
#         summar=print("your total balance is :{self.balance} ")

# jatin_account = Bankacc("Jatin","tahachal",4556578,0)

# choice= input("Enter whether u want to withdraw or deposit:  ")

# if choice == 'withdraw' :
#     jatin_account.withdraw()
# elif choice == 'deposit':
#     jatin_account.deposit()
# elif choice == 'summary':
#     pass
# else :
#     print("invalid entry try again")

class Bankacc:
    def __init__(self, name: str, address: str, accno: int, balance: int):
        self.name = name
        self.address = address
        self.accno = accno
        self.balance = balance

    def details(self):
        print(f"Account holder name is {self.name}")
        print(f"Holder address is {self.address}")
        print(f"Holder account number is {self.accno}")
        print(f"Holder balance is {self.balance}")

    def deposit(self):
        deposit = int(input("Enter the balance you want to add: "))
        self.balance = deposit + self.balance
        print(f"Your balance is {self.balance}")

    def withdraw(self):
        balsub = int(input("Enter the amount you want to withdraw: "))
        if self.balance >= balsub:
            self.balance = self.balance - balsub
            print(f"Your remaining balance is {self.balance}")
        else:
            print("Invalid, your balance is insufficient.")

    def summary(self):
        print(f"Your total balance is: {self.balance}")


jatin_account = Bankacc("Jatin", "tahachal", 4556578, 0)

while True:
    choice = input("Enter whether you want to withdraw, deposit, see the summary, or exit: ")

    if choice == 'withdraw':
        jatin_account.withdraw()
    elif choice == 'deposit':
        jatin_account.deposit()
    elif choice == 'summary':
        jatin_account.summary()
    elif choice == 'exit':
        print("Exiting the program.")
        break
    else:
        print("Invalid entry, please try again.")