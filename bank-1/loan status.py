# apply loan 
name = input("Enter name: ") 
pin = int(input("Enter PIN: ")) 
amount =input("Enter amount to applyloan:") 
def applyloan(loanrequests, customers, name, pin, amount):
    cus = findcustomer(customers, name, pin)
    if cus:
        loanrequests.append({"customerid": cus["id"], "amount": amount, "status": "Pending"})
        print("Loan request submitted")
    else:
        print("Invalid") 
applyloan(loanrequests, customers, name, pin, amount) 
# view loan status 
def viewloanstatus(loanrequests, customers, name, pin):
    cus = findcustomer(customers, name, pin)
    if cus:
        for req in loanrequests:
            if req["customerid"] == cus["id"]:
                print("Amount:", req["amount"], "Status:", req["status"])
    else:
        print("Invalid") 
viewloanstatus(loanrequests, customers, name, pin)