from db_connection import get_connection

def generate_monthly_statement(account_id, year, month):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT
                txn_type,
                from_account,
                to_account,
                amount,
                created_at
            FROM transactions
            WHERE (from_account = %s OR to_account = %s)
              AND YEAR(created_at) = %s
              AND MONTH(created_at) = %s
              AND status = 'SUCCESS'
            ORDER BY created_at
            """,
            (account_id, account_id, year, month)
        )

        rows = cursor.fetchall()

        if not rows:
            print("ℹ️ No transactions for this period")
            return

        total_credit = 0
        total_debit = 0

        for r in rows:
            if r["to_account"] == account_id:
                total_credit += r["amount"]
            if r["from_account"] == account_id:
                total_debit += r["amount"]

        cursor.execute(
            "SELECT balance FROM accounts WHERE account_id = %s",
            (account_id,)
        )
        closing_balance = cursor.fetchone()["balance"]

        opening_balance = closing_balance - total_credit + total_debit

        print("\n📄 Monthly Statement")
        print(f"Account ID: {account_id}")
        print(f"Period: {month}/{year}")
        print("-" * 40)
        print(f"Opening Balance : {opening_balance}")
        print(f"Total Credit    : {total_credit}")
        print(f"Total Debit     : {total_debit}")
        print(f"Closing Balance : {closing_balance}")

    except Exception as e:
        print("❌ Failed to generate statement:", str(e))

    finally:
        cursor.close()
        conn.close()