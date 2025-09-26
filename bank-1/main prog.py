# Main Program 
def main():
    while True:
        print("\nBank Management System")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            admin_menu(customers, loanrequests)
        elif choice == "2":
            customermenu(customers, loanrequests)
        elif choice == "3":
            break
        else:
            print("Invalid choice") 
main()
