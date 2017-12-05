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
            c.execute("select * from distance where zipcode1=%s and  distance<>0 and zipcode2 is not %s or zipcode1=%s and  distance<>0 and zipcode2 is not %s order by distance,zipcode1 asc"%(zip1,zip,zip2,zip))
            result=c.fetchall()
            increment=0
            new_distance=[]
            new_zip1=[]
            new_zip2=[]
            for val in result:
                print(val)
                increment=increment+1
                new_distance.append(val[3])
                new_zip1.append(val[1])
                new_zip2.append(val[2])
            print(new_distance)
            print(new_zip1)
            print(new_zip2)
			
			if(increment==1):

                if(zip1==new_zip1[0]):
                    print("if increment=1 if ")
                    length=0
                    total_distance=new_distance[0]+distance1
                    check_status(new_zip2[0], total_distance, type, zip)
                else:
                    print("if increment=1 else")
                    length=0
                    total_distance = new_distance[0] + distance2
                    check_status(new_zip2[0], total_distance, type, zip)






if __name__ == '__main__':
    start_algo()