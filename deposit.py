# Function: Deposit
from utility import authenticate

def deposit(accounts, name, pin, amount):
    account = authenticate(accounts, name, pin)
    if account:
        if amount > 0:
            account["balance"] += amount
            account["transactions"].append(f"Deposited ₹{amount}")
            print(f"\n₹{amount} deposited successfully. New balance: ₹{account['balance']}\n")
        else:
            print("\nInvalid amount. Please enter a positive number.\n")
    else:
        print("\nInvalid name or PIN.\n")