from db_connection import get_connection


def get_transaction_history(account_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT
                txn_id,
                txn_type,
                from_account,
                to_account,
                amount,
                status,
                created_at
            FROM transactions
            WHERE from_account = %s
               OR to_account = %s
            ORDER BY created_at DESC
            """,
            (account_id, account_id)
        )

        rows = cursor.fetchall()

        if not rows:
            print("ℹ️ No transactions found for this account.")
            return

        print("\n📄 Transaction History")
        print("-" * 70)
        for r in rows:
            print(
                f"TxnID: {r['txn_id']} | "
                f"Type: {r['txn_type']} | "
                f"From: {r['from_account']} | "
                f"To: {r['to_account']} | "
                f"Amount: {r['amount']} | "
                f"Status: {r['status']} | "
                f"Date: {r['created_at']}"
            )

    except Exception as e:
        print("❌ Failed to fetch transaction history:", str(e))

    finally:
        cursor.close()
        conn.close()