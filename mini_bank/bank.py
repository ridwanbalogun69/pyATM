from storage import save_accounts

def bank_operations(account):
    while True:
        print("\nSelect an operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Personal info")
        print("5. Transaction history")
        print("6. Exit")
        operation = input("Enter the number of the operation you want to perform: ").strip()

        if operation == "1":
            amount = input("Enter amount to deposit (or 0 to go back): ").strip()
            if amount == "0": continue
            account["balance"] += int(amount)
            account["transactions"].append(f"Deposited: {amount}")
            print(f"Deposit successful, your new balance is {account['balance']} naira")

        elif operation == "2":
            withdraw_amount = input("Enter amount to withdraw (or 0 to go back): ").strip()
            if withdraw_amount == "0": continue
            withdraw_amount = int(withdraw_amount)
            if withdraw_amount > account["balance"]:
                print("Insufficient funds")
                continue
            for _ in range(3):
                pin = input("Enter your 4-digit PIN to proceed (or 0 to go back): ").strip()
                if pin == "0": break
                if pin == account["pin"]:
                    account["balance"] -= withdraw_amount
                    account["transactions"].append(f"Withdrew: {withdraw_amount}")
                    save_accounts()
                    print(f"Withdrawal successful, new balance: {account['balance']}")
                    break
                else:
                    print("Incorrect PIN")
            else:
                print("Attempts exceeded")

        elif operation == "3":
            input(f"Your current balance is {account['balance']} naira\nPress Enter to go back")

        elif operation == "4":
            while True:
                print(f"Name: {account['first_name']} {account['last_name']}")
                print(f"Balance: {account['balance']} naira")
                edit = input("Enter 'edit profile' to update info or 0 to go back: ").strip().lower()
                if edit == "0": break
                if edit == "edit profile":
                    account["first_name"] = input("Enter new first name: ").strip()
                    account["last_name"] = input("Enter new last name: ").strip()
                    account["username"] = input("Enter new username: ").strip()
                    account["password"] = input("Enter new password: ").strip()
                    account["pin"] = input("Set up a new 4-digit PIN: ").strip()
                    save_accounts()
                    print("Profile updated successfully")
                    break

        elif operation == "5":
            input("\n".join(account["transactions"]) + "\nPress Enter to go back")

        elif operation == "6":
            print("Thank you for banking with us!")
            break
