import sqlite3

conn = sqlite3.connect('test.db')
cur  = conn.cursor()

update_sql = "UPDATE users SET age = ? WHERE name=?"

user_input = input("请输入信息（修改的年龄,要修改人的姓名）：")
parts = user_input.split(",")  # ['1', 'Alice', '30']
# 转换数据类型
t = (int(parts[0]), parts[1],)
print(t)
print()


cur.execute(update_sql,t)
conn.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)


cur.close()
conn.close()