__author__ = 'abdul'


import sqlite3
conn = sqlite3.connect('pytrix.db')
c = conn.cursor()

# conn.execute('''CREATE TABLE Log
#        (ID INTEGER PRIMARY KEY    AUTOINCREMENT,
#        text           TEXT    NOT NULL);''')

# c.execute("INSERT INTO Log(text) VALUES('hola dogs, fijense que este es otro text ehhh pos kiobo') ")
# c.execute("SELECT * FROM Log;")


def agregar(texto):
    t = (texto)
    c.execute('insert into Log(text) values ("%s")'% t)
    c.execute("SELECT * FROM Log;")
    cur =c.fetchall()
    print(cur)


conn.commit()