import sqlite3
co = sqlite3.connect("signupfile1.db")
c= co.cursor()
c.execute('CREATE TABLE IF NOT EXISTS example(id integer PRIMARY KEY AUTOINCREMENT ,email text,Username text, '         
          'password text,permission text)')
c.execute('INSERT INTO example (email, Username, password, permission) VALUES '
          '("01122471@gmail.com","A471", "012345","admin")')
c.execute('INSERT INTO example (email, Username, password, permission) VALUES '
          '("01122472@gmail.com","A472", "0012345","admin")')
c.execute('INSERT INTO example (email, Username, password, permission) VALUES '
          '("01122473@gmail.com","A473", "00012345","admin")')
c.execute('INSERT INTO example (email, Username, password, permission) VALUES '
          '("01122474@gmail.com","A474", "000012345","admin")')
co.commit()