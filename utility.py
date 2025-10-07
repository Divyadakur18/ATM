# Utility: Authenticate user

def authenticate(accounts, name, pin):
    for account in accounts:
        if account["name"].lower() == name.lower() and account["pin"] == pin:
            return account
    return None
