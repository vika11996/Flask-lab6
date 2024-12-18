import pandas as pd
import sqlite3
connection  = sqlite3.connect('present.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Status (
name TEXT NOT NULL,
kind TEXT NOT NULL,
price INTEGER,
status TEXT NOT NULL
)
''')
sql = 'INSERT INTO Status (name, kind, price, status) VALUES (?, ?, ?, ?)'
data = [('Иванов Иван Иванович', 'санки', 2000, 'куплен'),
        ('Федоров Федор Федорович', 'варежки', 1000, 'куплен'),
        ('Дворецкий Константин Константинович', 'перчатки', 400, 'куплен'),
        ('Григорьева Анастасия Григорьевна', 'кухонный набор', 6000, ' не куплен'),
        ('Иванищев Иван Иванович', 'водолазный костюм', 15000, 'не куплен'),
        ('Иванов Иван Петрович', 'мотор', 3000, 'куплен'),
        ('Андронов Андрон Иванович', 'снаряжение для рыбалки', 7000, 'куплен'),
        ('Петров Иван Иванович', 'ружье', 75000, 'не куплен'),
        ('Сидоров Василий Васильевич', 'лодка', 15000, 'не куплен'),
        ('Петров Петр Петрович', 'водка', 150, 'не куплен')]
with connection:
    connection.executemany(sql, data)
sql = '''
            select *
            from Status

'''
#print(pd.read_sql(sql, connection))


from flask import Flask, render_template, request, make_response

HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "present.db"
app = Flask(__name__)
# app.debug = True

def getpresent():
  conn = sqlite3.connect(DBFILE)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM `Status`")
  results = cursor.fetchall()
  conn.close()
  return results

@app.route('/')
def start():
    return "<h1>Добавьте /hello в поисковую строку </h1>"

@app.route("/hello", methods=['GET'])
def index():

    users = getpresent()
    # print(users)

    return render_template("flask.html", usr=users)

if __name__ == "__main__":
    app.run(HOST_NAME, HOST_PORT)