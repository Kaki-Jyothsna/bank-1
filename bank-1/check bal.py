# customer features 
name= input("enter name:") 
pin=int(input("enter pin:")) 
def checkbalance(customers, name, pin): 
    cus = findcustomer(customers, name, pin)
    if cus:
        print("Balance:", cus["balance"]) 
    else: 
        print("Invalid login") 
checkbalance(customers, name, pin) 