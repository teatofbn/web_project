import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Добавить первую задачу', 'Попробуйте самостоятельно составить свою первую задачу')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Изменить задачу', 'А теперь попробуйте изменить ту задачу: добавить туда каких-то деталей, дедлай, например'
                                ', или же полностью изменить суть задачи')
            )

connection.commit()
connection.close()
