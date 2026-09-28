
balance = 1000

print("===== SIMPLE BANKING SYSTEM =====")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your Balance: Rs.", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Amount deposited successfully!")
            print("Current Balance:", balance)
        else:
            print("Enter a valid amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Enter a valid amount.")
        elif amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid choice. Please try again.")