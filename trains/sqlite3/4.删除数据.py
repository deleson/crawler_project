import sqlite3

conn = sqlite3.connect('test.db')
cur  = conn.cursor()

delete_sql = "DELETE FROM users WHERE name = ?"

user_input = input("请输入信息（要删除的姓名）：")
parts = user_input.split(",")  # ['1', 'Alice', '30']
# 转换数据类型
t = (parts[0],)
print(t)
print()

cur.execute(delete_sql,t)
conn.commit()


cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)


cur.close()
conn.close()
