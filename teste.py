import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='arthur',
                             password='root',
                             db='assistant_db',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS record()")
    print(cursor.fetchone())
    if cursor.fetchone() == None:
        connection = pymysql.connect(database='history')
