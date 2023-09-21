import sqlite3
co = sqlite3.connect("signupfile1.db")
c= co.cursor()
c.execute('CREATE TABLE IF NOT EXISTS example(id integer PRIMARY KEY AUTOINCREMENT ,email text,Username text, '         
          'password text,permission text)')
c.execute('INSERT INTO example (email, Username, password, permission) VALUES '
          '("01122571@gmail.com","S571", "0123456","Sales Staff")')
c.execute('INSERT INTO example (email, Username, password, permission) VALUES '
          '("01122572@gmail.com","S572", "00123456","Sales Staff")')
c.execute('INSERT INTO example (email, Username, password, permission) VALUES '
          '("01122573@gmail.com","S573", "00123456","Sales Staff")')
co.commit()