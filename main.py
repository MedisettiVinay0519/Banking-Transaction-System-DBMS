from create_customer import create_customer
from create_account import create_account

from banking_operations import (
    deposit_money,
    withdraw_money,
    transfer_money,
    check_balance
)

from trans_hist import get_transaction_history
from account_service import close_account
from monthly_Statement import generate_monthly_statement
from admin_service import block_account, unblock_account


def main():
    while True:
        print("\n========== Banking Transaction Management System ==========")
        print("1. Create Customer")
        print("2. Create Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Check Balance")
        print("7. Transaction History")
        print("8. Monthly Statement")
        print("9. Close Account")
        print("10. Block Account (Admin)")
        print("11. Unblock Account (Admin)")
        print("12. Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        # 1️⃣ Create Customer
        if choice == 1:
            print("\n--- Create Customer ---")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            street = input("Street No: ")
            city = input("City: ")
            state = input("State: ")
            pincode = input("Pincode: ")

            create_customer(
                first_name, last_name, phone, email,
                dob, street, city, state, pincode
            )

        # 2️⃣ Create Account
        elif choice == 2:
            print("\n--- Create Account ---")
            customer_id = int(input("Customer ID: "))
            account_type = input("Account Type (SAVINGS/CURRENT): ")
            initial_balance = float(input("Initial Balance: "))
            create_account(customer_id, account_type, initial_balance)

        # 3️⃣ Deposit
        elif choice == 3:
            print("\n--- Deposit ---")
            account_id = int(input("Account ID: "))
            amount = float(input("Amount to deposit: "))
            deposit_money(account_id, amount)

        # 4️⃣ Withdraw
        elif choice == 4:
            print("\n--- Withdraw ---")
            account_id = int(input("Account ID: "))
            amount = float(input("Amount to withdraw: "))
            withdraw_money(account_id, amount)

        # 5️⃣ Transfer
        elif choice == 5:
            print("\n--- Transfer ---")
            from_account = int(input("Sender Account ID: "))
            to_account = int(input("Receiver Account ID: "))
            amount = float(input("Amount to transfer: "))
            transfer_money(from_account, to_account, amount)

        # 6️⃣ Check Balance
        elif choice == 6:
            print("\n--- Check Balance ---")
            account_id = int(input("Account ID: "))
            check_balance(account_id)

        # 7️⃣ Transaction History
        elif choice == 7:
            print("\n--- Transaction History ---")
            account_id = int(input("Account ID: "))
            get_transaction_history(account_id)

        # 8️⃣ Monthly Statement
        elif choice == 8:
            print("\n--- Monthly Statement ---")
            account_id = int(input("Account ID: "))
            year = int(input("Year (YYYY): "))
            month = int(input("Month (1-12): "))
            generate_monthly_statement(account_id, year, month)

        # 9️⃣ Close Account
        elif choice == 9:
            print("\n--- Close Account ---")
            account_id = int(input("Account ID: "))
            close_account(account_id)

        # 🔟 Block Account
        elif choice == 10:
            print("\n--- Block Account (Admin) ---")
            account_id = int(input("Account ID: "))
            block_account(account_id)

        # 1️⃣1️⃣ Unblock Account
        elif choice == 11:
            print("\n--- Unblock Account (Admin) ---")
            account_id = int(input("Account ID: "))
            unblock_account(account_id)

        # 1️⃣2️⃣ Exit
        elif choice == 12:
            print("👋 Exiting Banking System. Thank you!")
            break

        else:
            print("❌ Invalid option. Please try again.")


if __name__ == "__main__":
    main()