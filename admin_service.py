from db_connection import get_connection

def block_account(account_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE accounts SET status = 'BLOCKED' WHERE account_id = %s",
            (account_id,)
        )
        conn.commit()
        print("🚫 Account blocked successfully")

    except Exception as e:
        conn.rollback()
        print("❌ Failed to block account:", str(e))

    finally:
        cursor.close()
        conn.close()


def unblock_account(account_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE accounts SET status = 'ACTIVE' WHERE account_id = %s",
            (account_id,)
        )
        conn.commit()
        print("✅ Account unblocked successfully")

    except Exception as e:
        conn.rollback()
        print("❌ Failed to unblock account:", str(e))

    finally:
        cursor.close()
        conn.close()