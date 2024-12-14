from faker import Faker
from tabulate import tabulate
from pyjokes import get_joke

accounts = []

def generate_fake_data():
    fake = Faker()
    return {"Name": fake.name(), 
            "Address": fake.address(), 
            "Email": fake.email()}

def print_random_joke():
    print("===============")
    j = get_joke()
    print(j)
    print("===============")

def print_accounts():
    header = accounts[0].keys()
    rows = [x.values() for x in accounts]
    print(tabulate(rows, header))

def generate_Accounts():
    count = int(input("How many accounts you want to generate?: "))
    for _ in range(count): 
        accounts.append(generate_fake_data())

choice = ""
while choice != "4":
    print("Menu:")
    print("1. Generate accounts")
    print("2. Display accounts")
    print("3. Say a joke")
    print("4. Exit")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            generate_Accounts()
        case "2":
            print_accounts()
        case "3":
            print_random_joke()
        case "4":
            print("Bye! Bye!")
        case _:
            print("Invalid choice.")