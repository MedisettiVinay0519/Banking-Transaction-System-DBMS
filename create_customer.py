from db_connection import get_connection


def create_customer(
    first_name,
    last_name,
    phone,
    email,
    date_of_birth,
    street_no,
    city,
    state,
    pincode
):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO customers
            (first_name, last_name, phone, email, date_of_birth,
             street_no, city, state, pincode)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                first_name,
                last_name,
                phone,
                email,
                date_of_birth,
                street_no,
                city,
                state,
                pincode
            )
        )

        conn.commit()
        customer_id = cursor.lastrowid
        print(f"✅ Customer created successfully. Customer ID: {customer_id}")
        return customer_id

    except Exception as e:
        conn.rollback()
        print("❌ Failed to create customer:", str(e))
        return None

    finally:
        cursor.close()
        conn.close()