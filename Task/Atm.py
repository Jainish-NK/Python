balance = 10000

while True:
    print("\nATM Menu:")
    print("\n1.Check Balance")
    print("\n2.Deposite Balance")
    print("\n3.Withdraw Money")
    print("\n4.Exit")

    choice = input("\nEnter The Choice(1-4) : ")

    if choice =='1':
        print("Current Balance: ",balance)
    elif choice == '2':
        amt = int(input("\nEnter Amount Deposite : "))
        balance += amt
        print("\nAmount Deposited.")
    elif choice =='3':
        amt = int(input("\nEnter Amount to withdraw: "))
        if amt > balance:
            print("\nInsufficient Balance.")
        else:
            balance -= amt
            print("Please collect your cash.")
    elif choice =='4':
        print("Thank you for using the ATM.")
    else:
        print("Invalid choice. Try again.")