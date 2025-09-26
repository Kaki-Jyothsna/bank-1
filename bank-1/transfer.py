# transfer money 
sendername = input("Enter your name: ") 
senderpin = int(input("Enter your PIN: ")) 
receivername = input("Enter receiver name: ") 
amount = int(input("Enter amount: ")) 
def transfer(customers, sendername, senderpin, receivername, amount):
    sender = findcustomer(customers, sendername, senderpin)
    receiver = None
    for c in customers:
        if c["name"].lower() == receivername.lower():
            receiver = c
            break
    if sender is None:
        print("Invalid sender login")
        return
    if receiver is None:
        print("Receiver not found")
        return
    if amount > sender["balance"]:
        print("Insufficient balance")
        return
    sender["balance"] -= amount
    receiver["balance"] += amount
    print("Transferred", amount, "to", receivername)
    print("Your new balance is", sender["balance"]) 
transfer(customers, sendername, senderpin, receivername, amount) 