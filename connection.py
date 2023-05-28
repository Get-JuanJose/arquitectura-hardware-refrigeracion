import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user= 'root',
            password='admin',
            db='temperaturas'
        )
        self.cursor = self.connection.cursor()
        print("Conectado")

    def selectAllAndWrite(self):
        sql='select * from temperaturas'
        file = open("data.csv", "w")
        file.write("fecha")
        file.write(",")
        file.write("temperatura")
        try:
            self.cursor.execute(sql)
            temps = self.cursor.fetchall()
    
            for temp in temps:
                temps2 = str(temp[1])
                file.write("\n")
                file.write(temps2)
                file.write(",")
                temps2 = str(temp[2])
                file.write(temps2)
        except Exception as e:
            raise 

    def insertInto(self, id):
        values = (str(id), '800')
        sql= "insert into temperaturas (id, date, temperatura) values (%s, curtime(), %s)"
        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
        except Exception as e:
            raise   
