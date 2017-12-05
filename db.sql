create table if not exists evehicle (id INTEGER PRIMARY KEY AUTOINCREMENT,type INTEGER,zipcode INTEGER);
create table if not exists vrequest (id INTEGER PRIMARY KEY AUTOINCREMENT,type INTEGER,zipcode INTEGER,vid INTEGER)
CREATE TABLE evehicle ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `type` INTEGER, `zipcode` INTEGER, `available` TEXT )