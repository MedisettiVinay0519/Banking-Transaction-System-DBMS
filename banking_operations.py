from db_connection import get_connection



def validate_account_status(cursor, account_id):
    cursor.execute(
        "SELECT status FROM accounts WHERE account_id = %s",
        (account_id,)
    )
    result = cursor.fetchone()

    if result is None:
        raise Exception("Account not found")

    status = result[0]

    if status != "ACTIVE":
        raise Exception(f"Account is {status}. Operation not allowed.")




def transfer_money(from_account, to_account, amount):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        if amount <= 0:
            raise Exception("Transfer amount must be positive")

        conn.start_transaction()

        validate_account_status(cursor, from_account)
        validate_account_status(cursor, to_account)

        cursor.execute(
            "SELECT balance FROM accounts WHERE account_id = %s FOR UPDATE",
            (from_account,)
        )
        balance = cursor.fetchone()[0]

        if balance < amount:
            raise Exception("Insufficient balance")

        cursor.execute(
            "UPDATE accounts SET balance = balance - %s WHERE account_id = %s",
            (amount, from_account)
        )

        cursor.execute(
            "UPDATE accounts SET balance = balance + %s WHERE account_id = %s",
            (amount, to_account)
        )

        cursor.execute(
            """
            INSERT INTO transactions
            (from_account, to_account, amount, status, txn_type)
            VALUES (%s, %s, %s, 'SUCCESS', 'TRANSFER')
            """,
            (from_account, to_account, amount)
        )

        txn_id = cursor.lastrowid

        cursor.execute(
            """
            INSERT INTO transaction_audit (txn_id, action, remarks)
            VALUES (%s, 'TRANSFER', 'Transfer successful')
            """,
            (txn_id,)
        )

        conn.commit()
        print("✅ Transfer successful")

    except Exception as e:
        conn.rollback()
        print("❌ Transfer failed:", str(e))

    finally:
        cursor.close()
        conn.close()


def withdraw_money(account_id, amount):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive")

        conn.start_transaction()

        validate_account_status(cursor, account_id)

        cursor.execute(
            "SELECT balance FROM accounts WHERE account_id = %s FOR UPDATE",
            (account_id,)
        )
        balance = cursor.fetchone()[0]

        if balance < amount:
            raise Exception("Insufficient balance")

        cursor.execute(
            "UPDATE accounts SET balance = balance - %s WHERE account_id = %s",
            (amount, account_id)
        )

        cursor.execute(
            """
            INSERT INTO transactions
            (from_account, to_account, amount, status, txn_type)
            VALUES (%s, NULL, %s, 'SUCCESS', 'WITHDRAW')
            """,
            (account_id, amount)
        )

        txn_id = cursor.lastrowid

        cursor.execute(
            """
            INSERT INTO transaction_audit (txn_id, action, remarks)
            VALUES (%s, 'WITHDRAW', 'Withdrawal successful')
            """,
            (txn_id,)
        )

        conn.commit()
        print("✅ Withdrawal successful")

    except Exception as e:
        conn.rollback()
        print("❌ Withdrawal failed:", str(e))

    finally:
        cursor.close()
        conn.close()

def check_balance(account_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT balance FROM accounts WHERE account_id = %s",
            (account_id,)
        )
        result = cursor.fetchone()

        if result is None:
            print("❌ Account not found")
        else:
            print(f"💰 Current Balance: {result[0]}")

    except Exception as e:
        print("❌ Error checking balance:", str(e))

    finally:
        cursor.close()
        conn.close()

def deposit_money(account_id, amount):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        if amount <= 0:
            raise Exception("Deposit amount must be positive")

        conn.start_transaction()

        validate_account_status(cursor, account_id)

        cursor.execute(
            "SELECT balance FROM accounts WHERE account_id = %s FOR UPDATE",
            (account_id,)
        )

        cursor.execute(
            "UPDATE accounts SET balance = balance + %s WHERE account_id = %s",
            (amount, account_id)
        )

        cursor.execute(
            """
            INSERT INTO transactions
            (from_account, to_account, amount, status, txn_type)
            VALUES (NULL, %s, %s, 'SUCCESS', 'DEPOSIT')
            """,
            (account_id, amount)
        )

        txn_id = cursor.lastrowid

        cursor.execute(
            """
            INSERT INTO transaction_audit (txn_id, action, remarks)
            VALUES (%s, 'DEPOSIT', 'Deposit successful')
            """,
            (txn_id,)
        )

        conn.commit()
        print("✅ Deposit successful")

    except Exception as e:
        conn.rollback()
        print("❌ Deposit failed:", str(e))

    finally:
        cursor.close()
        conn.close()