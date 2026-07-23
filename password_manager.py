from pathlib import Path
import json


def menu():

    print("================\n" \
    "Password Manager\n" \
    "================\n" \
    "\n1. Add Password" \
    "\n2. Delete Passwords" \
    "\n3. Load Passwords" \
    "\n4. Search Passwords"
    "\n5. Exit Password Manager")

    selection_choice = input("\nPlease input your choice: " \
    "\n")


    if selection_choice == "1":
        add_password()
    elif selection_choice == "2":
        delete_password()
    elif selection_choice == "3":
        load_passwords()
    elif selection_choice == "4":
        search_password()
    elif selection_choice == "5":
        quit()
    else:
        print("Invalid Selection. Please try again.")

passwords_file = Path("data/passwords.json")

def add_password():

    website = input("======================\n"
                "What is the website?: ")

    username = input("======================\n"
                    "What is your username?: ")

    password = input("======================\n"
                "What is the password used?: ")
    
    password_entry = {
        "Website": website,
        "Username": username,
        "Password": password
    }

    save_passwords(password_entry)

def delete_password():

    if passwords_file.stat().st_size == 0:
            print(
            "=================\n"
            "No profiles found.\n"
            "=================\n"
            )
            return
    
    with passwords_file.open("r") as file:
        passwords = json.load(file)

    print(
    "=================\n"
    "Available Profiles\n"
    "=================\n"
    )
    for number, password in enumerate(passwords, start=1):
        print(f"{number}. {password['Website']} ({password['Username']})")

    delete_request = int(input("\nWhich password would you like to delete?"))

    if delete_request < 1 or delete_request > len(passwords):
        print("Please input a valid number. ")
        return

    passwords.pop(delete_request - 1)
    print("=========================" \
    "\nPassword Deleted" \
    "\n=========================")

    with passwords_file.open("w") as file:
        json.dump(passwords, file, indent=4)

def search_password():

    if passwords_file.stat().st_size == 0:
            print(
            "=================\n"
            "No profiles found.\n"
            "=================\n"
            )
            return

    with passwords_file.open("r") as file:
        passwords = json.load(file)

    search_request = input("Please write what website you would like to search for: ").lower()

    found = False

    for number, password in enumerate(passwords, start=1):
        if search_request in password["Website"].lower():
            found = True
            print(f"{number}. {password['Website']} ({password['Username']} | {password['Password']})")
    if not found:
        print("Website not found. Please try again.")

def load_passwords():

    if passwords_file.stat().st_size == 0:
        print(
        "=================\n"
        "No profiles found.\n"
        "=================\n"
        )
        return
    
    with passwords_file.open("r") as file:
        passwords = json.load(file)

    print(
    "=================\n"
    "Available Profiles\n"
    "=================\n"
    )
    for number, password in enumerate(passwords, start=1):
        print(f"{number}. {password['Website']} ({password['Username']})")

def save_passwords(password_entry):
    passwords_file.parent.mkdir(parents=True, exist_ok=True)
    passwords_file.touch(exist_ok=True)
    passwords = []

    if passwords_file.stat().st_size > 0:
        with passwords_file.open("r") as file:
            passwords = json.load(file)

    passwords.append(password_entry)

    with passwords_file.open("w") as file:
        json.dump(passwords, file, indent=4)
    print("Password saved successfully.")