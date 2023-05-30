import mysql.connector

class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='base_datos', 
                                            user = 'root',
                                            password ='')
    def busca_users(self, users):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM login_datos WHERE Users = {}".format(users)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()     
        return usersx 

    def busca_password(self, password):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM login_datos WHERE Password = {}".format(password)
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()     
        return passwordx

    def actualiza_password(self, users, password):
        cur = self.conexion.cursor()
        sql ='''UPDATE login_datos SET Password = '{}'
        WHERE USERS = '{}' '''.format(password,users)
        cur.execute(sql)
        a = cur.rowcount
        # Se guarde y persista simpre
        self.conexion.commit()    
        cur.close()
        return a   