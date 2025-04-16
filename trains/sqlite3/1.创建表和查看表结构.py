import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()


# 创建表
create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
        )
"""

show_table_struct ="SHOW TABLES"

cur.execute(create_table_sql)
conn.commit()


# 查看表结构（字段名、数据类型等）
table_name = 'users'
show_table_info_sql = f"PRAGMA table_info({table_name});"
cur.execute(show_table_info_sql)
columns = cur.fetchall()
print(f"Structure of table '{table_name}':")
for col in columns:
    print(col)


cur.close()
conn.close()