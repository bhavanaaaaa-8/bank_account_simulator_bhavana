
balance = 1000.0
transactions = []


def balance_inquiry():
    print(f"Current Balance: Rs. {balance:.2f}")


def deposit():
    global balance
    amount = float(input("Enter deposit amount: Rs. "))

    if amount > 0:
        balance += amount
        transactions.append(f"Deposited Rs. {amount:.2f}")
        print("Deposit successful!")
    else:
        print("Enter a valid amount.")


def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: Rs. "))

    if amount <= 0:
        print("Enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        transactions.append(f"Withdrawn Rs. {amount:.2f}")
        print("Withdrawal successful!")


def transaction_history():
    print("\n--- Transaction History ---")

    if not transactions:
        print("No transactions yet.")
    else:
        for i, transaction in enumerate(transactions, start=1):
            print(f"{i}. {transaction}")


def main():
    while True:
        print("\n===== BANKING SIMULATOR =====")
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            balance_inquiry()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transaction_history()
        elif choice == "5":
            print("Thank you for using our bank!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
