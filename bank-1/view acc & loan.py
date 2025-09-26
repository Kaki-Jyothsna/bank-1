customers = [  
{"id":1, "name":"Ravi", "balance":5000, "pin":1234, "loan_requests":[]},  
{"id":2, "name":"Priya", "balance":7000, "pin":2345, "loan_requests":[]},  
{"id":3, "name":"Suresh","balance":10000, "pin":3456, "loan_requests":[]}] 
loanrequests = [  
{"customerid": 1, "amount": 5000, "status": "Pending"},  
{"customerid": 2, "amount": 10000, "status": "Pending"}] 
def findcustomer(customers, name, pin):
    for c in customers:
        if c["name"].lower() == name.lower() and c["pin"] == pin:
            return c 
            return None 
# admin features 
# view all accounts 
def viewallacc(customers): 
    for c in customers: 
        print("id:",c["id"], "name:",c["name"],"balance:",c["balance"]) 
viewallacc(customers) 
# view loan requests 
def loanrequest(loanrequests,customers): 
    for req in loanrequests: 
        for c in customers: 
            if c["id"]==req["customerid"]: 
                print("id",req["customerid"],"amount",req["amount"],"status",req["status"]) 
loanrequest(loanrequests,customers) 
# approve/reject loan requests 
def loanstatus(loanrequests): 
    for req in loanrequests: 
        if req["customerid"]== customerid and req["status"]== "pending": 
            req["status"]="approved" 
            print("loan is approved") 
        else: 
            print("no pending loans")