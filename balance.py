# Function: Check Balance
from utility import authenticate

def check_balance(accounts, name, pin):
    account = authenticate(accounts, name, pin)
    if account:
        print(f"\nCurrent Balance: ₹{account['balance']}\n")
    else:
        print("\nInvalid name or PIN.\n")
