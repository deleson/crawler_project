import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

insert_sql = "INSERT OR IGNORE INTO users(name,age,email) VALUES (?,?,?)"
users_data = [
    ('shit',30,'2221735462@qq.com'),
    ('big',130,'2421735462@qq.com'),
    ('king',30,'2321735462@qq.com')
]

cur.executemany(insert_sql,users_data)
conn.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)


cur.close()
conn.close()