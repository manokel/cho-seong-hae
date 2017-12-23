import pymysql.cursors

def connectDB():
    conn = pymysql.connect(host ='localhost',
                           user='root',
                           password='1234',
                           db='zoo',
                           charset ='utf8')
    return conn

def insertDB():
    conn = connectDB()
    with conn.cursor() as cursor:
        sql = 'insert into zoo_manager(type, number) values(%s , %s)'
        cursor.execute(sql,('hamster', 10))
        conn.commit()
        conn.close()

def updateDB():
    conn = connectDB()
    with conn.cursor() as cursor:
        sql = 'update zoo_manager SET number = %s where type =  %s'
        cursor.execute(sql, (7, 'dog'))
        conn.commit()
        conn.close()

def selectDB():
    conn = connectDB()
    with conn.cursor() as cursor:
        sql = 'select * from zoo_manager'
        cursor.execute(sql)
        prt = cursor.fetchall()
        print(prt)
        conn.close()

def deleteDB():
    conn = connectDB()
    with conn.cursor() as cursor:
        sql = 'DELETE from zoo_manager where type = %s'
        cursor.execute(sql, ('hamster'))
        conn.commit()
        conn.close()

def main():
    deleteDB()


main()