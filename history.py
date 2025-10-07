# Function: Transaction History
from utility import authenticate

def transaction_history(accounts, name, pin):
    account = authenticate(accounts, name, pin)
    if account:
        if account["transactions"]:
            print("\nTransaction History:")
            for t in account["transactions"]:
                print(f" - {t}")
        else:
            print("\nNo transactions found.")
        print()
    else:
        print("\nInvalid name or PIN.\n")