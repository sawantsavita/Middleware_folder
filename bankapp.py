import datetime

class Bank:
    bank_name = "ICICI Bank"
    bank_amt = 20000000

    def __init__(self, uname, pd, name, bal, type, acc_no):
        self.username = uname
        self.password = pd
        self.name = name
        self.account_no = acc_no
        self.balance = bal
        self.account_type = type

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return str(self)

    def get_balance(self):
        print("Current balance is ", self.balance, "on ", datetime.datetime.now())

    @classmethod
    def get_bank_name(cls):
        print("Bank name: ", Bank.bank_name)

    @classmethod
    def get_bank_amt(cls):
        print("Current bank amount is ", Bank.bank_amt,"on ", datetime.datetime.now())
        
    def withdraw(self, amt):
        if amt < 0:
            print("Amount is negative number. Enter the valid amount.")
        elif amt < self.balance:
            self.balance -= amt
            self.get_balance()
        else:
            print("Balance is less than the amount that you want to withdraw so not possible to complete the transaction.")
            
    def deposit(self, amt):
        if amt < 0:
            print("Amount is negative number. Enter the valid amount.")
        else:
            self.balance += amt
            self.get_balance() 


# b1 = Bank("savita", "savita", "savita", 23000, "savings", 101)
# print(b1)
# b1.get_bank_amt()
# b1.get_balance()
# b1.withdraw(-22000)
# b1.deposit(10000)

cust_no = int(input("How many accounts do you want to create? "))
customer_lst = []
for i in range(1, cust_no+1):
    print("Enter details of new Customer ")
    uname = input("Enter the username: ") 
    pd = input("Enter the password: ")
    name = input("Enter the Name of AccountHolder: ") 
    bal = int(input("Enter the balance amount: "))
    type = input("Enter the type of account: ")
    acc_no = i
    obj = Bank(uname, pd, name, bal, type, acc_no)
    customer_lst.append(obj)
print(customer_lst)

def account_no_generation():
    acc_no_list = [customer.account_no for customer in customer_lst]
    print(acc_no_list)
    max_acc_no = max(acc_no_list)
    acc =max_acc_no + 1
    return acc

def create_new_account():
    print("Enter details of new Customer ")
    uname = input("Enter the username: ") 
    flag = False
    for i in customer_lst:
        if i.username == uname:
            print("Username already exists.")
            flag = True
            break
    if flag == False:
        pd = input("Enter the password: ")
        name = input("Enter the Name of AccountHolder: ") 
        bal = int(input("Enter the balance amount: "))
        type = input("Enter the type of account: ")
        acc_no = account_no_generation()
        obj = Bank(uname, pd, name, bal, type, acc_no)
        customer_lst.append(obj)
        print("Customer account created successfully.")
        print(customer_lst)
    
while True:
    print(f"""
Options:
1. Display bank name 
2. Display bank amount 
3. Display customer balance
4. Withdraw amount
5. Deposit amount
6. Create new account
7. Exit
""")
    option = int(input("Enter the option: "))
    if option == 1:
        Bank.get_bank_name()
        
    if option == 2:
        Bank.get_bank_amt()
        
    if option == 3:
        uname = input("Enter username: ")
        pw = input("Enter password: ")
        for i in customer_lst:
            if i.username == uname and i.password == pw:
                i.get_balance()
            else:
                print("Account not present")
                
    if option == 4:
        uname = input("Enter username: ")
        pw = input("Enter password: ")
        flag = False
        for i in customer_lst:
            if i.username == uname and i.password == pw:
                amt = int(input("Enter the amount do you want to withdraw: "))
                i.withdraw(amt)  
                flag = True
                break              
        if flag == False:
            print("Account not present")
        pass
    if option == 5:
        uname = input("Enter username: ")
        pw = input("Enter password: ")
        flag = False
        for i in customer_lst:
            print(i)
            if i.username == uname and i.password == pw:
                amt = int(input("Enter the amount do you want to deposit: "))
                i.deposit(amt)
                flag = True
                break
        if flag == False:
            print("Account not present")
            
    if option == 6:
        create_new_account()
        
    if option == 7:   
        print(f"Thanks for using {Bank.bank_name}")
        break
    
    inp = input("Would you like to continue? (Yes/ No): ").lower()
    if inp in ["yes", "y"]:
        pass
    else:
        print(f"Thanks for using {Bank.bank_name}")
        break
        
