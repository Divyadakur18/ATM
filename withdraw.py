# Function: Withdraw
from utility import authenticate

def withdraw(accounts, name, pin, amount):
    account = authenticate(accounts, name, pin)
    if account:
        if amount > 0:
            if account["balance"] >= amount:
                account["balance"] -= amount
                account["transactions"].append(f"Withdrew ₹{amount}")
                print(f"\n₹{amount} withdrawn successfully. New balance: ₹{account['balance']}\n")
            else:
                print("\nInsufficient balance.\n")
        else:
            print("\nInvalid amount. Please enter a positive number.\n")
    else:
        print("\nInvalid name or PIN.\n")