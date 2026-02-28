from db_connection import get_connection

def close_account(account_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        conn.start_transaction()

        cursor.execute(
            "SELECT balance, status FROM accounts WHERE account_id = %s FOR UPDATE",
            (account_id,)
        )
        result = cursor.fetchone()

        if result is None:
            raise Exception("Account not found")

        balance, status = result

        if status == "CLOSED":
            raise Exception("Account is already closed")

        if balance != 0:
            raise Exception("Account balance must be zero before closure")

        cursor.execute(
            "UPDATE accounts SET status = 'CLOSED' WHERE account_id = %s",
            (account_id,)
        )

        conn.commit()
        print("✅ Account closed successfully")

    except Exception as e:
        conn.rollback()
        print("❌ Account closure failed:", str(e))

    finally:
        cursor.close()
        conn.close()

