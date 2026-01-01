from account import create_account, login_account
from bank import bank_operations  
from storage import load_accounts, all_accounts
load_accounts()

while True:
    print("Welcome to Mini Bank")
    print("1. Login")
    print("2. Sign Up")
    print("3. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        account = login_account()
        bank_operations(account)
    elif choice == "2":
        account = create_account()
        bank_operations(account)
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid choice. Try again.")
