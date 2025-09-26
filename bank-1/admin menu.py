def adminmenu(customers, loanrequests):
    while True:
        print("\nAdmin Menu") 
        print("1. View All Accounts") 
        print("2. View Loan Requests") 
        print("3. Approve Loan") 
        print("4. Reject Loan") 
        print("5. Exit")
        option = input("Enter choice: ")
        if option == "1":
            viewallacc(customers)
        elif option == "2":
            loanrequest(loanrequests, customers) 
        elif option == "3": 
            cid = int(input("Enter Customer ID: ")) 
            loanstatus(loanrequests, cid) 
        elif option == "4": 
            cid = int(input("Enter Customer ID: ")) 
            loanstatus(loanrequests, cid) 
        elif option == "5": 
            break 
        else:
            print("Invalid choice") 
adminmenu(customers, loanrequests)