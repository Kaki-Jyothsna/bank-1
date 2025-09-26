def customermenu(customers, loanrequests):
    name = input("Enter name: ")
    pin = int(input("Enter PIN: "))
    while True:
        print("\nCustomer Menu") 
        print("1. Check Balance") 
        print("2. Deposit Money") 
        print("3. Withdraw Money") 
        print("4. Transfer Money") 
        print("5. Apply for Loan") 
        print("6. View Loan Status") 
        print("7. Exit") 
        choice = input("Enter choice: ") 
        if choice == "1":
            checkbalance(customers, name, pin) 
        elif choice == "2":
            amt = int(input("Enter amount: "))
            deposit(customers, name, pin, amt) 
        elif choice == "3":
            amt = int(input("Enter amount: ")) 
            withdrawl(customers, name, pin, amt) 
        elif choice == "4":
            recv = input("Enter receiver name: ")
            amt = int(input("Enter amount: "))
            transfer(customers, name, pin, recv, amt) 
        elif choice == "5":
            amt = int(input("Enter loan amount: "))
            applyloan(loanrequests, customers, name, pin, amt) 
        elif choice == "6":
            viewloanstatus(loanrequests, customers, name, pin) 
        elif choice == "7":
            break 
        else:
            print("Invalid choice") 
customermenu(customers, loanrequests) 