import random
from storage import all_accounts, save_accounts

def pin_setup():
    pin = input("Set up a 4-digit PIN for your account: ").strip()
    if len(pin) == 4 and pin.isdigit():
        print("PIN set successfully.")
        return pin
    else:
        print("Invalid PIN. Please enter a 4-digit number.")
        return pin_setup()

def create_account():
    print("Welcome\nCreate an account with us today")
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    password = input("Enter a password: ").strip()
    user_name = first_name.lower() + last_name.lower() + str(random.randint(1, 5))
    print(f"Your username is {user_name}, welcome {first_name}")

    user_pin = pin_setup()
    account = {
        "first_name": first_name,
        "last_name": last_name,
        "username": user_name,
        "password": password,
        "pin": user_pin,
        "balance": 100000,
        "transactions": []
    }
    all_accounts[user_name] = account
    save_accounts()
    print("Account created successfully, please note your username for login")
    return account

def login_account():
    print("Type 'back' at any time to return to the main menu.")
    
    while True:
        login = input("Please input 'proceed' to login into your account: ").strip().lower()
        if login == "back":
            return None
        if login == "proceed":
            print("Welcome to the Mini bank")
            break
        else:
            print("Error, please input 'proceed' again to continue or 'back' to return")
    while True:
        access = input("Please input 'continue' to access your account: ").strip().lower()
        if access == "back":
            return None
        if access == "continue":
            print("Access granted, welcome to your account")
            break
        else:
            print("Error, please input 'continue' again to access your account or 'back' to return")

    while True:
        username = input("Enter your username: ").strip()
        if username.lower() == "back":
            return None
        password = input("Enter your password: ").strip()
        if password.lower() == "back":
            return None

        account = all_accounts.get(username)
        if account and account["password"] == password:
            print(f"Login successful, welcome back {account['first_name']}")
            return account
        else:
            print("Login failed, incorrect username or password. Type 'back' to return to main menu.")
