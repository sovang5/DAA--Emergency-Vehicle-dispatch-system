import sqlite3
DATABASE = 'route.db'

def connect_db():
    global conn,c
    conn = sqlite3.connect(DATABASE)
    c=conn.cursor()
def close_db():
    conn.commit()
    conn.close()

def start_algo():
    global zip,car_type,length
    global i
    global count,distance
    zip=input("Enter your Zipcode\n")
    car_type=input("Enter the type of the car\n")
    connect_db()
    c.execute("select * from distance where zipcode1=%s order by distance asc"%zip)
    rows=c.fetchall()
    count=[]
    distance=[]
    length=0
    i = 0
    for val in rows:
        print(val)
        length=length+1
        distance.append(val[3])
        count.append(val[2])
        print("zipcode ",count)
        print('distance ',distance)
        print('length ',length)

    check_status(count[i],distance[i],car_type,zip)
    close_db()
def check_status(position,distant,type,zip):
    global i,length
    i = i + 1
    c.execute("select * from evehicle where zipcode=%s and type=%s and available='y'" % (position,type));
    rows = c.fetchall()
    if (rows):
        print(rows[0][0]);
        c.execute("insert into assign values(%s,%s,%s,%s)"%(type,zip,rows[0][0],distant));
        c.execute("update evehicle set available='n' where id=%s"%rows[0][0]);
        c.execute("select * from assign");
        #
    elif (i<length):
        print(count[i])
        print(distance[i])
        check_status(count[i],distance[i],type,zip)
        i=i+1
    else:
        if(length>2):

            zip1=count[1]
            zip2 = count[2]
            print("if length>2")
            print(zip1)
            print(zip2)
            print(zip)
            distance1=distance[1]
            distance2=distance[2]
            






if __name__ == '__main__':
    start_algo()