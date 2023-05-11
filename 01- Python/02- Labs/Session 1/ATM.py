# Define the initial account balances
accounts = {
    'Alice': 5000,
    'Bob': 3000,
    'Charlie': 10000
}

# Define the denominations of bills available in the ATM
denominations = (1000, 500, 200, 100)

# Define a function to withdraw money from an account
def withdraw(account_name, amount):
    if account_name in accounts:
        balance = accounts[account_name]
        if amount <= balance:
            print(f"Withdrawing {amount} from {account_name} account")
            for denomination in denominations:
                count = amount // denomination
                if count > 0:
                    print(f"{count} x {denomination} bill(s)")
                    amount -= count * denomination
            accounts[account_name] -= amount
            print(f"New balance for {account_name}: {accounts[account_name]}")
        else:
            print(f"Insufficient balance in {account_name} account")
    else:
        print(f"{account_name} account not found")

# Define a function to deposit money into an account
def deposit(account_name, amount):
    if account_name in accounts:
        print(f"Depositing {amount} into {account_name} account")
        accounts[account_name] += amount
        print(f"New balance for {account_name}: {accounts[account_name]}")
    else:
        print(f"{account_name} account not found")

# Define a function to check the balance of an account
def check_balance(account_name):
    if account_name in accounts:
        print(f"Current balance of {account_name} account: {accounts[account_name]}")
    else:
        print(f"{account_name} account not found")

# Test the functions
withdraw('Alice', 2500)
deposit('Bob', 1000)
check_balance('Charlie')