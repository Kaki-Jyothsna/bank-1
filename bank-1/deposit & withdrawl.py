# deposit money 
name = input("Enter name: ") 
pin = int(input("Enter PIN: ")) 
amount = int(input("Enter amount to deposit: "))  
def deposit(customers, name, pin, amount):
    cus= findcustomer(customers, name, pin) 
    if cus:
        cus["balance"]+=amount 
        print("deposited",amount ) 
        print("new balance:",cus["balance"])  #"new balance"==cus["balance"]) 
    else:
        print("no money deposited") 
deposit(customers, name, pin, amount) 
# withdraw money 
name = input("Enter name: ") 
pin = int(input("Enter PIN: ")) 
amount = int(input("Enter amount to withdraw: "))  
def withdrawl(customers, name, pin, amount):
    cus= findcustomer(customers, name, pin)
    if cus:
        if amount<=cus["balance"]:
            cus["balance"]-=amount
            print("withdrawl", amount, "new balance" , cus["balance"]) 
        else:
            print("insufficient funds") 
    else:
        ("invalid") 
withdrawl(customers, name, pin, amount) 