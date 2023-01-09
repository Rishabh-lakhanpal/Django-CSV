import csv
import mysql.connector
# Database connection 
def connection():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root', 
            password='',  
            database='student'
        )
        if(conn):
            print("Database connected...")
            return conn
    except Exception as e:
        print("Exception ", e)


def readCSV():
    con = connection()
    cursor = con.cursor()

    with open('student.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        skipHeader = True
        for line in csv_reader:
            print(line)
            if skipHeader:
                skipHeader = False
                continue

            sql = 'INSERT INTO student_table(name, role_no, email, test) VALUES(%s, %s, %s, %s)'
            record = tuple(line)
            cursor.execute(sql, record)
            con.commit()
readCSV()