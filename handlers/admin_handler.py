import sqlite3

def verify_admin(admin_id, password):
    admin_list = []

    with sqlite3.connect('bangazon.db') as conn:
        db = conn.cursor()

        db.execute("""
SELECT
    a.AdminId,
    a.Password
FROM Admin a
WHERE a.AdminId = ?
AND a.Password = ?
            """, (admin_id, password))

        conn.commit()
        admin_list = db.fetchone()

    if admin_list != None:
        return True
    else:
        return False
