from db_connection import get_connection


def create_account(customer_id, account_type, initial_balance):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        if initial_balance < 0:
            raise Exception("Initial balance cannot be negative")

        cursor.execute(
            "SELECT customer_id FROM customers WHERE customer_id = %s",
            (customer_id,)
        )
        if cursor.fetchone() is None:
            raise Exception("Customer does not exist")

        cursor.execute(
            """
            INSERT INTO accounts
            (customer_id, account_type, balance, status)
            VALUES (%s, %s, %s, 'ACTIVE')
            """,
            (customer_id, account_type, initial_balance)
        )

        conn.commit()
        account_id = cursor.lastrowid
        print(f"✅ Account created successfully. Account ID: {account_id}")
        return account_id

    except Exception as e:
        conn.rollback()
        print("❌ Failed to create account:", str(e))
        return None

    finally:
        cursor.close()
        conn.close()