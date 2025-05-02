# Initialize balance and transcation history
balance = 0
history = []

# Add Income
def add_income():
    global balance
    amount = float(input("Enter income amount: $"))
    balance += amount
    history.append(("Income", amount))
    print(f"Income of ${amount} added!")

#Add Expense
def add_expense():
    global balance
    amount = float(input("Enter expense amount: $"))
    balance -= amount
    history.append(("Expense", amount))
    print(f"Expense of ${amount} recorded.")

def show_balance():
    print(f"\nYour current balance is: ${balance}\n")

def show_history():
    print("\nTransaction History:")
    for item in history:
        print(f"{item[0]}: ${item[1]}")
    print()

while True:
    print("=== Expense Tracker ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Show History")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        show_balance()
    elif choice == "4":
        show_history()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
