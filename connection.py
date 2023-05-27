import pymysql

class database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user= 'root',
            password='',
            db='temperature'
        )
        self.cursor = self.connection.cursor()
        print("SaS")

    def selectAll(self):
        sql='select * from temperature'

        try:
            self.cursor.execute(sql)
            temps = self.cursor.fetchall()

            for temp in temps:
                print("id:", temp[0])
                print("date:", temp[1])
                print("temperature:", temp[2])
        except Exception as e: 
            raise

database = database()
database.selectAll()