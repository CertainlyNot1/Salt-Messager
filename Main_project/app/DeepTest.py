import psycopg2

try:
    conn = psycopg2.connect(
        host="db.mqlntyaeouzjecpjtwga.supabase.co",
        database="postgres",
        user="postgres",
        password="12345670709090ABCs",
        port=5432
    )
    print("Підключення успішне!")
    conn.close()
except Exception as e:
    print(f"Помилка: {e}")