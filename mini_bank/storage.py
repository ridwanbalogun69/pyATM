import json

all_accounts = {}

def save_accounts():
    with open("accounts.json", "w") as file:
        json.dump(all_accounts, file, indent=4)

def load_accounts():
    global all_accounts
    try:
        with open("accounts.json", "r") as file:
            all_accounts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        all_accounts = {}
