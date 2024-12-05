def atm():
    balance = 500

    def check_balance():
        print(f"  balance is: ${balance:.2f}")

    def deposit():
        nonlocal balance
        try:
            amount = float(input("Enter the amount to deposit: $"))
            if amount > 0:
                balance += amount
                print(f"Successfully deposited ${amount:.2f}.")
                check_balance()
            else:
                print("Deposit Can' be zero or negative.")
        except ValueError:
            print("Only enter a numeric value.")

    def withdraw():
        nonlocal balance
        try:
            amount = float(input("Enter the amount to withdraw: $"))
            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")
            elif amount > balance:
                print("Insufficient balance. Cannot withdraw.")
            else:
                balance -= amount
                print(f"Successfully withdrew ${amount:.2f}.")
                check_balance()
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def menu():
        while True:

            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Please choose an option (1-4): ")

            if choice == "1":
                check_balance()
            elif choice == "2":
                deposit()
            elif choice == "3":
                withdraw()
            elif choice == "4":
                print("Thank you.")
                break
            else:
                print("Invalid choice.")

    menu()
atm()


