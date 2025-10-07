# Function
from balance import check_balance
from deposit import deposit
from withdraw import withdraw
from history import transaction_history
from data import accounts

def menu():
    while True:
        print("===== ATM Machine =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice in ['1', '2', '3', '4']:
            name = input("Enter your name: ").strip()
            try:
                pin = int(input("Enter your 4-digit PIN: ").strip())
            except ValueError:
                print("\nPIN must be a 4-digit number.\n")
                continue

            if choice == '1':
                check_balance(accounts, name, pin)
            elif choice == '2':
                try:
                    amount = float(input("Enter amount to deposit: "))
                    deposit(accounts, name, pin, amount)
                except ValueError:
                    print("\nInvalid input. Please enter a numeric amount.\n")
            elif choice == '3':
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    withdraw(accounts, name, pin, amount)
                except ValueError:
                    print("\nInvalid input. Please enter a numeric amount.\n")
            elif choice == '4':
                transaction_history(accounts, name, pin)
        elif choice == '5':
            print("\nThank you for using the ATM. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please select from the menu.\n")

