create table if not exists evehicle (id INTEGER PRIMARY KEY AUTOINCREMENT,type INTEGER,zipcode INTEGER);
create table if not exists vrequest (id INTEGER PRIMARY KEY AUTOINCREMENT,type INTEGER,zipcode INTEGER,vid INTEGER)