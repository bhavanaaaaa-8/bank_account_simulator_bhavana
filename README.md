# Banking Simulator

## Description
A simple command-line banking simulator developed using Python. It allows users to check their account balance, deposit money, withdraw money, and view transaction history.

## Features
- **Balance Inquiry:** Displays the current account balance.
- **Deposit:** Adds money to the account.
- **Withdrawal:** Withdraws money only when the available balance is sufficient.
- **Transaction History:** Displays all successful transactions in the order they occurred.
- **Input Validation:** Prevents invalid deposit and withdrawal amounts.
- **Insufficient Balance Protection:** Prevents withdrawals greater than the available balance.

## Technologies Used
- Python 3
- Lists
- Functions
- Conditional statements
- Loops

## Initial Balance
The account starts with an initial balance of ₹1,000.

## How to Run

1. Install Python 3 on your computer.
2. Save the program as `banking_simulator.py`.
3. Open a terminal in the folder containing the file.
4. Run the following command:

   ```bash
   python banking_simulator.py
   ```

## Menu Options

1. Balance Inquiry
2. Deposit
3. Withdraw
4. Transaction History
5. Exit

## Example

```text
===== BANKING SIMULATOR =====
1. Balance Inquiry
2. Deposit
3. Withdraw
4. Transaction History
5. Exit

Enter your choice: 2
Enter deposit amount: Rs. 500
Deposit successful!

Enter your choice: 4

--- Transaction History ---
1. Deposited Rs. 500.00
```

## Validation Rules
- Deposit amounts must be greater than zero.
- Withdrawal amounts must be greater than zero.
- Withdrawals cannot exceed the available account balance.
- Only successful deposits and withdrawals are recorded in transaction history.

## Limitations
- The account balance starts at ₹1,000 each time the program runs.
- Transaction history is stored in memory and is cleared when the program exits.
- This is an educational project and is not connected to a real banking system.

## Future Enhancements
- Multiple user accounts
- PIN-based authentication
- Persistent transaction storage using files or a database
- Transaction dates and timestamps

## Author
Python Banking Simulator Project
