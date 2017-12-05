import sqlite3

DATABASE = 'route.db'

def init_db():
    db=sqlite3.connect(DATABASE)

    sql="create table if not exists evehicle (id INTEGER PRIMARY KEY AUTOINCREMENT,type INTEGER,zipcode INTEGER);"
    print(sql)
    db.cursor().execute(sql)
    db.commit()
	sql1="create table if not exists vrequest (id INTEGER PRIMARY KEY AUTOINCREMENT,type INTEGER,zipcode INTEGER,vid INTEGER);"
    db.cursor().execute(sql1)
    db.commit()
if __name__ == '__main__':
    init_db()